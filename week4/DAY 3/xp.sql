-- -- Get a list of all the languages, from the language table.
-- -- SELECT name from language;
-- -- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
-- -- SELECT film.title, film.description, language.name as language
-- -- FROM film 
-- -- JOIN language ON film.language_ID = language.language_id;
-- -- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
-- -- SELECT film.title, film.description, language.name as language
-- -- FROM language 
-- -- LEFT JOIN film ON film.language_ID = language.language_id;

-- -- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- -- CREATE table new_film (
-- -- id SERIAL PRIMARY KEY,
-- -- 	name VARCHAR(255)
-- -- );
-- -- INSERT INTO new_film (name)
-- -- VALUES
-- --     ('Home Alone'),
-- --     ('Openheimer'),
-- --     ('Harry Potter');
-- -- Create a new table called customer_review, which will contain film reviews that customers will make.
-- -- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- -- It should have the following columns:
-- -- review_id – a primary key, non null, auto-increment.
-- -- film_id – references the new_film table. The film that is being reviewed.
-- -- language_id – references the language table. What language the review is in.
-- -- title – the title of the review.
-- -- score – the rating of the review (1-10).
-- -- review_text – the text of the review. No limit on the length.
-- -- last_update – when the review was last updated.

-- -- CREATE TABLE reviews (
-- --     review_id SERIAL PRIMARY KEY,
-- --     film_id INT NOT NULL,
-- --     language_id INT NOT NULL,
-- --     title VARCHAR(255),
-- --     score INT CHECK (score >= 1 AND score <= 10),
-- --     review_text TEXT,
-- --     last_update TIMESTAMP,
-- --     FOREIGN KEY (film_id) REFERENCES new_film (id) ON DELETE CASCADE,
-- --     FOREIGN KEY (language_id) REFERENCES language (language_id)
-- -- );


-- -- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- -- Inserting the first review
-- -- INSERT INTO reviews (film_id, language_id, title, score, review_text, last_update)
-- -- VALUES (1, 2, 'Great Movie!', 9, 'This movie was amazing. I loved the storyline and the acting.', CURRENT_TIMESTAMP);

-- -- Inserting the second review
-- -- INSERT INTO reviews (film_id, language_id, title, score, review_text, last_update)
-- -- VALUES (2, 1, 'Enjoyable Film', 8, 'It was a fun movie to watch with family. Highly recommended!', CURRENT_TIMESTAMP);


-- -- Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- --- when the film is deleted the review is deleted too
-- -- DELETE FROM film
-- -- WHERE id = 1;



-- EXERCISE 2
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- UPDATE film
-- SET language_id = 2 
-- WHERE film_id = 1;
-- UPDATE film
-- SET language_id = 5 
-- WHERE film_id = 3;

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- SELECT
--     conname AS foreign_key_name,
--     conrelid::regclass AS table_name,
--     a.attname AS column_name,
--     confrelid::regclass AS referenced_table_name,
--     af.attname AS referenced_column_name
-- FROM
--     pg_constraint AS c
--     JOIN pg_attribute AS a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid
--     JOIN pg_attribute AS af ON af.attnum = ANY(c.confkey) AND af.attrelid = c.confrelid
-- WHERE
--     c.confrelid = 'customer'::regclass;
-- The foreign key constraint ensures that the value being inserted into the foreign key column (e.g., customer_id) must match an existing value in the referenced table (the table referenced by the foreign key). 
-- if it's allowed the foreign key column allows NULL values, you can insert a NULL 
-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- SELECT COUNT(*) FROM rental 
-- WHERE return_date IS NULL

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- SELECT title
-- FROM film f
-- INNER JOIN inventory ON f.film_id = inventory.film_id
-- INNER JOIN rental on rental.inventory_id = inventory.inventory_id
-- ORDER BY replacement_cost DESC
-- LIMIT 30;


-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT title, description 
-- from film f
-- where fulltext @@ tsquery('sumo') AND fulltext @@ tsquery('wrestler')
-- SELECT title, description
-- FROM film
-- INNER JOIN film_actor fa on film.film_id = fa.film_id
-- WHERE description ILIKE '%sumo wrestler%'
-- AND first_name ILIKE '%penelope%'
-- and last_name ILIKE '%monroe%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- SELECT title,  category.name, film.length
-- FROM film
-- INNER JOIN film_category AS fc ON film.film_id = fc.film_id
-- INNER JOIN category ON category.category_id = fc.category_id
-- WHERE category.name ILIKE '%documentary%'
-- AND film.length < 60
-- AND rating = 'R'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- SELECT film.title, payment.amount, customer.first_name, customer.last_name 
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN payment ON rental.rental_id = payment.rental_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE payment.amount > 4 AND
-- customer.first_name = 'Matthew' AND
-- customer.last_name = 'Mahan'
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

-- SELECT film.title, film.replacement_cost
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE 
-- customer.first_name = 'Matthew' 
-- AND
-- customer.last_name = 'Mahan'
-- AND (title ILIKE '%boat%' OR description ILIKE '%boat%')
-- ORDER BY film.replacement_cost DESC