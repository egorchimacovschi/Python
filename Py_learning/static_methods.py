# static methods = a method thath belong to a class rather than any object from that class (instance)
#                   usually used for genral utility functions


#Instance methods = Best for operations on instance of the class (objects)
#Static methods = Best for utility functions that do not need access to class data


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    #instance method
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

#print(Emplyee.is_valid_position("Manager"))

employee1 = Employee("Eugen", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("SpongeBob", "Cook")

print(employee1.get_info())
Employee.is_valid_position(employee1.position)
