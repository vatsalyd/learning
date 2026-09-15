# CSL303 / MAL505: Database Management Systems
## Complete Mid-Semester Examination Master Roadmap & Study Guide (Lectures 1–12)

---

### Master Roadmap Sequence & Dependency Flow
This roadmap synthesizes all theoretical principles, algebraic foundations, SQL constructs, database programming interfaces, security mechanisms, and transaction semantics across **Lectures 1 through 12**.

$$\begin{matrix}
\textbf{Phase 1: Architecture \& Engine} & \longrightarrow & \textbf{Phase 2: Relational Model} & \longrightarrow & \textbf{Phase 3: Relational Algebra (I \& II)} \\
\downarrow & & & & \downarrow \\
\textbf{Phase 6: Aggregation \& Analytics} & \longleftarrow & \textbf{Phase 5: Joins \& Set Ops} & \longleftarrow & \textbf{Phase 4: DDL \& Single-Table SQL} \\
\downarrow & & & & \\
\textbf{Phase 7: Subqueries, CTEs \& 3VL} & \longrightarrow & \textbf{Phase 8: Window Functions} & \longrightarrow & \textbf{Phase 9: DML, DB-API \& Security} \\
& & & & \downarrow \\
& & & & \textbf{Phase 10: Transactions (ACID)}
\end{matrix}$$

---

## Phase 1: Database Fundamentals & Architecture (Lecture 1)
- [ ] **7 Flaws of Traditional File-Processing Systems**:
  - *Data Redundancy & Inconsistency*: Duplication of facts across departments leads to partial updates and divergent records.
  - *Difficulty in Accessing Data*: Ad-hoc analytical queries require writing custom file-parsing scripts from scratch.
  - *Data Isolation*: Data resides in disparate formats (CSV, binary, JSON); cross-file joins require custom glue code.
  - *Integrity Problems*: Business constraints are hardcoded into applications rather than centralized in the storage layer.
  - *Atomicity Failures*: System crashes during multi-step operations (e.g., bank transfers) cause permanent partial state corruption.
  - *Concurrent-Access Anomalies*: Uncontrolled concurrent execution results in anomalies such as *Lost Updates*.
  - *Security & Access Control*: Operating system file permissions are too coarse for granular column- and row-level access control.
- [ ] **DBMS Abstraction & Components**:
  - *Core Services*: Centralized data model, declarative querying, integrity checks, transactions, concurrency, recovery, security.
  - *Engine Pipeline*: Query Parser $\rightarrow$ Query Optimizer $\rightarrow$ Execution Engine $\leftrightarrow$ Access Methods (Heap, B+Tree) $\leftrightarrow$ Buffer Pool $\leftrightarrow$ Storage Manager & WAL.
- [ ] **Three-Schema Architecture & Data Independence**:
  - *Physical / Internal Level*: Low-level data layout (slotted pages, byte offsets, indexing structures).
  - *Conceptual / Logical Level*: Global structural entities, tables, relationships, and constraints.
  - *External / View Level*: Tailored slices, abstractions, and virtual tables for applications.
  - *Physical Data Independence*: Capacity to modify physical storage/indexes without rewriting logical schemas.
  - *Logical Data Independence*: Capacity to alter conceptual schemas without breaking external application views.
- [ ] **Workload Models**:
  - *OLTP (Online Transaction Processing)*: High-throughput, short concurrent transactions, row-oriented layout (e.g., PostgreSQL).
  - *OLAP (Online Analytical Processing)*: Complex aggregations over vast datasets, column-oriented layout (e.g., DuckDB).

---

## Phase 2: The Formal Relational Model (Lectures 2 & 3)
- [ ] **Formal Relational Concepts**:
  - *Origins*: Proposed by E. F. Codd (1970) to separate logical structure from physical machine representation.
  - *Mathematical Relation*: Subset of the Cartesian product of attribute domains: $R \subseteq D_1 \times D_2 \times \dots \times D_n$.
  - *Attributes & Atomic Domains*: Each column draws from an atomic domain $\text{dom}(A)$; First Normal Form (1NF) disallows non-atomic values.
  - *Relation Schema vs. Instance*: Schema $R(A_1: D_1, \dots, A_n: D_n)$ represents static intension; Instance $r(R)$ is the dynamic snapshot of tuples.
  - *Set vs. Bag Semantics*: Formal relations prohibit duplicate tuples and lack order; SQL tables implement multiset/bag semantics.
