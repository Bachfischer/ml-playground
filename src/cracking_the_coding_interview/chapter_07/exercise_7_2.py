"""
Call Center:
Imagine you have a call center with three levels of employees: respondent, manager, and director. An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not free or not able to handle it, then the call should be escalated to a director. Design the classes and data structures for this problem. Implement a method dispatchCall() which assigns a call to the first available employee.
"""

class Employee:

    def __init__(self, name):
        self.name = name
        self.free = True

    def is_free(self):
        return self.free

    def handle_call(self, can_handle_himself, escalate_to_manager):
        self.free = False
        print("Employee %s dealing with call" %( self.name))
        if not can_handle_himself:
            escalate_to_manager()
        self.free = True

class Manager:

    def __init__(self, name):
        self.name = name
        self.free = True

    def is_free(self):
        return self.free

    def handle_call(self, can_handle_himself, escalate_to_director):
        self.free = False
        print("Manager %s dealing with call" % (self.name))
        if not can_handle_himself:
            escalate_to_director()
        self.free = True

class Director:

    def __init__(self, name):
        self.name = name
        self.free = True

    def is_free(self):
        return self.free

    def handle_call(self):
        self.free = False
        print("Director %s dealing with call" % (self.name))
        self.free = True

class CallCenter:

    def __init__(self):
        employee1 = Employee("Employee 1")
        employee2 = Employee("Employee 2")
        employee3 = Employee("Employee 3")
        employee4 = Employee("Employee 4")
        employee5 = Employee("Employee 5")

        manager1 = Manager("Manager 1")
        manager2 = Manager("Manager 2")

        director1 = Director("Director 1")

        self.employees = []
        self.employees.append(employee1)
        self.employees.append(employee2)
        self.employees.append(employee3)
        self.employees.append(employee4)
        self.employees.append(employee5)

        self.managers = []
        self.managers.append(manager1)
        self.managers.append(manager2)

        self.directors = []
        self.directors.append(director1)

        for i in range(10):
            if i%2 == 0:
                self.dispatch_call(can_handle_himself=False)
            else:
                self.dispatch_call(can_handle_himself=True)


    def dispatch_call(self, can_handle_himself):
        for employee in self.employees:
            if employee.is_free():
                employee.handle_call(can_handle_himself=can_handle_himself, escalate_to_manager=self.escalate_to_manager)
                break


    def escalate_to_manager(self):
        for manager in self.managers:
            if manager.is_free():
                manager.handle_call(can_handle_himself=False,
                                     escalate_to_director=self.escalate_to_director)
                break


    def escalate_to_director(self):
        for director in self.directors:
            if director.is_free():
                director.handle_call()
                break


def main():
    call_center = CallCenter()


if __name__ == "__main__":
    main()