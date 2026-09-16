-- DBMS Phase 2 SQL Practice
-- Topic: relational schemas, keys, integrity, and relationship mapping
-- Dialect: SQLite-compatible SQL
-- Run this file directly in a SQLite client.

PRAGMA foreign_keys = ON;

-- ================================================================
-- 1. Learn: relation schemas and domains
-- ================================================================

DROP TABLE IF EXISTS prerequisite;
DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS department;

-- A domain is represented here through SQL types plus CHECK predicates.
CREATE TABLE department (
    department_id TEXT PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE
);

CREATE TABLE student (
    student_id TEXT PRIMARY KEY,
    student_name TEXT NOT NULL,
    department_id TEXT NOT NULL,
    FOREIGN KEY (department_id)
        REFERENCES department(department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE course (
    course_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    credits INTEGER NOT NULL CHECK (credits BETWEEN 1 AND 6)
);

-- ================================================================
-- 2. Learn: M:N relationship through an associative relation
-- ================================================================

-- Students can take many courses; courses can have many students.
-- The composite primary key prevents the same student/course enrollment
-- from being inserted twice for the same offering.
CREATE TABLE enrollment (
    student_id TEXT NOT NULL,
    course_id TEXT NOT NULL,
    semester TEXT NOT NULL CHECK (semester IN ('Spring', 'Summer', 'Fall')),
    year INTEGER NOT NULL CHECK (year >= 2000),
    grade TEXT,
    PRIMARY KEY (student_id, course_id, semester, year),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

-- ================================================================
-- 3. Learn: self-referencing relationship
-- ================================================================

-- Both columns reference course.course_id. A course may require another
-- course, and the same table plays both the parent and child role.
CREATE TABLE prerequisite (
    course_id TEXT NOT NULL,
    prerequisite_id TEXT NOT NULL,
    PRIMARY KEY (course_id, prerequisite_id),
    CHECK (course_id <> prerequisite_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
    FOREIGN KEY (prerequisite_id) REFERENCES course(course_id) ON DELETE RESTRICT
);

-- ================================================================
-- 4. Populate a relation instance
-- ================================================================

INSERT INTO department (department_id, department_name)
VALUES ('CS', 'Computer Science'), ('MATH', 'Mathematics');

INSERT INTO student (student_id, student_name, department_id)
VALUES
    ('S1', 'Mira', 'CS'),
    ('S2', 'Arun', 'CS'),
    ('S3', 'Leena', 'MATH');

INSERT INTO course (course_id, title, credits)
VALUES
    ('CS101', 'Database Systems', 4),
    ('CS201', 'Operating Systems', 4),
    ('CS301', 'Distributed Systems', 3),
    ('MA101', 'Discrete Mathematics', 4);

INSERT INTO enrollment (student_id, course_id, semester, year, grade)
VALUES
    ('S1', 'CS101', 'Fall', 2026, 'A'),
    ('S1', 'CS201', 'Fall', 2026, NULL),
    ('S2', 'CS101', 'Fall', 2026, 'B');

INSERT INTO prerequisite (course_id, prerequisite_id)
VALUES
    ('CS201', 'CS101'),
    ('CS301', 'CS201');

-- Observe schema-level degree and instance rows.
SELECT * FROM student ORDER BY student_id;
SELECT * FROM enrollment ORDER BY student_id, course_id;
SELECT * FROM prerequisite ORDER BY course_id;

-- ================================================================
-- 5. Learn: key and integrity failures
-- ================================================================

-- Each statement below is intentionally commented out. Uncomment one at a
-- time to observe the database rejecting a domain/entity/referential error.

-- Domain integrity: credits must be between 1 and 6.
-- INSERT INTO course(course_id, title, credits)
-- VALUES ('BAD1', 'Invalid Credits', 0);

-- Entity integrity: student_id is a non-null primary key.
-- INSERT INTO student(student_id, student_name, department_id)
-- VALUES (NULL, 'No ID', 'CS');

-- Referential integrity: department_id must exist.
-- INSERT INTO student(student_id, student_name, department_id)
-- VALUES ('S9', 'Unknown Department', 'NO_SUCH_DEPT');

-- Composite-key uniqueness: the exact offering cannot be enrolled twice.
-- INSERT INTO enrollment(student_id, course_id, semester, year)
-- VALUES ('S1', 'CS101', 'Fall', 2026);

-- Self-reference rule: a course cannot be its own prerequisite.
-- INSERT INTO prerequisite(course_id, prerequisite_id)
-- VALUES ('CS101', 'CS101');

-- ================================================================
-- 6. YOUR TURN — direct SQL practice
-- ================================================================

-- YOUR TURN 1: Insert a new student in an existing department, then verify
-- the row with a SELECT query.


-- YOUR TURN 2: Insert one valid enrollment for that student. Use an existing
-- course, a valid semester, and a year >= 2000.


-- YOUR TURN 3: Write a query that lists each student_id and the courses they
-- take. Do not use NATURAL JOIN; write explicit JOIN conditions.


-- YOUR TURN 4: Write a query that lists each course title and its prerequisite
-- course title. You will need two aliases for the course relation.


-- YOUR TURN 5: Explain in a SQL comment why enrollment uses a composite key
-- instead of student_id alone or course_id alone.


-- ================================================================
-- 7. Set/bag observation
-- ================================================================

-- SQL projection can retain duplicate department IDs under bag semantics.
SELECT department_id FROM student;

-- DISTINCT gives the formal-set-style unique projection.
SELECT DISTINCT department_id FROM student;

