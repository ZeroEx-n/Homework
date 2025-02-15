#№1
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def display_info(self):
#         print(f"Name: {self.name}")
# class Employee(Person):

#     def work(self):
#         print(f"{self.name} works")

# tom = Employee("Tom")
# print(tom.name)
# tom.display_info()
# tom.work()



# class Parent:
#     def info(self):
#         return "I'm a parent"
# class Child(Parent):
#     def info(self):
#         return "I'm a child"

# obj = Child()
# print(obj.info())
        
#№2
# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         return f"Hello, my name is {self.name}"


# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def greet(self):
#         return f"Hi I'm {self.name}, and I'm {self.age} years old"


# parent = Parent("John")
# print(parent.greet())

# child = Child("Jane", 10)
# print(child.greet())
#№3
# class Parent:
#     def greet(self):
#         return "Hello from Parent"

# class Child(Parent):
#     def greet(self):
#         parent_greeting = super().greet()
#         return f"{parent_greeting} And hello from Child"

# obj = Child()
# print(obj.greet())
#№3
# class Employee:
#     def do(self):
#         print("Employee works")
# class Student:
#     def do(self):
#         print("Student studies")

# class WorkingStudent(Employee, Student):
#     pass

# tom = WorkingStudent()
# tom.do()
# print(WorkingStudent.mro())
