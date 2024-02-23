# 0x0F. Python - Object-relational mapping

## Description
This project is a part of the Holberton School curriculum, focusing on Object-relational mapping (ORM) in Python, covering concepts such as Python, OOP, SQL, MySQL, ORM, and SQLAlchemy. The project, authored by Guillaume, carries a weight of 1 and is scheduled to start on February 14, 2024, at 7:00 PM, with a deadline set for February 18, 2024, at 7:00 PM. The checker was released on February 15, 2024, at 7:00 PM, and an auto review will be launched at the deadline.

Before beginning the project, it is essential to ensure that the MySQL server is in version 8.0. Instructions on how to install MySQL 8.0 on Ubuntu 20.04 are provided.

## Background Context
This project aims to bridge the gap between Databases and Python. It consists of two parts:

1. Utilizing the MySQLdb module to connect to a MySQL database and execute SQL queries.
2. Implementing SQLAlchemy, an Object Relational Mapper (ORM), to abstract the storage to the usage, eliminating the need for writing SQL queries directly in Python code.

With SQLAlchemy ORM, the focus shifts from SQL queries to working with Python objects, enabling seamless interaction with the database without being dependent on the storage type.

## Resources
To prepare for the project, it is recommended to read or watch resources such as:
- Object-relational mappers
- MySQLclient/MySQLdb documentation
- SQLAlchemy documentation and tutorials
- Python Virtual Environments tutorial
- Other relevant tutorials and guides listed in the project description

## Learning Objectives
Upon completion of the project, learners are expected to:
- Understand the benefits of Python programming
- Know how to connect to a MySQL database from a Python script
- Be able to execute SELECT and INSERT operations on MySQL tables using Python
- Grasp the concept of ORM and its advantages
- Learn how to map a Python Class to a MySQL table
- Create and utilize Python Virtual Environments effectively

## Requirements
General requirements for the project include:
- Ubuntu 20.04 LTS environment
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Usage of permitted editors: vi, vim, emacs
- Adherence to specified coding style (pycodestyle)
- Mandatory README.md file containing project overview, resources, learning objectives, and requirements
- Proper documentation for modules, classes, and functions

## Installation and Setup
To set up the project environment:
1. Install and activate Python Virtual Environment:
    ```
    $ sudo apt-get install python3.8-venv
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
2. Install MySQLdb version 2.0.x:
    ```
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```

3. Install SQLAlchemy version 1.4.x:
    ```
    $ sudo pip3 install SQLAlchemy
    ```

## Note
Ignore any warning messages during the installation process.

For detailed instructions and further assistance, refer to the provided resources and project guidelines.

## Author
Guillaume

