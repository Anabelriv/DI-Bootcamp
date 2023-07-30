-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = anabelrivera
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE students(
-- 	id smallint PRIMARY KEY,
-- 	last_name VARCHAR (50) NOT NULL,
--  	first_name VARCHAR (100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )
-- SET DateStyle TO DMY;
-- INSERT INTO students (id, first_name, last_name, birth_date)
-- VALUES(1,'Marc','Benichou',	'02/11/1998'),
-- (2,'Yoan','Cohen','03/12/2010'),
-- (3,'Lea','Benichou','27/07/1987'),
-- (4,'Amelia','Dux','07/04/1996'),
-- (5,'David','Grez','14/06/2003'),
-- (6,'Omer','Simpson','03/10/1980');

-- INSERT INTO students (id, first_name, last_name, birth_date)
-- VALUES(7,'Anabel','Rivera','23/03/1991')

-- SELECT * FROM students;

-- SELECT first_name, last_name FROM students;

-- SELECT first_name, last_name FROM students WHERE id = 2;

-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'A%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '_%a%';

-- SELECT first_name, last_name FROM students WHERE id IN (1,3);

-- SELECT * from students WHERE birth_Date >= '1/01/2000';
