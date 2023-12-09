

#USAGE: python employee.py 

"""
  Inheritance :
            Employee: Parent class 
            Manager: Subclass 
  Purpose: Demonstrating Inheritance relationship in Python
  
"""

class Employee:
     count = 0
     def __init__(self, first_name, last_name, employee_id, salary, man_id=None):
         self.first_name = first_name
         self.last_name =  last_name
         self.employee_id = employee_id
         self.pay = salary
         self.man_id = man_id 
         Employee.count +=1
     
     def get_full_name (self):
        return "{}  {}".format(self.first_name, self.last_name)
       
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
    emp2 =  Employee("Gebre", "Gemechu", "002", 7000)
    emp3 =  Employee("Hagos", "Desta", "003", 6000)
    emp4 =  Employee("Gemechu", "Demise", "004", 15000)

    print(f"1. {emp.get_full_name()}")
    emp.apply_raise(20)
    print(f"2. {emp.get_pay()}")
    print(f"3. {emp}")
    print(f"4. {emp4}")
    print(f"5. {emp.get_full_name()} said there are {emp.count} employees")
    print(f"6. {emp4.get_full_name()} said there are {emp4.count} employees")
    print(f"7. Woow! how {emp.get_full_name()} knew that there are {emp4.count} employees")
    print(f"8. Did {emp.get_full_name()} know everything {emp4.get_full_name()} knows???")