- [ ] **Key Taxonomy & Hierarchies**:
  - *Superkey*: Attribute set $K$ such that no two distinct tuples in any valid instance share identical values for $K$.
  - *Candidate Key*: A minimal superkey (removing any single attribute violates uniqueness).
  - *Primary Key*: The designated candidate key chosen by the schema designer; non-null, immutable, uniquely identifies tuples.
  - *Composite Key*: A primary key consisting of multiple attributes (e.g., `section(course_id, sec_id, semester, year)`).
  - *Foreign Key (FK)*: Attribute set in referencing relation matching the primary/candidate key of the referenced relation.
  - *Natural vs. Surrogate Keys*: Real-world identifiers (roll numbers) vs. synthetic system-generated auto-increments.
- [ ] **The Three Fundamental Integrity Constraints**:
  - *Domain Integrity*: Values must conform to attribute data types and defined `CHECK` expressions.
  - *Entity Integrity*: Primary key attributes can never be `NULL` (in whole or in part).
  - *Referential Integrity*: A foreign key must either match an existing primary key in the referenced relation or be entirely `NULL`.
- [ ] **Relationship-to-Table Mapping Recipes**:
  - *One-to-Many (1:N)*: Primary key of the "one" side placed as foreign key on the "many" side.
  - *Many-to-Many (M:N)*: Associative relation created with foreign keys referencing both participating relations + relationship attributes.
  - *Self-Referencing Relationships*: A relation referencing its own primary key (e.g., `prereq(course_id, prereq_id)`).

---

## Phase 3: Relational Algebra — Core, Extended & Translation (Lectures 3 & 4)
- [ ] **Closure Property**: Operators take relations as inputs and produce relations as outputs, enabling query trees.
- [ ] **Unary Operators**:
  - *Selection ($\sigma_p$)*: Horizontal row filter preserving tuples where predicate $p$ is true; degree invariant.
  - *Projection ($\pi_{A_1, \dots, A_k}$)*: Vertical column filter dropping unlisted attributes; eliminates duplicates.
  - *Rename ($\rho_{S(B_1, \dots, B_n)}(R)$ / $\rho_S(R)$)*: Renames relations and/or attributes to resolve naming conflicts in self-joins.
- [ ] **Set Operators & Union-Compatibility**:
  - *Preconditions*: Identical degree (number of columns) and pairwise domain compatibility.
  - *Union ($R \cup S$)*, *Intersection ($R \cap S$)*, *Set Difference ($R - S$)*.
- [ ] **The Join Family**:
  - *Cartesian Product ($R \times S$)*: Pairs every tuple in $R$ with every tuple in $S$; size $|R| \times |S|$.
  - *Theta Join ($R \bowtie_\theta S$)*: Filtered Cartesian product $\sigma_\theta(R \times S)$.
  - *Equijoin*: Theta join restricted exclusively to equality comparisons ($=$).
  - *Natural Join ($R \bowtie S$)*: Automatically equates identically-named attributes and eliminates duplicate columns (carries silent schema change risks).
  - *Outer Joins*: Left ($R \leftouterjoin S$), Right ($R \rightouterjoin S$), Full ($R \fullouterjoin S$) to preserve unmatched tuples padded with `NULL`.
  - *Semijoin ($R \ltimes S$)*: Returns tuples from $R$ that have matches in $S$ without row multiplication.
  - *Antijoin ($R \rhd S$)*: Returns tuples from $R$ that have no matches in $S$.
- [ ] **Relational Division ($R \div S$)**:
  - Answers "for all" universal quantification queries: finds tuples in $R$ associated with *all* tuples in $S$.
  - Derivation: $R \div S = \pi_a(R) - \pi_a((\pi_a(R) \times S) - R)$.
- [ ] **Extended Relational Algebra (Aggregation)**:
  - Aggregation Operator: $_{G_1, \dots, G_k}\mathcal{G}_{F_1(A_1), \dots, F_m(A_m)}(R)$.
  - Grouping attributes $G_i$ partition tuples; aggregate functions $F_j$ compute summary metrics.
