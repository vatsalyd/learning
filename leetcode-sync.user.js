// ==UserScript==
// @name         LeetCode → GitHub Auto Sync
// @namespace    https://github.com/vatsalyd/learning
// @version      1.0.0
// @description  Auto-commit accepted LeetCode solutions to GitHub repo organized by difficulty
// @author       vatsalyd
// @match        https://leetcode.com/problems/*
// @match        https://leetcode.com/submissions/*
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_xmlhttpRequest
// @grant        GM_notification
// @grant        GM_log
// @connect      leetcode.com
// @connect      api.github.com
// @connect      raw.githubusercontent.com
// ==/UserScript==

(function () {
  "use strict";

  const CONFIG = {
    repoOwner: "vatsalyd",
    repoName: "learning",
    githubApiBase: "https://api.github.com",
    leetcodeGraphql: "https://leetcode.com/graphql",
    patKey: "LEETCODE_GH_PAT",
    patCreatedKey: "LEETCODE_GH_PAT_CREATED",
    patRotationDays: 90,
    difficultyMap: {
      1: "easy",
      2: "medium",
      3: "hard"
    },
    normalizeDifficulty(difficulty) {
      if (typeof difficulty === "number" && [1, 2, 3].includes(difficulty)) {
        return difficulty;
      }
      if (typeof difficulty === "string") {
        const d = difficulty.trim().toLowerCase();
        if (d === "easy") return 1;
        if (d === "medium") return 2;
        if (d === "hard") return 3;
      }
      return 1;
    },
    langExt: {
      python3: "py",
      python: "py",
      java: "java",
      cpp: "cpp",
      c: "c",
      csharp: "cs",
      javascript: "js",
      typescript: "ts",
      go: "go",
      rust: "rs",
      ruby: "rb",
      swift: "swift",
      kotlin: "kt",
      php: "php",
      scala: "scala",
      r: "r",
      dart: "dart",
      elixir: "ex",
      erlang: "erl",
      racket: "rkt"
    }
  };

  let isProcessing = false;

  function log(...args) {
    GM_log("[LeetCode Sync] " + args.join(" "));
    console.log("[LeetCode Sync]", ...args);
  }

  function getPat() {
    return GM_getValue(CONFIG.patKey, "");
  }

  function setPat(pat) {
    GM_setValue(CONFIG.patKey, pat);
    GM_setValue(CONFIG.patCreatedKey, Date.now().toString());
  }

  function checkPatRotation() {
    const created = parseInt(GM_getValue(CONFIG.patCreatedKey, "0"), 10);
    if (!created) return;
    const daysSince = (Date.now() - created) / (1000 * 60 * 60 * 24);
    if (daysSince > CONFIG.patRotationDays) {
      showNotification("⚠️ PAT Rotation Recommended", `Your GitHub PAT is ${Math.floor(daysSince)} days old. Consider rotating it for security.`, "warning");
    }
  }

  function showNotification(title, text, type = "info") {
    if (typeof GM_notification !== "undefined") {
      GM_notification({ title, text, timeout: 5000, type });
    } else {
      const n = document.createElement("div");
      n.style.cssText = `
        position: fixed; top: 20px; right: 20px; z-index: 999999;
        padding: 16px 24px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        background: ${type === "error" ? "#fee" : type === "warning" ? "#ffd" : "#dff"};
        border: 1px solid ${type === "error" ? "#fcc" : type === "warning" ? "#fc0" : "#8c8"};
        color: #333; font-family: system-ui, sans-serif; font-size: 14px;
        max-width: 350px; animation: slideIn 0.3s ease;
      `;
      n.innerHTML = `<strong>${title}</strong><br>${text}`;
      document.body.appendChild(n);
      setTimeout(() => n.remove(), 5000);
    }
  }

  function githubRequest(method, path, body = null) {
    const pat = getPat();
    if (!pat) throw new Error("GitHub PAT not configured. Set it in Tampermonkey script settings.");

    return new Promise((resolve, reject) => {
      GM_xmlhttpRequest({
        method,
        url: CONFIG.githubApiBase + path,
        headers: {
          "Authorization": `Bearer ${pat}`,
          "Accept": "application/vnd.github+json",
          "Content-Type": "application/json",
          "User-Agent": "LeetCode-Sync-Userscript/1.0"
        },
        data: body ? JSON.stringify(body) : undefined,
        onload: (res) => {
          if (res.status >= 200 && res.status < 300) {
            try { resolve(JSON.parse(res.responseText)); } catch { resolve(res.responseText); }
          } else {
            let msg = `GitHub API ${res.status}`;
            try { msg += ": " + JSON.parse(res.responseText).message; } catch { msg += ": " + res.responseText; }
            reject(new Error(msg));
          }
        },
        onerror: (err) => reject(new Error("Network error: " + err)),
        ontimeout: () => reject(new Error("Request timeout"))
      });
    });
  }

  function leetcodeGraphql(query, variables) {
    return new Promise((resolve, reject) => {
      GM_xmlhttpRequest({
        method: "POST",
        url: CONFIG.leetcodeGraphql,
        headers: {
          "Content-Type": "application/json",
          "Referer": "https://leetcode.com/",
          "Origin": "https://leetcode.com"
        },
        data: JSON.stringify({ query, variables }),
        credentials: "include",
        onload: (res) => {
          try {
            const data = JSON.parse(res.responseText);
            if (data.errors) reject(new Error(data.errors.map(e => e.message).join(", ")));
            else resolve(data.data);
          } catch (e) { reject(new Error("Invalid GraphQL response")); }
        },
        onerror: (err) => reject(new Error("GraphQL network error: " + err)),
        ontimeout: () => reject(new Error("GraphQL timeout"))
      });
    });
  }

  async function getSubmissionDetails(submissionId) {
    const query = `
      query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
          code
          lang { name }
          runtime
          memory
          statusDisplay
          timestamp
          question {
            titleSlug
            title
            difficulty
            questionId
          }
        }
      }
    `;
    const data = await leetcodeGraphql(query, { submissionId });
    return (data && data.submissionDetails) || {};
  }

  async function getLatestAcceptedSubmission(titleSlug) {
    const query = `
      query recentAcSubmissions($titleSlug: String!) {
        recentAcSubmissionList(titleSlug: $titleSlug, limit: 1) {
          id
          code
          lang
          runtime
          memory
          statusDisplay
          timestamp
        }
      }
    `;
    const data = await leetcodeGraphql(query, { titleSlug });
    const list = data.recentAcSubmissionList;
    return list.length > 0 ? list[0] : null;
  }

  function getFilePath(difficulty, titleSlug, lang) {
    const ext = CONFIG.langExt[lang] || lang || "txt";
    const diffFolder = CONFIG.difficultyMap[difficulty] || "unknown";
    return `leetcode/${diffFolder}/${titleSlug}.${ext}`;
  }

  async function fileExistsOnGitHub(path) {
    try {
      await githubRequest("GET", `/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/contents/${encodeURIComponent(path)}`);
      return true;
    } catch (e) {
      if (e.message.includes("404")) return false;
      throw e;
    }
  }

  async function getFileSha(path) {
    try {
      const data = await githubRequest("GET", `/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/contents/${encodeURIComponent(path)}`);
      return data.sha;
    } catch {
      return null;
    }
  }

  async function commitFile(path, content, message, sha = null) {
    const body = {
      message,
      content: btoa(unescape(encodeURIComponent(content))),
      branch: "main"
    };
    if (sha) body.sha = sha;
    return githubRequest("PUT", `/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/contents/${encodeURIComponent(path)}`, body);
  }

  function hashCode(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) - hash) + str.charCodeAt(i);
      hash |= 0;
    }
    return hash.toString(16);
  }

  async function processAcceptedSubmission(submission) {
    if (isProcessing) return;
    isProcessing = true;

    try {
      const { code, lang, runtime, memory, statusDisplay, timestamp, question } = submission;
      if (!question) throw new Error("No question info in submission");

      const langName = (lang && lang.name) ? lang.name : lang;
      const { titleSlug, title, difficulty, questionId } = question;
      const normDiff = CONFIG.normalizeDifficulty(difficulty);
      const diffLabel = CONFIG.difficultyMap[normDiff] || "unknown";
      const filePath = getFilePath(normDiff, titleSlug, langName);

      log(`Processing: ${title} (${diffLabel}) - ${langName}`);

      const existingSha = await getFileSha(filePath);
      if (existingSha) {
        const existingContent = await githubRequest("GET", `/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/contents/${encodeURIComponent(filePath)}`);
        const existingCode = atob(existingContent.content.replace(/\n/g, ""));
        if (hashCode(existingCode) === hashCode(code)) {
          log("Identical solution already committed, skipping");
          showNotification("LeetCode Sync", `⏭️ Skipped: ${title} (already synced)`);
          return;
        }
      }

      const message = `feat(leetcode): add ${title} (${diffLabel}) [${questionId}]\n\nLanguage: ${langName}\nRuntime: ${runtime}ms\nMemory: ${memory}MB\nLeetCode: https://leetcode.com/problems/${titleSlug}/`;
      
      await commitFile(filePath, code, message, existingSha);

      log(`Committed: ${filePath}`);
      showNotification("✅ LeetCode Synced", `Committed ${title} (${diffLabel}) to GitHub`, "success");

    } catch (err) {
      log("Error:", err.message);
      showNotification("❌ LeetCode Sync Failed", err.message, "error");
    } finally {
      isProcessing = false;
    }
  }

  function extractSubmissionIdFromUrl() {
    const match = window.location.pathname.match(/\/submissions\/(\d+)/);
    return match ? parseInt(match[1], 10) : null;
  }

  function extractTitleSlugFromUrl() {
    const match = window.location.pathname.match(/\/problems\/([^\/]+)/);
    return match ? match[1] : null;
  }

  async function handleSubmissionPage() {
    const submissionId = extractSubmissionIdFromUrl();
    if (!submissionId) return;

    log(`Submission page detected: ${submissionId}`);
    try {
      const details = await getSubmissionDetails(submissionId);
      if (details && details.statusDisplay === "Accepted") {
        await processAcceptedSubmission(details);
      }
    } catch (err) {
      log("Failed to fetch submission details:", err.message);
    }
  }

  async function handleProblemPage() {
    const titleSlug = extractTitleSlugFromUrl();
    if (!titleSlug) return;

    const observer = new MutationObserver(async (mutations) => {
      for (const m of mutations) {
        if (m.type === "childList") {
          const acceptedToast = document.querySelector('[data-cy="submission-result-accepted"], .css-1x5n938, .success__3Ai1');
          if (acceptedToast && !isProcessing) {
            log("Accepted toast detected via DOM");
            try {
              const submission = await getLatestAcceptedSubmission(titleSlug);
              if (submission) {
                submission.question = { titleSlug, title: document.title.split(" - ")[0].trim(), difficulty: null };
                await processAcceptedSubmission(submission);
              }
            } catch (err) {
              log("DOM fallback failed:", err.message);
            }
            break;
          }
        }
      }
    });

    observer.observe(document.body, { childList: true, subtree: true });

    setTimeout(() => observer.disconnect(), 30000);
  }

  async function init() {
    checkPatRotation();

    const pat = getPat();
    if (!pat) {
      const input = prompt("LeetCode Sync: Enter your GitHub PAT (fine-grained, repo contents write):");
      if (input) setPat(input.trim());
      else { showNotification("LeetCode Sync", "PAT required for sync to work", "warning"); return; }
    }

    if (window.location.pathname.includes("/submissions/")) {
      await handleSubmissionPage();
    } else if (window.location.pathname.includes("/problems/")) {
      await handleProblemPage();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.LeetCodeSync = {
    setPat,
    getPat,
    syncNow: async (titleSlug) => {
      const submission = await getLatestAcceptedSubmission(titleSlug);
      if (submission) await processAcceptedSubmission({ ...submission, question: { titleSlug, title: titleSlug, difficulty: 1, questionId: submission.questionId || titleSlug } });
    }
  };
})();