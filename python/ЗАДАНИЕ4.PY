class Drob:
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"{self.num1} , {self.num2}"
        
    def delenie(self):
        return self.num1 / self.num2
    def plus(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def ymnojit(self):
        return self.num1 * self.num2
    
    
        
ddd1 = Drob(25,5)


print(ddd1.delenie())
print(ddd1.minus())
print(ddd1.plus())
print(ddd1.ymnojit())