- [ ] **Full RA $\longleftrightarrow$ SQL Translation Equivalences**:
  - $\sigma_p(R) \equiv$ `SELECT * FROM R WHERE p`
  - $\pi_A(R) \equiv$ `SELECT DISTINCT A FROM R`
  - $R \times S \equiv$ `SELECT * FROM R CROSS JOIN S`
  - $R \bowtie_\theta S \equiv$ `SELECT * FROM R JOIN S ON θ`
  - $R \bowtie S \equiv$ `SELECT * FROM R NATURAL JOIN S`
  - $R \leftouterjoin S \equiv$ `SELECT * FROM R LEFT JOIN S ON θ`
  - $R \div S \equiv$ SQL Double `NOT EXISTS` idiom.

---

## Phase 4: SQL DDL & Table Constraints (Lecture 5)
- [ ] **Sublanguages**: Data Definition (`DDL`), Data Manipulation (`DML`), Data Control (`DCL`), Transaction Control (`TCL`).
- [ ] **Type Systems**: Strict type validation (PostgreSQL) vs. Type Affinity (`INTEGER`, `REAL`, `TEXT`, `BLOB`, `NUMERIC` in SQLite).
- [ ] **Integrity Constraints**:
  - `NOT NULL`, `DEFAULT <value>`, `UNIQUE`, `PRIMARY KEY`, `CHECK (<condition>)`.
  - Column-level constraints vs. Table-level composite constraints.
