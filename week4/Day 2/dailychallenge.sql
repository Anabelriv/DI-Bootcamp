-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

---> I created a new table that has 2 columns, 1 for numbers and 1 for text with a limit of char of 10

-- INSERT INTO firstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

---> I added data and one has no id 

-- SELECT * FROM firstTab
---> I am getting all the table's data
-- CREATE TABLE SecondTab (
-- 	id integer 
-- )
---> I created a new table with only one row, id 

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)

---> I added data in my second table

-- SELECT * FROM SecondTab

---> I printed everything from my second table
--- QUESTIONS:

-- SELECT COUNT(*) 
-- FROM firsttab AS ft WHERE ft.id NOT IN ( SELECT id FROM secondtab WHERE id IS NULL )

--->Result is 0, I am having the result of how many rows there are from my first table with a condition where there won't be the first table id not in the secondtable where the id is NULL

-- SELECT COUNT(*) 
-- FROM firsttab AS ft WHERE ft.id NOT IN ( SELECT id FROM secondtab WHERE id = 5 )
---> Result is 2, I am counting the columns from firsttable where the ft id not in second table that has id 5

-- SELECT COUNT(*) 
-- FROM firsttab AS ft WHERE ft.id NOT IN ( SELECT id FROM secondtab )
---> Result is 0 counting columns, from the first table where the id is not in the id from the secondtable

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

---> Result is 2 counting columns with the condition similar to before but that id is not null




