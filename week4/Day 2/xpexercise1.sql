-- Table: public.items

-- DROP TABLE IF EXISTS public.items;

-- CREATE TABLE IF NOT EXISTS public.items
-- (
--     "number" smallint,
--     name text COLLATE pg_catalog."default",
--     price money
-- )

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- SELECT * from items
-- ORDER by price
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- SELECT * from items
-- WHERE price > '80'
-- ORDER by price DESC;

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- SELECT first_name, last_name
-- FROM customers
-- ORDER BY first_name
-- LIMIT 3;
-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- SELECT last_name 
-- FROM customers
-- ORDER BY last_name DESC;

