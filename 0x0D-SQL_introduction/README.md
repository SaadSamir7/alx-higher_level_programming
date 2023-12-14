# 0x0D. SQL - Introduction

## Description

This project is an introduction to SQL (Structured Query Language) and MySQL. The goal is to gain a fundamental understanding of databases, relational databases, and basic SQL commands.

## Concepts

For this project, the following concepts are covered:

- Databases
- What is a relational database
- SQL (Structured Query Language)
- MySQL
- DDL (Data Definition Language) and DML (Data Manipulation Language)
- Creating and altering tables
- Selecting data from a table
- Inserting, updating, or deleting data
- Subqueries
- MySQL functions

## Resources

Before starting the project, it is recommended to read or watch the following:

- [What is Database & SQL?](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL statements: DDL and DML](#) (no need to read the chapter “Privileges”)
- [Basic queries: SQL and RA](#)
- [SQL technique: functions](#)
- [SQL technique: subqueries](#)
- [What makes the big difference between a backtick and an apostrophe?](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)
- [Installing MySQL in Ubuntu 20.04](#)

## Learning Objectives

At the end of this project, you should be able to explain:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

- Allowed editors: vi, vim, emacs
- Files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- Files should end with a new line
- SQL queries should have a comment just before (i.e., syntax above)
- Files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file at the root of the project folder is mandatory
- The length of files will be tested using wc

## Example

Comments for your SQL file:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Installation

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

### Connect to your MySQL server

```bash
$ sudo mysql
```

## Usage

In the container, credentials are root/root.

```bash
$ service mysql start
$ cat 0-list_databases.sql | mysql -uroot -p
```

In the container, credentials are root/root.

## Author

Guillaume