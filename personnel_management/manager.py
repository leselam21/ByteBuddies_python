
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
    def assign_manager(cls, employee_id, manager_id):
        for emp in Employee.employees:
            if emp.employee_id == employee_id:
                if not any(manager.employee_id == employee_id for manager in cls.managers):
                    # assign the employee to a manager
                    new_manager = Manager(emp.first_name, emp.last_name, emp.employee_id, emp.pay, manager_id)
                    print(f"Employee {employee_id} is now assigned as a manager with manager ID {manager_id}.")
                    return
        print(f"We don't have an employee with employee_id: {employee_id}.")

    
    @classmethod
    def add_teammate(cls, manager_id, teammate_id):
        # Find the manager
        for manager in cls.managers:
            if manager.manager_id == manager_id:
                # Check if the employee is already a teammate
                for teammate in manager.teammates:
                    if teammate.employee_id == teammate_id:
                        print("This employee is already a teammate.")
                        return True

                # Find the employee and add them as a teammate
                new_teammate = Employee.find_by_id(teammate_id)
                if new_teammate:
                    manager.teammates.append(new_teammate)
                    print(f"Employee {new_teammate.get_full_name()} added as a teammate to manager {manager.get_full_name()}.")
                    return True
                print("Employee not found.")
                return False
        print(f"No manager found with ID {manager_id}.")
        return False

    @classmethod
    def find_manager_by_name(cls, search_name):
        for manager in cls.managers:
            if manager.get_full_name() == search_name:
               manager.display_info()
               return True
        return False

    @classmethod
    def find_manager_by_id(cls, search_id):
        for manager in cls.managers:
            if manager.manager_id == search_id:
                manager.display_info()
                return True
        return False

    @classmethod
    def show_all_managers(cls):
        print("\nAll Registered Managers:")
        if len(cls.managers) ==0 :
            print("None: Manager list is empty")
        for manager in cls.managers:
            print(f"Employee_Id: {manager.employee_id} manager_Id: {manager.manager_id} first_name: {manager.first_name} last_name: {manager.last_name} salary: {manager.pay:.3f}")

    @classmethod
    def find_teammate_by_name(cls, search_name):
        search_name = search_name.strip().lower()
        for manager in cls.managers:
            for teammate in manager.teammates:
                if teammate.get_full_name().lower == search_name:
                    print(f"Teammate found: {teammate.get_full_name()} (ID: {teammate.employee_id}), managed by {manager.get_full_name()} (Manager ID: {manager.manager_id}).")
                    return True
        print(f"No teammate found with name: {search_name}.")
        return False

    @classmethod
    def find_teammate_by_id(cls, search_id):
        for manager in cls.managers:
            for teammate in manager.teammates:
                if teammate.employee_id == search_id:
                    print(f"Teammate found: {teammate.get_full_name()} (ID: {search_id}), managed by {manager.get_full_name()} (Manager ID: {manager.manager_id})")
                    return True

        print(f"No teammate found with ID: {search_id}.")
        return False
        
    @classmethod
    def show_teammates(cls, man_id):
        """Display teammates of the Manager whose ID is man_id."""
        for manager in cls.managers:
            if manager.manager_id == man_id:
                if not manager.teammates:
                    print(f"Manager with ID {man_id} has no teammates.")
                    return

                print(f"Teammates of Manager {man_id} ({manager.get_full_name()}):")
                for teammate in manager.teammates:
                    print(f"- {teammate.get_full_name()} (ID: {teammate.employee_id})")
                return

        print(f"No manager found with ID {man_id}.")

    @classmethod
    def remove_manager(cls, man_id, new_manager_id=None):
        pass

    @classmethod
    def remove_teammate(cls, man_id, teammate_id):
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

