"""
  Inheritance :
            Employee: Parent class 
            Manager: Subclass 
  Purpose: Demonstrating Inheritance relationship in Python
  
"""

class Employee:
     def __init__(self, first_name, last_name, employee_id, salary):
         self.first_name = first_name
         self.last_name =  last_name
         self.employee_id = employee_id
         self.pay = salary
     
     def get_full_name (self):
        return "Employee Full Name : {}  {}".format(self.first_name, self.last_name)
       
     def display_info(self):
         print(f"Employee_Id:{self.employe_id}, Name :{self.name},  salary: {self.salary:.3f}")
     def apply_raise(self, raise_percent):
        self.pay = self.pay + round(self.pay * raise_percent/100)
     
     def get_pay(self):
         return self.pay
     
     def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first_name, self.last_name, self.pay)
     def help(self):
        print(help(self))


if __name__ == '__main__':
    emp =  Employee("Selam", "Demise", "001", 5000)
    print(f"1. {emp.get_full_name()}")
    emp.apply_raise(20)
    print(f"2. {emp.get_pay()}")
    print(f"3. {emp}")
