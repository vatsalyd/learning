-- DBMS Phase 1 SQL Practice
-- Topic: architecture, integrity, external views, and physical access paths
-- Dialect: SQLite-compatible SQL
-- Run this file as a script, then complete the YOUR TURN sections.

-- ================================================================
-- 1. Learn: the conceptual schema and integrity constraints
-- ================================================================

PRAGMA foreign_keys = ON;

DROP VIEW IF EXISTS public_employee_directory;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL CHECK (salary >= 0)
);

INSERT INTO employees (employee_id, name, salary)
VALUES
    ('E-17', 'Mira', 85000),
    ('E-18', 'Arun', 72000);

-- Observe the logical rows and columns exposed by the base table.
SELECT employee_id, name, salary
FROM employees
ORDER BY employee_id;

-- ================================================================
-- 2. Learn: external schemas through views
-- ================================================================

-- A directory application should not receive salary information.
-- The view is an external-level interface over the conceptual table.
CREATE VIEW public_employee_directory AS
SELECT employee_id, name
FROM employees;

SELECT employee_id, name
FROM public_employee_directory
ORDER BY employee_id;

-- YOUR TURN 1
-- Write a query against public_employee_directory that returns only
-- the employee named 'Mira'. Do not query the salary column.


-- ================================================================
-- 3. Learn: physical data independence through an index
-- ================================================================

-- Adding an index changes an internal access path, not the view contract.
CREATE INDEX employees_salary_idx
ON employees (salary);

-- The logical result is unchanged after the internal optimization.
SELECT employee_id, name
FROM public_employee_directory
ORDER BY employee_id;

-- SQLite can show the planner's chosen access strategy.
EXPLAIN QUERY PLAN
SELECT employee_id, name, salary
FROM employees
WHERE salary >= 80000;

-- ================================================================
-- 4. Learn: integrity is enforced by the database, not just the app
-- ================================================================

-- This statement must fail because salary violates CHECK (salary >= 0).
-- Uncomment it to observe the constraint error.
-- INSERT INTO employees (employee_id, name, salary)
-- VALUES ('E-19', 'Invalid Salary', -1);

-- This statement must fail because employee_id is a duplicate PRIMARY KEY.
-- Uncomment it to observe the entity-integrity error.
-- INSERT INTO employees (employee_id, name, salary)
-- VALUES ('E-17', 'Duplicate ID', 50000);

-- YOUR TURN 2
-- Write an INSERT for a valid employee of your choice.
-- It must contain a unique employee_id, a non-empty name, and
-- a non-negative integer salary. Then write a SELECT that verifies it.


-- ================================================================
-- 5. Learn: logical versus physical independence
-- ================================================================

-- Physical change: the index can be removed without changing the view.
-- Uncomment to test that the view still works after the access path changes.
-- DROP INDEX employees_salary_idx;
-- SELECT * FROM public_employee_directory ORDER BY employee_id;

-- YOUR TURN 3
-- Add a second external view named employee_names_only that exposes
-- exactly one column: name. Query the view ordered alphabetically.


-- ================================================================
-- 6. Exam self-check queries
-- ================================================================

-- What does the public application see?
SELECT * FROM public_employee_directory;

-- What does the base table contain that the public view hides?
SELECT employee_id, name, salary FROM employees;

-- Cleanup is intentionally omitted so you can inspect the database state.
-- In a temporary SQLite database, the objects disappear when the session ends.
