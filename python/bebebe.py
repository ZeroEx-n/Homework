# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.
class Stadion:
    def __init__(self, stadion_name, open_date, country, city, capacity):
        self._stadion_name = stadion_name
        self._open_date = open_date
        self._country = country
        self._city = city
        self._capacity = capacity
    
 
    def get_stadion_name(self):
        return self._stadion_name
    
    def get_open_date(self):
        return self._open_date
    
    def get_country(self):
        return self._country
    
    def get_city(self):
        return self._city
    
    def get_capacity(self):
        return self._capacity
    
    def set_stadion_name(self, name):
        self._stadion_name = name
    
    def set_open_date(self, date):
        self._open_date = date
    
    def set_country(self, country):
        self._country = country
    
    def set_city(self, city):
        self._city = city
    
    def set_capacity(self, capacity):
        self._capacity = capacity
    

    def __str__(self):
        return f"Stadion: {self._stadion_name}, Date: {self._open_date}, Country: {self._country}, City: {self._city}, Capacity: {self._capacity})"

stadion = Stadion("Wembley Stadium", "2007-03-09", "UK", "London", 90000)

print(stadion)