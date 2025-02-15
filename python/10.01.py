class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")
    def __del__(self):
        print("Deleted person with name:", self.name)
    def say_hello(self):
        print("Hello")
    def say(self,message):
        print(message)
tom = Person("Tom", 22)
tom.display_info()

bob = Person("Bob", 44)
bob.display_info()
tom.say
tom.say_hello()


print(tom.name)
print(bob.name)
tom.company = "Microsoft"
print(tom.company)


