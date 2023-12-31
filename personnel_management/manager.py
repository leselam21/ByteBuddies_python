
#USAGE: python manager.py 


from employee import Employee
class Manager(Employee):
    managers =[]
    def __init__(self, fname, lname, employee_id,salary, manager_id):
        super().__init__(fname,lname, employee_id, salary)
        self.manager_id = manager_id
        self.teammates = []
        Manager.managers.append(self)
    
    @classmethod
    def assign_manager(cls, employee_id,manager_id):
        assigned_manager = Employee.find_by_id(employee_id)
        if assigned_manager:
            setattr(assigned_manager, "manager_id", manager_id)
            Manager.managers.append(assigned_manager)
        else:
            print(f"We don't have employee of  employee_id : {employee_id}. ")
        
    @classmethod
    def add_teammate(cls, manager_id, teammate_id):
        pass 

    @classmethod
    def find_manager_by_name(cls, search_name):
        for manager in cls.managers:
            if manager.get_full_name() == search_name:
               manager.display_info()
               return True
            return False
         
         

    @classmethod
    def find_manager_by_id(cls, search_id):
        pass 

    @classmethod
    def show_all_managers(cls):
        print("\nAll Registered Employees:")
        if len(cls.managers) ==0 :
            print("None: Manager list is empty")
        for manager in cls.managers:
            print(f"Employee_Id: {manager.employee_id} manager_Id: {manager.manager_id} first_name: {manager.first_name} last_name: {manager.last_name} salary: {manager.pay:.3f}")


    def remove_teammate(self, temate_id):
        pass
    
    def remove_manager(self, man_id):
        pass
    
    def show_teammates(cls, man_id):
        """Display teammates of the Manager whose ID is man_id."""
        pass 

    def do_more(self):
        """
        Feel free to add more members if deemed crucial
        """

if __name__ == '__main__':
    man =  Manager("Kass", "Haile","E001", 5000, "m001")
    man.apply_raise(15)
    man2 = Manager("Dani", "sami", "E002", 6000, "man002")
    print(f"1. {man.get_full_name()} monthly pay is {man.get_pay()}")
    print(f"2. {man.get_full_name()} said we are {man.count}.")

