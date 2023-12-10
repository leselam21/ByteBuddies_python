

#USAGE: python main.py 

""" This program is the User Interface Program !"""
from employee import Employee
from manager import Manager


def main():
    while True:
        print("\t========================")
        print("\t===   Main Menu:  ======")
        print("\t===   ----------  ======")
        print("\t===               ======")
        print("\t===  1. Employee  ======")
        print("\t===  2. Manager   ======")
        print("\t===  3. Exit      ======")
        print("\t========================")

        choice = input("\tEnter your choice (1, 2 or 3): ")
        if choice == "1":
                print("\n\t---------------------------")
                print("\t      Employee Menu:")
                print("\t      --------------         ")
                print("\t1. Register ")
                print("\t2. Find by ID ")
                print("\t3. Find by Name ")
                print("\t4. Show All Employees ")
                print("\t5. Help              ")
                print("\t6. Back to Main Menu ")
                print("\n\t---------------------------")
                employee_choice = input("\tEnter your choice: any of(1,2, 3, 4,5): ")
                if employee_choice == "1":
                    employee_info = {
                        "name": input("Enter employee name: "),
                        "employee_id": input("Enter employee ID: "),
                        "salary": float(input("Enter employee salary: "))
                    }
                    employee = Employee(**employee_info)
                    employee.display_info()
                elif employee_choice == "2":
                    print("Please write me,I am waiting for you :)")
                elif employee_choice == "3":
                    print("Please write me,I am waiting for you :)")
                elif employee_choice == "4":
                    Employee.show_employees()
                else:
                     print("Please write me,I am waiting for you :)")
        elif choice == "2":
            while True:
                print("\nManager Menu:")
                print("1. Promote to Manager")
                print("2. Add Teammate")
                print("3. Find by ID")
                print("4. Find by Name")
                print("5. Show All Managers")
                print("6. Help")
                print("7. Back to Main Menu")
                manager_choice = input("Enter your choice (1/2/3/4/5/6/7): ")

                if manager_choice == "1":
                    employee_id = input("Enter Employee ID to assign as a Manager: ")
                    Manager.assign_manager(employee_id)
                elif manager_choice == "2":
                    print("Please write me,I am waiting for you :)")
                elif manager_choice == "3":
                    print("Please write me,I am waiting for you :)")
                elif manager_choice == "5":
                    Manager.show_managers()
                elif manager_choice == "6":
                    Manager.help() 
                elif manager_choice == "7":
                    break 
                else:
                    print("Please write me,I am waiting for you :)")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")




if __name__ == '__main__':
     main()