- [ ] **Referential Integrity Actions**:
  - `ON DELETE` / `ON UPDATE`: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT` / `NO ACTION`.
  - SQLite foreign key enforcement prerequisite: `PRAGMA foreign_keys = ON;`.
- [ ] **Schema Lifecycle**:
  - `CREATE TABLE`, `ALTER TABLE` (adding/renaming columns and constraints).
  - Deletion mechanics: `DROP TABLE` (removes data + catalog schema) vs. `DELETE FROM` (removes tuples, logs, triggers) vs. `TRUNCATE` (fast deallocation of pages).

---

## Phase 5: Single-Table SQL & Joins (Lectures 6 & 6a)
- [ ] **Single-Table Querying**:
  - Projection list, Bag/Multiset duplicate retention vs. `SELECT DISTINCT`.
  - Filtering predicates: Comparison (`=`, `<>`, `<`, `<=`, `>`, `>=`), Range (`BETWEEN ... AND`), Membership (`IN`, `NOT IN`), Substring Pattern Matching (`LIKE` with `%`, `_`; `ILIKE`), NULL checking (`IS NULL`, `IS NOT NULL`).
  - Generalized projections: Arithmetic expressions, concatenation (`||`), Aliasing (`AS`).
  - Sorting & Pagination: `ORDER BY col [ASC|DESC] [NULLS FIRST|NULLS LAST]`, `LIMIT n OFFSET k`.
- [ ] **Logical Query Evaluation Order**:
  $$\mathbf{1.\; FROM} \longrightarrow \mathbf{2.\; WHERE} \longrightarrow \mathbf{3.\; SELECT} \longrightarrow \mathbf{4.\; DISTINCT} \longrightarrow \mathbf{5.\; ORDER\; BY} \longrightarrow \mathbf{6.\; LIMIT / OFFSET}$$
- [ ] **Multi-Table Joins**:
  - `INNER JOIN ... ON` vs. `JOIN ... USING (column)`.
  - Multi-table join chains; Join associativity and commutativity in optimizer planning.
  - Self-Joins: Relational table joined with itself using distinct aliases (eliminating self-pairs and duplicates via inequalities like `a.id < b.id`).
  - Non-equijoins (Theta joins over ranges and bands).
- [ ] **Outer Join Pitfalls**:
  - Anti-join pattern: `LEFT JOIN ... WHERE right.key IS NULL`.
  - Outer join filtering trap: Filtering the right table in `WHERE` strips NULL-padded rows and converts the query into an `INNER JOIN`; filters must reside in the `ON` clause.
- [ ] **Set Operations**:
  - `UNION`, `INTERSECT`, `EXCEPT` (duplicate eliminating) vs. `UNION ALL`, `INTERSECT ALL`, `EXCEPT ALL` (duplicate retaining, computationally faster).

---

## Phase 6: Aggregation & Grouping (Lecture 7)
- [ ] **Aggregate Functions & NULL Behavior**:
  - Core functions: `COUNT(*)`, `COUNT(col)`, `COUNT(DISTINCT col)`, `SUM(col)`, `AVG(col)`, `MIN(col)`, `MAX(col)`.
  - Golden Rule: All aggregate functions (except `COUNT(*)`) silently ignore `NULL` values.
  - Summing or averaging an empty partition or all-`NULL` column returns `NULL` (safeguard with `COALESCE(SUM(col), 0)`).
- [ ] **Group Partitioning**:
  - `GROUP BY`: Partitions input tuples into buckets; aggregates compute per bucket.
  - Cardinal Rule of `GROUP BY`: Every column in the `SELECT` list must either appear in the `GROUP BY` clause or be wrapped in an aggregate function.
  - Grouping by computed expressions, dates (`strftime`), or `CASE` expressions.
- [ ] **`WHERE` vs. `HAVING`**:
  - `WHERE`: Evaluated before grouping; filters rows; cannot contain aggregate functions.
  - `HAVING`: Evaluated after grouping; filters groups based on aggregate results.
- [ ] **Full 7-Step Logical Execution Pipeline**:
  $$\mathbf{1.\; FROM / JOIN} \rightarrow \mathbf{2.\; WHERE} \rightarrow \mathbf{3.\; GROUP\; BY} \rightarrow \mathbf{4.\; HAVING} \rightarrow \mathbf{5.\; SELECT} \rightarrow \mathbf{6.\; ORDER\; BY} \rightarrow \mathbf{7.\; LIMIT}$$
- [ ] **Advanced Aggregation**:
  - Join-induced row multiplication (double-counting aggregate quantities across 1:N joins).
  - `COUNT(right.id)` (yields `0` for empty left joins) vs. `COUNT(*)` (incorrectly yields `1`).
  - Multi-level grouping: `ROLLUP` (hierarchical subtotals + grand total), `GROUPING SETS`.
  - String concatenation aggregation: `STRING_AGG` (Postgres) / `GROUP_CONCAT` (SQLite).

---

## Phase 7: Subqueries, CTEs & Three-Valued Logic (Lectures 8, 9 & 9a)
- [ ] **Subquery Categorization**:
  - *Scalar Subqueries*: Return a single 1x1 value; permitted in `SELECT`, `WHERE`, `HAVING`.
  - *Set Comparisons*: `IN`, `NOT IN`, `> ANY` / `< ANY` (greater/less than minimum/maximum), `> ALL` / `< ALL` (greater/less than maximum/minimum).
  - *Derived Tables*: Inline subqueries in the `FROM` clause (mandatory table alias).
- [ ] **Correlated Subqueries & Relational Division**:
  - Inner query references outer query attribute; evaluated conceptually per outer tuple.
  - `EXISTS` and `NOT EXISTS`: Semijoins and antijoins that short-circuit upon finding the first match.
  - Double `NOT EXISTS` idiom: Translates universal quantification ($R \div S$, "customers who bought all products").
- [ ] **Common Table Expressions (CTEs)**:
  - `WITH ... AS`: Named temporary result sets improving readability and enabling linear chaining.
  - `WITH RECURSIVE`: Solves hierarchical and graph traversal queries (org charts, prerequisite paths); consists of Anchor Member $\cup$ Recursive Member; cycle defenses.
- [ ] **Three-Valued Logic (3VL) & NULLs**:
  - Truth states: `TRUE`, `FALSE`, `UNKNOWN`.
  - Truth tables: `UNKNOWN AND TRUE = UNKNOWN`, `UNKNOWN AND FALSE = FALSE`, `UNKNOWN OR TRUE = TRUE`, `NOT UNKNOWN = UNKNOWN`.
  - Row survival: A row is retained by `WHERE` if and only if the predicate evaluates strictly to `TRUE`.
  - The `NOT IN` NULL trap: `x NOT IN (..., NULL)` evaluates to `UNKNOWN`, returning **0 rows**. Solution: Replace with `NOT EXISTS`.
- [ ] **NULL Functions & Conditionals**:
  - `COALESCE(v1, v2, ...)`: Evaluates to first non-`NULL` argument.
  - `NULLIF(a, b)`: Returns `NULL` if $a=b$, otherwise $a$ (safeguards division by zero: `/ NULLIF(x, 0)`).
  - `CASE`: Simple vs. Searched `CASE`; conditional aggregation via `SUM(CASE WHEN ... THEN 1 ELSE 0 END)`.

---

## Phase 8: Analytical SQL — Window Functions (Lecture 9b)
- [ ] **The Window Concept**:
  - Aggregates collapse rows into a single summary; Window functions compute metrics across partitions while **preserving individual row identity**.
  - Syntax: `FUNCTION() OVER (PARTITION BY ... ORDER BY ... [FRAME])`.
- [ ] **Ranking Functions**:
  - `ROW_NUMBER()`: Unique sequential integers ($1, 2, 3, 4$).
  - `RANK()`: Tied values receive identical rank; leaves subsequent rank gaps ($1, 1, 3$).
  - `DENSE_RANK()`: Tied values receive identical rank; leaves no gaps ($1, 1, 2$).
  - `NTILE(n)`: Divides ordered partition into $n$ balanced buckets (quartiles, deciles).
- [ ] **Window Framing & Running Calculations**:
  - Frame specification: `ROWS BETWEEN <start> AND <end>`.
  - Frame boundaries: `UNBOUNDED PRECEDING`, `n PRECEDING`, `CURRENT ROW`, `n FOLLOWING`, `UNBOUNDED FOLLOWING`.
  - Running totals: `SUM(x) OVER (ORDER BY d ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`.
  - Moving averages: `AVG(x) OVER (ORDER BY d ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)`.
- [ ] **Positional & Value Functions**:
  - `LAG(col, offset)` / `LEAD(col, offset)`: Accesses preceding/succeeding row values (period-over-period comparisons).
  - `FIRST_VALUE(col)` / `LAST_VALUE(col)`: Inspects partition boundary values.
- [ ] **Distribution & Boolean Aggregates**:
  - `CUME_DIST()` (cumulative relative position) and `PERCENT_RANK()`.
  - PostgreSQL boolean aggregations: `bool_or` (any true), `bool_and` (all true).
- [ ] **The Top-N Per Group Pattern**:
  - Computing ranks in a CTE or subquery, then filtering by `WHERE rn <= N` in the outer query (window functions cannot be filtered directly in `WHERE`).

---

## Phase 9: Views, Security, DML & Application DB-API (Lectures 10 & 11)
- [ ] **Views & Materialization**:
  - *Standard Views*: Virtual queries; recomputed dynamically upon each invocation; drops catalog definition without affecting base tables.
  - *Updatable Views*: Direct single-table views without aggregations, `GROUP BY`, `DISTINCT`, or joins; `WITH CHECK OPTION` prevents rows from silently escaping the view upon insertion/update.
  - *Materialized Views*: Precomputed results persisted to disk for fast analytical queries; managed via `REFRESH MATERIALIZED VIEW [CONCURRENTLY]`.
  - *Complex View Updates*: Handled via `INSTEAD OF` triggers.
- [ ] **Stored Functions & Access Control**:
  - Functions (return values, usable in SQL expressions) vs. Procedures (`CALL`, manage transactions).
  - Security contexts: `SECURITY INVOKER` (caller privileges) vs. `SECURITY DEFINER` (runs with owner privileges for controlled access).
  - Role-Based Access Control (RBAC): `CREATE ROLE`, `GRANT privilege ON object TO role`, `REVOKE privilege ON object FROM role`, `WITH GRANT OPTION`.
  - Security abstractions: Exposing restricted views + PostgreSQL Row-Level Security (`RLS`).
- [ ] **DML Mutations & Triggers**:
  - `INSERT` (multi-row, `INSERT ... SELECT`), `UPDATE` (with joins via `UPDATE ... FROM`), `DELETE`.
  - Upsert patterns: `ON CONFLICT (key) DO UPDATE SET ...` / `DO NOTHING`.
  - `RETURNING` clause: Returns modified tuples without issuing subsequent `SELECT` queries.
  - Triggers: Timing (`BEFORE`, `AFTER`, `INSTEAD OF`), Events (`INSERT`, `UPDATE`, `DELETE`), Transition variables (`OLD`, `NEW`).
- [ ] **Python DB-API (PEP 249) & Security**:
  - Lifecycle: `connect()` $\rightarrow$ `cursor()` $\rightarrow$ `execute()` / `executemany()` $\rightarrow$ `fetchone()` / `fetchall()` / `fetchmany()` $\rightarrow$ `commit()` $\rightarrow$ `close()`.
  - SQL Injection: Dynamic string concatenation allows malicious input to alter query syntax.
  - Parameterized Queries: Placeholders (`?` in SQLite, `%s` in psycopg) pass data separately from SQL AST; placeholders cannot be used for identifiers (table/column names).

---

## Phase 10: Transactions — ACID & Concurrency from the User's View (Lecture 12)
- [ ] **Transaction Concept & ACID Guarantees**:
  - *Transaction*: A sequence of operations executed as a single, atomic logical unit of work.
  - *Atomicity (All-or-Nothing)*: All operations commit successfully, or all changes are rolled back.
  - *Consistency*: A transaction transitions the database from one valid state to another, preserving all declared schema constraints and business invariants.
  - *Isolation*: Concurrent transactions execute without mutual interference; intermediate uncommitted states remain invisible.
  - *Durability*: Once committed, modifications survive crashes, power outages, and system restarts (enforced by WAL `fsync`).
- [ ] **Transaction Control Statements**:
  - `BEGIN` / `START TRANSACTION`: Opens a transaction boundary.
  - `COMMIT`: Persists changes permanently to disk.
  - `ROLLBACK`: Reverts all modifications made since `BEGIN`.
  - `SAVEPOINT name` & `ROLLBACK TO name`: Partial rollback points within an open transaction.
  - *Autocommit Danger*: Default environment where each statement commits immediately; breaks atomicity across multi-step business operations unless wrapped in explicit transactions.
- [ ] **The 3 Concurrency Read Anomalies**:
  - *Dirty Read*: $T_1$ updates a row without committing; $T_2$ reads the uncommitted value; $T_1$ aborts and rolls back.
  - *Non-Repeatable Read*: $T_2$ reads a row; $T_1$ modifies and commits that row; $T_2$ re-reads the row and observes divergent data.
  - *Phantom Read*: $T_2$ queries a range of rows; $T_1$ inserts/deletes rows satisfying the predicate and commits; $T_2$ re-executes the query and observes a different set of rows.
- [ ] **SQL Standard Isolation Levels**:
  | Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
  | :--- | :---: | :---: | :---: |
  | **Read Uncommitted** | Permitted | Permitted | Permitted |
  | **Read Committed** *(PostgreSQL Default)* | Prevented | Permitted | Permitted |
  | **Repeatable Read** | Prevented | Prevented | Permitted *(Prevented in PG Snapshot Isolation)* |
  | **Serializable** | Prevented | Prevented | Prevented |
- [ ] **Transaction Execution Architectures**:
  - *Pessimistic Concurrency*: Explicit two-phase locking (`2PL`); transactions wait on lock conflicts.
  - *Optimistic Concurrency (SSI / MVCC)*: Transactions proceed without lock contention; checked at commit time; conflicting transactions abort and require application-level retry loops.
  - *Deadlocks*: Circular wait dependencies between concurrent transactions; DBMS selects and aborts a victim transaction.
  - *Read-Only Transactions*: `BEGIN TRANSACTION READ ONLY` provides a stable point-in-time snapshot.

---

## High-Yield Mid-Sem Pitfall & Exam Trap Matrix

| Concept / Phenomenon | Common Examination Mistake | Correct Mechanical Behavior |
| :--- | :--- | :--- |
| **`WHERE` vs. `HAVING`** | Including aggregate functions (`COUNT(*) > 2`) inside `WHERE` | `WHERE` filters tuples before grouping; `HAVING` filters aggregated buckets after grouping. |
| **Logical Order vs. Aliases** | Referencing column aliases created in `SELECT` within `WHERE` or `GROUP BY` | `WHERE` and `GROUP BY` execute before `SELECT`; the alias is not yet bound. |
| **`COUNT(*)` vs. `COUNT(col)`** | Assuming both return the exact same count | `COUNT(*)` counts total rows; `COUNT(col)` strictly counts rows where `col IS NOT NULL`. |
| **Outer Join `WHERE` Trap** | Placing filtering conditions on the right table in `WHERE` | Strips NULL-padded rows, silently converting a `LEFT JOIN` into an `INNER JOIN`. Condition belongs in `ON`. |
| **The `NOT IN` NULL Trap** | Executing `WHERE id NOT IN (SELECT id FROM ...)` where subquery has `NULL` | In 3VL, `NOT IN (..., NULL)` evaluates to `UNKNOWN`, returning **0 rows**. Use `NOT EXISTS`. |
| **Natural Join Hazards** | Using `NATURAL JOIN` in production code | Silently joins on all shared attribute names; adding an unrelated column with matching name breaks the query. |
| **Aggregating over 1:N Joins** | Summing parent columns after joining a child table | Duplicates parent values across child rows, resulting in inflated aggregate sums. |
| **Window Functions in `WHERE`** | Writing `WHERE ROW_NUMBER() OVER (...) = 1` | Window functions evaluate after `WHERE`. Ranking must be computed in a CTE/subquery first. |
| **`RANK` vs. `DENSE_RANK`** | Treating rank tie distributions as identical | `RANK()` produces gaps ($1, 1, 3$); `DENSE_RANK()` produces no gaps ($1, 1, 2$). |
| **Disappearing View Rows** | Inserting rows into a view that do not satisfy the view's `WHERE` filter | Row is inserted into base table but disappears from view. Prevent using `WITH CHECK OPTION`. |
| **Autocommit Failures** | Relying on autocommit during multi-statement operations | Crash between updates leaves partial state permanently committed, breaking Atomicity. |
| **Uncommitted DB-API Writes** | Executing DML in Python and closing connection without `conn.commit()` | Driver issues an automatic rollback; modified rows are discarded permanently. |
| **SQL Injection Vulnerability** | Using Python f-strings or string concatenation to build queries | User payload alters query AST. Must use parameterized placeholders (`?` or `%s`). |

---

## Complete Rapid Revision Drill Checklist (By Week)

```
[ ] Week 1: DBMS Architecture & Relational Model (Lec 1-3)
    ├── 1. Explain the 7 file-processing flaws and how DBMS architecture solves each.
    ├── 2. Contrast Logical vs Physical Data Independence.
    ├── 3. Define Superkeys, Candidate Keys, and Primary Keys with minimality proofs.
    └── 4. Enforce Domain, Entity, and Referential Integrity with referential actions.

[ ] Week 2: Relational Algebra (Lec 3-4)
    ├── 5. Compose complex queries using σ, π, ρ, and query trees.
    ├── 6. Verify Union-Compatibility for Set Difference and Intersection.
    ├── 7. Derive Relational Division (R ÷ S) from fundamental operators.
    └── 8. Translate queries bidirectionally between Extended RA (G) and SQL.

[ ] Week 3: DDL, Joins & Aggregation (Lec 5-7)
    ├── 9. Differentiate type enforcement between PostgreSQL and SQLite.
    ├── 10. Trace the 7-step logical query execution pipeline.
    ├── 11. Implement Self-Joins and Theta Joins without duplicate pairing.
    ├── 12. Distinguish INNER, LEFT, RIGHT, and FULL joins and master the Anti-Join idiom.
    └── 13. Apply the Cardinal Rule of GROUP BY and formulate HAVING conditions.

[ ] Week 4: Subqueries, CTEs, 3VL & Window Functions (Lec 8-9b)
    ├── 14. Formulate Universal Quantification using the Double NOT EXISTS idiom.
    ├── 15. Write Recursive CTEs (WITH RECURSIVE) for hierarchies and cyclic graphs.
    ├── 16. Evaluate 3VL truth tables and explain why NOT IN fails with NULLs.
    ├── 17. Implement Top-N per group using ROW_NUMBER() / DENSE_RANK() in a CTE.
    └── 18. Construct running totals and moving averages using window frame clauses.

[ ] Week 5: Views, Security, DML & Transactions (Lec 10-12)
    ├── 19. Define Updatable Views and protect row retention with WITH CHECK OPTION.
    ├── 20. Implement RBAC using roles, GRANT/REVOKE, and SECURITY DEFINER functions.
    ├── 21. Write Upsert statements using ON CONFLICT DO UPDATE and handle RETURNING.
    ├── 22. Prevent SQL Injection using Python DB-API parameterized queries.
    ├── 23. Define the ACID properties and trace transaction rollback to SAVEPOINT.
    └── 24. Map Concurrency Anomalies (Dirty, Non-repeatable, Phantom) across the 4 Isolation Levels.
```
