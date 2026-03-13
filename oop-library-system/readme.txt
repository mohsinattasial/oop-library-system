# OOP Library Management System

## Project Title
Library Management System using Python (OOP)

## Description
This project implements a simple Library Management System using Object Oriented Programming in Python. 
The system allows adding books, registering members, borrowing books, returning books, and calculating fines for late returns.

The main goal of this project is to demonstrate proper OOP design and separation of business logic from user interface.

## Features
- Add new books to the library
- Register new members
- Borrow books
- Return books
- Automatic fine calculation for late returns
- Borrow limit enforcement (maximum 3 books per member)

## OOP Concepts Used
- **Encapsulation** – Book availability and borrowed books are private attributes.
- **Abstraction** – Fine calculation is implemented using an abstract `FinePolicy`.
- **Composition** – Library contains Book, Member, and BorrowRecord objects.
- **Polymorphism** – Different fine policies can be implemented and used without changing the Library class.
- **Separation of Concerns** – Business logic and CLI are separated.

## Project Structure

oop-library-system/