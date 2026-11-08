USE college;

SELECT * FROM students;

SELECT * FROM students
WHERE branch = 'CSE';

SELECT * FROM students
WHERE cgpa > 8.5;

SELECT * FROM students
WHERE cgpa >= 9.0;

SELECT * FROM students
WHERE branch != 'ECE';

SELECT * FROM students
WHERE branch = 'CSE'
AND cgpa > 8.5;

SELECT * FROM students
WHERE branch = 'CSE'
OR branch = 'AIML';

SELECT * FROM students
WHERE branch IS NULL;

SELECT * FROM students
WHERE branch IS NOT NULL;