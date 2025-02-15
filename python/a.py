class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_on = False
    
    def engen_start(self):
        self.engine_on = True
        print("Двигатель запущен")

    def engen_stop(self):
        self.engine_on = False
        print("Двигатель остновлен")

    def __str__(self):
        return f"Car:{self.year} {self.brand} {self.model}"

if __name__ == '__main__' :
    car1 = Car(brand='BMW',model='M5', year='2021')
    print(car1)
    print(car1.brand)
    print(car1.model)
    print(car1.year)
    print(car1.engine_on)

  
    car1.engen_start()
    print(car1.engine_on)

    car1.engen_stop()
    print(car1.engine_on)
    