# 0x0E. SQL - More queries

## Introduction

This project focuses on expanding your knowledge of SQL by covering various concepts and techniques. You will work with MySQL 8.0 and perform tasks related to user management, privileges, constraints, and advanced SQL queries.

## Resources

Read or watch the following resources to enhance your understanding:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://www.mysqltutorial.org/mysql-constraints/)
- [SQL technique: subqueries](https://www.sqltutorial.org/sql-subquery/)
- [Basic query operation: the join](https://www.sqlshack.com/basic-query-operations-using-joins/)
- [SQL technique: multiple joins and the distinct keyword](https://www.sqltutorial.org/sql-joins/sql-joins-combined-with-distinct/)
- [SQL technique: join types](https://www.sqlshack.com/joining-multiple-tables-sql/)
- [SQL technique: union and minus](https://www.sqlshack.com/sql-union-sql-minus-two-ways-combine-query-results/)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [The Seven Types of SQL Joins](https://www.bmc.com/blogs/sql-joins/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

### Extra resources around relational database model design:

- [Design](https://www.lucidchart.com/pages/database-design)
- [Normalization](https://www.studytonight.com/dbms/database-normalization.php)
- [ER Modeling](https://www.tutorialspoint.com/dbms/entity_relationship_model_basic_concepts.htm)

## Learning Objectives

By the end of this project, you should be able to:

- Create a new MySQL user
- Manage privileges for a user to a database or table
- Understand the concepts of PRIMARY KEY and FOREIGN KEY
- Utilize NOT NULL and UNIQUE constraints
- Retrieve data from multiple tables in one request
- Work with subqueries
- Implement JOIN and UNION operations in SQL

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file at the root of the project folder is mandatory
- The length of your files will be tested using wc

## How to Use

Follow the steps below to set up and use MySQL 8.0 on Ubuntu 20.04:

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:

    ```bash
    $ sudo apt update
    $ sudo apt install mysql-server
    ```

2. Check the MySQL version:

    ```bash
    $ mysql --version
    ```

3. Connect to your MySQL server:

    ```bash
    $ sudo mysql
    ```

4. Use "container-on-demand" to run MySQL:

    - Ask for a container with Ubuntu 20.04
    - Connect via SSH or use the Web terminal
    - Start MySQL in the container:

        ```bash
        $ service mysql start
        ```

5. How to import a SQL dump:

    ```bash
    $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
    $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
    $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
    ```

## Tasks

Each task involves performing specific actions in MySQL. Follow the instructions in each task to complete them.

### Example Comment for SQL Files:

```sql
-- Retrieve the first 3 students in Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;