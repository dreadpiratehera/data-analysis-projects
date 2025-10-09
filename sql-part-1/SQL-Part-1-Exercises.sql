USE BooksDB ;
--A. The Books table (BooksDB.dbo.books)

--Question 1: Select the [top 1000 rows](https://www.w3schools.com/sql/sql\\_top.asp) from the books table.  Make sure you are able to see all of the columns.
SELECT TOP 1000 *
FROM BooksDB.dbo.books;

--Question 2: Count the number of titles.  Are there 10,000 titles as promised by the dataset?
--Answer: Yes, there are 10,000 titles
SELECT COUNT (*)
FROM BooksDB.dbo.books;

--Question 3: Count the number of books where the `original_publication_year` is earlier than 1800.
--Answer: 125
SELECT COUNT(*)
FROM BooksDB.dbo.books
WHERE original_publication_year <1800;

--Question 4: Create a query that displays distinct authors from the table.
SELECT DISTINCT authors
FROM BooksDB.dbo.books;

--Question 5: Create a query that displays a count of all the books that contain a language code for English.  This could be represented in the table as \"eng\" or \"en-\".
SELECT COUNT(*)
FROM BooksDB.dbo.books
WHERE language_code LIKE 'en%';

--Question 6: Create a query to check how many original titles were written during World War I era (1914-1921).
SELECT COUNT(*)
FROM BooksDB.dbo.books
WHERE (original_publication_year > 1913) AND (original_publication_year < 1922);

--B The Book Tags table (BooksDB.dbo.book_tags)
--Question 1: Select the top 1000 table items ordered by the `tag_id`.

SELECT TOP 1000 *
FROM BooksDB.dbo.book_tags
ORDER BY tag_id;

--Question 2: Create a query that counts the number of `goodreads_book_id` grouped by the `tag_id`.

SELECT COUNT(goodreads_book_id)
FROM BooksDB.dbo.book_tags
GROUP BY tag_id;

--Question 3: In the last query, we created a new, unnamed column.  Use `AS` to create an alias to provide a name of your choice to this new column.

SELECT COUNT(goodreads_book_id) AS "Books per Tag"
FROM BooksDB.dbo.book_tags
GROUP BY tag_id;

--C The Ratings table (BooksDB.dbo.ratings)
--Question 1: Create a query that displays the top 1000 items in the table in descending order.

SELECT TOP 1000 *
FROM BooksDB.dbo.ratings
ORDER BY rating DESC;

--Question 2: Create a query that returns the total number of users that have given a rating of less than 2.

SELECT COUNT (DISTINCT(user_id))
FROM BooksDB.dbo.ratings
WHERE rating <2;

--Question 3: Create a query that returns the sum of books that have a rating of 4 or higher.
/*NOTE: I proceeded as though this were asking for a count of books that had received any ratings of 4 or higher. 
I was unable to figure out how to get it to filter by average rating*/

SELECT COUNT (DISTINCT(book_id))
FROM BooksDB.dbo.ratings
WHERE rating>=4;

--D The Tags table (BooksDB.dbo.tags)
--Question 1: Create a query that returns table items where the `tag_name` describes the book as a mystery.

SELECT *
FROM BooksDB.dbo.tags
WHERE tag_name LIKE '%myster%';

--Question 2: Run the query below. In your own words, what is it returning?
-- SELECT *
   -- FROM BooksDB.BooksDB.dbo.tags
   -- WHERE tag_name < 'd' AND tag_name >= 'c';

   /*Answer: It is returning items where the tag name is, or begins with, the letter "C".*/

 SELECT *
 FROM BooksDB.BooksDB.dbo.tags
 WHERE tag_name < 'd' AND tag_name >= 'c';

 -- To Read table (BooksDB.dbo.to_read)
 /*Question 1:  Create a query that uses the `user_id` to count the total number of books that each user wants to read.  
 Print the results in ascending order by `user_id` under the alias 'Total Books To Read'.*/

 SELECT user_id, (COUNT(user)) AS "Total Books To Read"
 FROM BooksDB.dbo.to_read
 GROUP BY user_id;

 /*Question 2: Create a query that uses `user_id` to count the total number of books each user wants to read.  
 Have the results sort the table by the total number of `book_ids` in descending order and under the alias 'Total Books To Read'.*/

 SELECT user_id, (COUNT(user)) AS "Total Books To Read"
 FROM BooksDB.dbo.to_read
 GROUP BY user_id
 ORDER BY "Total Books To Read" DESC;

