# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования реализуйте класс CoffeeMachine (содержит информацию о кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.
class Device:
    def __init__(self, name, company, device_class):
        self.name = name
        self.company = company
        self.device_class = device_class

    def get_info(self):
        return f"Устройство: {self.name}, Компания: {self.company}, Класс: {self.device_class}"

class CoffeeMachine(Device):
    def __init__(self, name, company, device_class, coffee_type):
        super().__init__(name, company, device_class)
        self.coffee_type = coffee_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип кофе: {self.coffee_type}"

    def make_coffee(self):
        return f"{self.name} готовит {self.coffee_type}"

class Blender(Device):
    def __init__(self, name, company, device_class, bowl_capacity, nozzles):
        super().__init__(name, company, device_class)
        self.bowl_capacity = bowl_capacity 
        self.nozzles = nozzles 

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Чаша: {self.bowl_capacity} литра, Насадки: {self.nozzles}"

    def blend(self):
        return f"{self.name} размельчает ингредиенты"

class MeatGrinder(Device):
    def __init__(self, name, company, device_class, power, modes):
        super().__init__(name, company, device_class)
        self.power = power 
        self.modes = modes 

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Мощность: {self.power} Вт, Режимы: {self.modes}"

    def grind(self):
        return f"{self.name} перемалывает мясо"


coffee_machine = CoffeeMachine("Latte Maker", "Delonghi", "Кофемашина", "Латте")
blender = Blender("Smoothie Pro", "Philips", "Блендер", 2.0, 3)
meat_grinder = MeatGrinder("Power Grind", "Bosch", "Мясорубка", 1000, 2)

print(coffee_machine.get_info())
print(coffee_machine.make_coffee())

print(blender.get_info())
print(blender.blend())

print(meat_grinder.get_info())
print(meat_grinder.grind())

    
# Задание 2
# Создайте класс Ship, который содержит информацию о кораблях. С помощью механизма наследования реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.
class Ship:
    def __init__(self, name, displacement, max_speed, armament):
        self.name = name
        self.displacement = displacement
        self.max_speed = max_speed
        self.armament = armament

    def get_info(self):
        return f"Корабль: {self.name}, Водоизмещение: {self.displacement} тонн, Максимальная скорость: {self.max_speed} узлов, Оружие: {self.armament}"

    def fire_weapons(self):
        return f"{self.name} открывает огонь с вооружения!"

class Frigate(Ship):
    def __init__(self, name, displacement, max_speed, armament, radar_type):
        super().__init__(name, displacement, max_speed, armament)
        self.radar_type = radar_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип радара: {self.radar_type}"

    def perform_maneuver(self):
        return f"{self.name} выполняет маневр для уклонения от атаки!"

class Destroyer(Ship):
    def __init__(self, name, displacement, max_speed, armament, torpedo_count):
        super().__init__(name, displacement, max_speed, armament)
        self.torpedo_count = torpedo_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Количество торпед: {self.torpedo_count}"

    def launch_torpedo(self):
        if self.torpedo_count > 0:
            self.torpedo_count -= 1
            return f"{self.name} запускает торпеду!"
        else:
            return f"{self.name} не имеет торпед для запуска."

class Cruiser(Ship):
    def __init__(self, name, displacement, max_speed, armament, missile_count):
        super().__init__(name, displacement, max_speed, armament)
        self.missile_count = missile_count

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Количество ракет: {self.missile_count}"

    def launch_missile(self):
        if self.missile_count > 0:
            self.missile_count -= 1
            return f"{self.name} запускает ракету!"
        else:
            return f"{self.name} не имеет ракет для запуска."

frigate = Frigate("Фрегат Север", 5000, 30, "Пушки, Ракеты", "AESA Radar")
destroyer = Destroyer("Эсминец Гром", 8000, 32, "Пушки, Торпеды", 10)
cruiser = Cruiser("Крейсер Звезда", 12000, 28, "Пушки, Ракеты", 15)

print(f"Информация о фрегате: {frigate.get_info()}")
print(f"Информация об эсминце: {destroyer.get_info()}")
print(f"Информация о крейсере: {cruiser.get_info()}")

print(frigate.perform_maneuver())
print(destroyer.launch_torpedo())
print(cruiser.launch_missile())


