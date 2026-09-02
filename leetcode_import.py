#!/usr/bin/env python3
"""
One-time LeetCode import script for past accepted submissions.
Run once to backfill your GitHub repo with historical solves.

Usage:
  export GH_PAT="ghp_xxx"  # fine-grained PAT with repo contents write
  python3 leetcode_import.py [--username YOUR_LEETCODE_USERNAME] [--dry-run]
"""

import os
import sys
import json
import time
import base64
import argparse
import getpass
from pathlib import Path
from typing import Optional, List, Dict, Any

import requests

GITHUB_API = "https://api.github.com"
LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
REPO_OWNER = "vatsalyd"
REPO_NAME = "learning"

DIFFICULTY_MAP = {1: "easy", 2: "medium", 3: "hard"}
LANG_EXT = {
    "python3": "py", "python": "py", "java": "java", "cpp": "cpp", "c": "c",
    "csharp": "cs", "javascript": "js", "typescript": "ts", "go": "go",
    "rust": "rs", "ruby": "rb", "swift": "swift", "kotlin": "kt", "php": "php",
    "scala": "scala", "r": "r", "dart": "dart", "elixir": "ex", "erlang": "erl",
    "racket": "rkt"
}

SESSION = requests.Session()


def log(msg: str, level: str = "INFO"):
    prefix = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌"}.get(level, "•")
    print(f"{prefix} {msg}")


def github_request(method: str, path: str, pat: str, **kwargs) -> requests.Response:
    headers = {
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "LeetCode-Import-Script/1.0"
    }
    url = f"{GITHUB_API}{path}"
    resp = SESSION.request(method, url, headers=headers, **kwargs)
    if resp.status_code >= 400:
        try:
            err = resp.json().get("message", resp.text)
        except:
            err = resp.text
        raise RuntimeError(f"GitHub API {resp.status_code}: {err}")
    return resp


def leetcode_graphql(query: str, variables: dict, cookies: dict = None) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/",
        "Origin": "https://leetcode.com",
        "User-Agent": "LeetCode-Import-Script/1.0"
    }
    resp = SESSION.post(LEETCODE_GRAPHQL, json={"query": query, "variables": variables}, headers=headers, cookies=cookies)
    if resp.status_code >= 400:
        raise RuntimeError(f"LeetCode GraphQL {resp.status_code}: {resp.text}")
    data = resp.json()
    if data.get("errors"):
        raise RuntimeError(f"GraphQL errors: {data['errors']}")
    return data["data"]


def get_file_path(difficulty: int, title_slug: str, lang: str) -> str:
    ext = LANG_EXT.get(lang.lower(), lang.lower())
    diff_folder = DIFFICULTY_MAP.get(difficulty, "unknown")
    return f"leetcode/{diff_folder}/{title_slug}.{ext}"


def file_exists_on_github(pat: str, path: str) -> bool:
    try:
        github_request("GET", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}", pat)
        return True
    except RuntimeError as e:
        if "404" in str(e):
            return False
        raise


def get_file_sha(pat: str, path: str) -> Optional[str]:
    try:
        resp = github_request("GET", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}", pat)
        return resp.json()["sha"]
    except RuntimeError as e:
        if "404" in str(e):
            return None
        raise


def commit_file(pat: str, path: str, content: str, message: str, sha: Optional[str] = None) -> dict:
    body = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "committer": {"name": "LeetCode Import", "email": "leetcode-import@users.noreply.github.com"},
        "branch": "main"
    }
    if sha:
        body["sha"] = sha
    resp = github_request("PUT", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}", pat, json=body)
    return resp.json()


def hash_code(code: str) -> str:
    import hashlib
    return hashlib.sha256(code.encode()).hexdigest()[:16]


def get_all_ac_submissions(leetcode_session: str, username: str) -> List[Dict]:
    """Fetch all accepted submissions for a user via GraphQL."""
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id
        title
        titleSlug
        timestamp
        lang
        statusDisplay
        runtime
        memory
      }
    }
    """
    cookies = {"LEETCODE_SESSION": leetcode_session} if leetcode_session else None
    data = leetcode_graphql(query, {"username": username, "limit": 5000}, cookies)
    return data["recentAcSubmissionList"]


def get_submission_code(submission_id: int, leetcode_session: str) -> Dict:
    """Fetch full submission details including code."""
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang
        runtime
        memory
        statusDisplay
        timestamp
        question {
          titleSlug
          title
          difficulty
          frontendQuestionId
        }
      }
    }
    """
    cookies = {"LEETCODE_SESSION": leetcode_session} if leetcode_session else None
    data = leetcode_graphql(query, {"submissionId": submission_id}, cookies)
    return data["submissionDetails"]


