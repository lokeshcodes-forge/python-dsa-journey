USE college;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    branch VARCHAR(30),
    cgpa DECIMAL(3,2)
);

INSERT INTO students (id, name, branch, cgpa)
VALUES
(1, 'Shanmukh', 'CSE', 8.90),
(2, 'Rahul', 'ECE', 8.50),
(3, 'Priya', 'AI/ML', 9.20);

SELECT * FROM students;
