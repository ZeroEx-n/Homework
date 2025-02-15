# class Report:
#     def generate(self):
#         print("Generating report...")

# class Save():
#     def save_to_file(self, filename):
#         with open(filename, 'w') as f:
#             f.write("Report data")







# class Bird:
#     def fly(self):
#         print("Flying")

# class Penguin(Bird):
#     def fly_peng(self):
#         print("Penguins can fly!")




# class Worker:
#     def work(self):
#         pass
# class Eat:
#     def eat(self):
#         pass

# class Programmer(Worker, Eat):
#     def work(self):
#         print("Coding")

#     def eat(self):
#         print("Programmers don’t have time to eat")










#zadanie2 
class Task:
    def __init__(self):
        self.tasks=[]

    def add(self, task):
        self.tasks.append(task)
        print(f"Задача' {task}' добавлена")

    def show(self):
        if not self.tasks:
            print("Список пуст")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}, {task}")

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"Задача '{removed}' удалена")
        else:
            print("Неверный номер задачи")

todo = Task()
todo.add("Выучить Python")
todo.add("Понять SOLID")
todo.show()
todo.remove_task(1)
todo.show()