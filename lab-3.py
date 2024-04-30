# 1- Create class employee with the following characteristics:

#! /bin/env python3
from typing import List
from mysql.connector import connect, Error  # type: ignore
from uuid import uuid4


DB_URL = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "python"


class Employee:
    employees: List["Employee"] = []

    def __init__(self, first_name, last_name, age, department, salary) -> None:
        self.id = str(uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
        insert_employee(mydb, self)

    def transfer(self, department):
        pass
        transfer_employee(mydb, department, self)

    def fire(self):
        Employee.employees.remove(self)
        delete_employee(mydb, self)

    def show(self):
        show_employee(mydb, self)

    def list_employees(self):
        show_all_empolyees(mydb)


def connect_to_db(DB_URL, DB_USER, DB_PASSWORD, DB_DATABASE):
    try:
        db = connect(
            host=DB_URL, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
        )
        return db
    except Error as e:
        print("error connecting the database")
        print(e)


def create_employee_table(connection):
    try:
        cur = connection.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS employees(
                    id VARCHAR(50) PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    age INT NOT NULL NOT NULL,
                    department VARCHAR(50),
                    salary FLOAT
                    )"""
        )
        connection.commit()
        print("Table employee was created successfully")
    except Error as e:
        print("there is an error happend when creating the table")
        print(e)


def insert_employee(connection, employee):
    try:
        cur = connection.cursor()
        cur.execute(
            """INSERT INTO employees (id, first_name, last_name, age, department, salary)
                VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                employee.id,
                employee.first_name,
                employee.last_name,
                employee.age,
                employee.department,
                employee.salary,
            ),
        )
        connection.commit()
        print("employee was added successfully")
    except Error as e:
        print("there is an error happend when adding the employee")
        print(e)


def transfer_employee(connection, department, employee):
    oldDepartment = employee.department
    try:
        cur = connection.cursor()
        cur.execute(
            """
            Update employees
                SET department = %s
                WHERE id = %s
                    """,
            [department, employee.id],
        )
        connection.commit()
        print(f"employee has been transfer from {oldDepartment} to { department }")
    except Error as e:
        print(f"there is an error happend when transfer the employee")
        print(e)


def delete_employee(connection, employee):
    try:
        cur = connection.cursor()
        cur.execute(
            """
            DELETE FROM employees
                WHERE id = %s
                    """,
            [employee.id],
        )
        connection.commit()
        print(f"employee has been deleted successfully")
    except Error as e:
        print(f"there is an error happend when deleting the employee")
        print(e)


def show_employee(connection, employee):
    try:
        cur = connection.cursor()
        cur.execute(
            """
            SELECT * FROM employees
                WHERE id = %s
                    """,
            [employee.id],
        )
        employee_data = cur.fetchone()
        print(employee_data)
    except Error as e:
        print(f"there is an error happend when showing the employee")
        print(e)


def show_all_empolyees(connection):
    try:
        cur = connection.cursor()
        cur.execute(
            """
            SELECT * FROM employees
                    """,
        )
        employees_data = cur.fetchall()
        print(employees_data)
    except Error as e:
        print(f"there is an error happend when showing the employees")
        print(e)


mydb = connect_to_db(DB_URL, DB_USER, DB_PASSWORD, DB_DATABASE)

if mydb:
    create_employee_table(mydb)
    emp1 = Employee("Belal", "Abo Ata", 23, "IT", 3000)
    emp2 = Employee("Belal", "Mohamed", 17, "SA", 2000)
    emp3 = Employee("Belal", "Ali", 32, "MA", 2000)

    emp1.list_employees()
    emp1.show()
    emp1.transfer("MA")
    emp2.fire()
    emp1.list_employees()
