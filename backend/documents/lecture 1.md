# Introduction to Database Management Systems

**[CSCI 11062]**

**Database system concepts and architecture**  
*Part I*

*Dr. (Mrs.) Muditha Tissera*  
Email: mudithat@kln.ac.lk

---

## Session Objectives

- Identify a DB and a DBMS
- Characteristics and problems of data storage mechanisms
- The advantages and disadvantages of the DB approach
- Levels of abstraction in a DBMS
  - Three-Schema Architecture (ANSI-SPARC)

---

## What is a Database?

A Database is a collection of related data. It is designed to meet the information needs of multiple users in an organization.

- Designed, built, and populated for a specific purpose
- Has an intended group of users and predetermined applications
- Logically coherent collection of data and description with inherent meaning
- Represents some aspect of the real world (mini world)
- The description of the data is known as the data dictionary or meta-data ("data about data")

---

## Databases Usage Examples

- **Universities**: Student registrations, exams, and marks
- **Library Management Systems**: Members, books
- **Social Media Sites**: Users, posts
- **Telecommunication Applications**: Users, call records
- **Online Shopping Applications**: Products, sellers, customers
- **Sales and Manufacturing**: Customers, products, purchases
- **Banks**: ATM
- **Airlines**: Reservations, schedules
- **Manufacturing**: Production, inventory, orders, supply chain
- **Human Resource Management Systems**: Employee records, salaries, tax deductions

---

## Types of Databases

- Numeric and Textual Databases (e.g., Telecom service providers)
- Multimedia Databases (e.g., Amazon, iTunes, Google Play)
- Spacial Databases (e.g., GIS, Google Maps)

---

## What is a Database Management System (DBMS)?

A software package designed to create and maintain computerized databases.

- General-purpose software system

---

## Functions of DBMS

- **Defining**: Specifying data types, structures, and constraints for the data
- **Constructing**: Storing the data on a storage medium controlled by the DBMS
- **Manipulating**: Querying, updating, and generating reports from the data
- **Sharing**: Allowing multiple users and programs to access the DB concurrently

---

## DBMS Examples

| Market         | Type         | Vendor            | DBMS                 |
|----------------|--------------|-------------------|----------------------|
| Desktop        | Relational   | Microsoft         | Access               |
| Enterprise     | Relational   | Microsoft         | SQL Server           |
| Mobile/Embedded| Relational   | Centura Software  | SQLBase              |
| VLDB           | Relational   | NCR               | Teradata             |
| Enterprise     | Object Relational | IBM          | DB2                  |
| Open Source    | Relational   | Freeware          | MySQL                |
| Open Source    | Object Relational | Freeware     | PostgreSQL           |

---

## Data Storage & Retrieval Options

- **Manual Processing**: Time-consuming, does not support large data volumes
- **File-based Processing**: Traditional computer files, inadequate
- **Database Processing**

---

## File-based Processing

An obsolete approach where each program manages its own data.

- **Limitations**: Data redundancy, inconsistency, inflexibility, poor data sharing, and more

---

## Database Approach

- **Solution**: Use of a Database and DBMS for program-data independence and efficient data management.

---

## Advantages of Using a DBMS

- Controlling redundancy
- Data consistency
- Efficient data access
- Data integrity and security
- Concurrent access and crash recovery
- Reduced application development time
- More information from the same amount of data

---

## Levels of Abstraction in a DBMS

### Three-Schema Architecture (ANSI-SPARC)

1. **External Level**: User's view of the database
2. **Conceptual Level**: Structure of the database for the community of users
3. **Internal Level**: Physical storage of the data

### Data Independence

- **Logical Data Independence**: Modify the conceptual schema without affecting external schemas or applications.
- **Physical Data Independence**: Modify the internal schema without affecting the conceptual schema.

---

## Disadvantages of DBMS

- Increased complexity
- Growing size
- Cost of DBMS and hardware
- Performance issues
- Higher impact of failures

---

*End of Lecture 1 – Part I*

Questions?
