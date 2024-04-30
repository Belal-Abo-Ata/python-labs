from lab3 import *


def main_menu():
    print("Employee Management System")
    print("1. Add Employee")
    print("2. Transfer Employee")
    print("3. Fire Employee")
    print("4. Show Employee Details")
    print("5. List All Employees")
    print("q. Quit")


def add_employee():
    id = input("Enter ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employee = Employee(id, first_name, last_name, age, department, salary)


def transfer_employee():
    employee_id = input("Enter employee ID: ")
    new_department = input("Enter new department: ")

    # Find the employee and transfer them
    for employee in Employee.employees:
        if employee.id == employee_id:
            employee.transfer(new_department)
            break
    else:
        print("Employee not found.")


def fire_employee():
    # Prompt the user to enter employee ID
    employee_id = input("Enter employee ID: ")

    # Find and fire the employee
    for employee in Employee.employees:
        if employee.id == employee_id:
            employee.fire()
            break
    else:
        print("Employee not found.")


def show_employee_details():
    # Prompt the user to enter employee ID
    employee_id = input("Enter employee ID: ")

    # Find and show the employee details
    for employee in Employee.employees:
        if employee.id == employee_id:
            employee.show()
            break
    else:
        print("Employee not found.")


def list_all_employees():
    # List all employees
    Employee.list_employees()


def main():
    mydb = connect_to_db(DB_URL, DB_USER, DB_PASSWORD, DB_DATABASE)
    if mydb:
        create_employee_table(mydb)

        while True:
            main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                add_employee()
            elif choice == "2":
                transfer_employee()
            elif choice == "3":
                fire_employee()
            elif choice == "4":
                show_employee_details()
            elif choice == "5":
                list_all_employees()
            elif choice.lower() == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


main()
