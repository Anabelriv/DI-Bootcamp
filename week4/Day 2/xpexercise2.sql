-- We will use the newly installed dvdrental database.

-- In the dvdrental database write a query to select all the columns from the “customer” table.

-- SELECT * from customer;

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
 
-- SELECT first_name || ' ' || last_name AS full_name
-- FROM customer;


-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

-- SELECT DISTINCT create_date from customer;

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

-- SELECT * from customer
-- ORDER by first_name DESC;

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

-- SELECT film_id, title, description, release_year, rental_rate from film
-- ORDER BY rental_rate;

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

-- SELECT address, phone from address
-- where district = 'Texas';

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.

-- SELECT * from film 
-- WHERE film_id IN (15,150);

-- Write a query which should check if your favorite movie exists in the database. 
-- Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

-- SELECT film_id, title, description, length, rental_rate from film
-- WHERE title = 'Home Alone';
-- No luck finding your movie? Maybe you made a mistake spelling the name. 
-- Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

-- SELECT film_id, title, description, length, rental_rate from film
-- WHERE title LIKE 'Ho%';
-- Write a query which will find the 10 cheapest movies.
-- SELECT title, rental_rate from film
-- ORDER by rental_rate 
-- LIMIT 10;

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.

-- SELECT title, rental_rate from film
-- ORDER BY rental_rate
-- OFFSET 10
-- FETCH FIRST 10 ROWS ONLY;

-- Write a query which will join the data in the customer table and the payment table. 
-- You want to get the first name and last name from the curstomer table, 
-- as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- From customer join payment on customer.customer_id = payment.customer_id
-- ORDER by customer.customer_id;

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
-- get film ID, title Join film, and inventory, show film they left join on film_id

-- SELECT film.film_id, film.title, inventory.film_id as inventory
-- FROM film left join inventory on film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;


-- Write a query to find which city is in which country. they have country_id in common 

-- SELECT city.city, country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id;


-- Bonus You want to be able to see how your sellers have been doing? 
-- Write a query to get the customer’s id, names (first and last), 
-- the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
-- I need to join 3 tables them by staff_id for payment and staff and customer id for customer and payment 

-- SELECT  staff.staff_id, customer.customer_id, customer.first_name || ' ' || customer.last_name AS full_name, payment.amount, payment.payment_date
-- FROM customer 
-- INNER JOIN payment on payment.customer_id = customer.customer_id
-- INNER JOIN staff on staff.staff_id = payment.staff_id
-- ORDER BY staff.staff_id

