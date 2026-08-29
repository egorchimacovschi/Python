#class variables = shared among all instancesof a class defined out of the constructor

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.age = age
        self.name = name
        Student.num_students += 1

student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)

print(student1.name)
print(student2.age)
print(student1.class_year)
print(Student.num_students)