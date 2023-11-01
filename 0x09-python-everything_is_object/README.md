# 0x09. Python - Everything is Object

![Python](https://img.shields.io/badge/Python-v3.8.5-blue)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-green)
![By Guillaume](https://img.shields.io/badge/By-Guillaume-orange)
![Weight: 1](https://img.shields.io/badge/Weight-1-lightgrey)

Project started on: October 30, 2023 7:00 PM
Project deadline: October 31, 2023 7:00 PM
Checker release date: October 31, 2023 1:00 AM
Auto review will be launched at the deadline.

## Background Context

In this project, we will delve deeper into Python and its handling of different types of objects. We'll explore the concept that "everything is an object" in Python and how it impacts the behavior of variables and objects.

Have you ever wondered why some Python assignments result in unexpected behavior, like modifying a variable unintentionally? This project will address such questions and help you gain a better understanding of Python's object-oriented nature.

For example:

```python
a = 1
b = a
a = 2
print(b)  # Output: 1
```

And:

```python
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # Output: ['x', 2, 3]
```

This project consists of questions about Python's specific behavior, such as predicting the results of various code snippets. To succeed, you should read Python documentation, think critically, and collaborate with your peers before attempting any code. This approach ensures a deeper understanding of Python's behavior and its implications for variables and object types.

Understanding these concepts is crucial, as you may encounter similar questions during Python job interviews.

## Resources

Read or watch:

- [9.10. Objects and values](https://docs.python.org/3/reference/datamodel.html#objects-values)
- [9.11. Aliasing](https://docs.python.org/3/reference/datamodel.html#aliasing)
- [Immutable vs mutable types](https://docs.python.org/3/reference/datamodel.html#types)
- [Mutation (Only this chapter)](https://docs.python.org/3/reference/datamodel.html#mutability)
- [9.12. Cloning lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python tuples: immutable but potentially changing](https://docs.python.org/3/tutorial/introduction.html#tuples)
- [Learning Objectives](#learning-objectives)

## Learning Objectives

By the end of this project, you should be able to explain, without assistance:

**General**
- Why Python programming is awesome
- What is an object
- The difference between a class and an object or instance
- The difference between immutable objects and mutable objects
- What is a reference
- What is an assignment
- What is an alias
- How to determine if two variables are identical
- How to determine if two variables are linked to the same object
- How to display the variable identifier (memory address in the CPython implementation)
- What is mutable and immutable
- The built-in mutable types
- The built-in immutable types
- How Python passes variables to functions

## Copyright - Plagiarism

You must come up with solutions for the tasks in this project independently to meet the learning objectives. Copying and pasting someone else's work is strictly prohibited and may result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly `#!/usr/bin/python3`
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### .txt Answer Files

- Only one line
- No Shebang
- All your files should end with a new line

Now, dive into the project, learn more about Python's object-oriented nature, and enjoy exploring the fascinating world of Python programming!
