
#USAGE: python manager.py 


from employee import Employee

class Manager(Employee):
    def __init__(self, fname, lname, employee_id,salary, man_id):
        super().__init__(fname,lname, employee_id, salary)
        self.man_id = man_id
        self.teammates = []
    
    @classmethod
    def assign_manager(self, manager_id):
        pass 

    @classmethod
    def add_teammate(cls, manager_id, teammate_id):
        pass 

    @classmethod
    def find_manager_by_name(cls, search_name):
        pass

    @classmethod
    def find_manager_by_id(cls, search_id):
        pass 

    @classmethod
    def show_all_managers(cls):
        pass 

    def remove_teammate(self, temate_id):
        pass
    
    def remove_teammate(self, temate_id):
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