def get_question_difficulty(title_slug: str, leetcode_session: str) -> int:
    """Fetch question difficulty if not in submission."""
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
      }
    }
    """
    cookies = {"LEETCODE_SESSION": leetcode_session} if leetcode_session else None
    data = leetcode_graphql(query, {"titleSlug": title_slug}, cookies)
    diff_map = {"Easy": 1, "Medium": 2, "Hard": 3}
    return diff_map.get(data["question"]["difficulty"], 1)


def main():
    parser = argparse.ArgumentParser(description="Import past LeetCode solves to GitHub")
    parser.add_argument("--username", help="LeetCode username (required for public profile fetch)")
    parser.add_argument("--leetcode-session", help="LeetCode SESSION cookie (for private/profile access)")
    parser.add_argument("--gh-pat", help="GitHub PAT (or set GH_PAT env var)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without committing")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of submissions to process (0 = all)")
    parser.add_argument("--offset", type=int, default=0, help="Skip first N submissions")
    args = parser.parse_args()

    pat = args.gh_pat or os.getenv("GH_PAT")
    if not pat:
        pat = getpass.getpass("Enter GitHub PAT (fine-grained, repo contents write): ").strip()
    if not pat:
        log("GitHub PAT required", "ERROR")
        sys.exit(1)

    if not args.username and not args.leetcode_session:
        log("Either --username (public) or --leetcode-session (private) required", "ERROR")
        sys.exit(1)

    leetcode_session = args.leetcode_session or os.getenv("LEETCODE_SESSION")

    log(f"Fetching accepted submissions for {args.username or 'authenticated user'}...")
    try:
        submissions = get_all_ac_submissions(leetcode_session, args.username or "")
    except Exception as e:
        log(f"Failed to fetch submissions: {e}", "ERROR")
        log("Tip: Provide --leetcode-session cookie from browser for private profiles", "WARN")
        sys.exit(1)

    log(f"Found {len(submissions)} accepted submissions")

    processed = 0
    skipped = 0
    errors = 0

    for i, sub in enumerate(submissions):
        if i < args.offset:
            continue
        if args.limit and processed >= args.limit:
            break

        title_slug = sub["titleSlug"]
        log(f"\n[{i+1}/{len(submissions)}] {sub['title']} ({title_slug})")

        try:
            details = get_submission_code(sub["id"], leetcode_session)
            if not details.get("code"):
                log("  No code in submission, skipping", "WARN")
                skipped += 1
                continue

            difficulty = details["question"]["difficulty"] if details.get("question") else get_question_difficulty(title_slug, leetcode_session)
            lang = details["lang"]
            code = details["code"]
            runtime = details.get("runtime", "N/A")
            memory = details.get("memory", "N/A")
            frontend_id = details["question"]["frontendQuestionId"] if details.get("question") else "?"

            file_path = get_file_path(difficulty, title_slug, lang)

            if file_exists_on_github(pat, file_path):
                existing_sha = get_file_sha(pat, file_path)
                existing_resp = github_request("GET", f"/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}", pat)
                existing_content = base64.b64decode(existing_resp.json()["content"]).decode("utf-8")
                if hash_code(existing_content) == hash_code(code):
                    log(f"  Identical content exists, skipping", "WARN")
                    skipped += 1
                    continue
                log(f"  Different version exists, updating", "WARN")
            else:
                existing_sha = None

            message = (
                f"feat(leetcode): add {sub['title']} ({DIFFICULTY_MAP.get(difficulty, 'unknown')}) [{frontend_id}]\n\n"
                f"Language: {lang}\nRuntime: {runtime}ms\nMemory: {memory}MB\n"
                f"LeetCode: https://leetcode.com/problems/{title_slug}/\n"
                f"Submitted: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(details.get('timestamp', 0) or sub.get('timestamp', 0)))}"
            )

            if args.dry_run:
                log(f"  [DRY RUN] Would commit to {file_path}")
                print(f"    Message: {message.split(chr(10))[0]}")
            else:
                commit_file(pat, file_path, code, message, existing_sha)
                log(f"  Committed to {file_path}", "SUCCESS")

            processed += 1

        except Exception as e:
            log(f"  Error: {e}", "ERROR")
            errors += 1

        time.sleep(0.3)

    log(f"\n{'='*40}")
    log(f"Done. Processed: {processed}, Skipped: {skipped}, Errors: {errors}")
    if args.dry_run:
        log("Dry run complete. Re-run without --dry-run to apply.", "INFO")


if __name__ == "__main__":
    main()