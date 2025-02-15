class Smartphone:
    def __init__(self, model, manufacturer, ram, storage, screen_size, price):
        self.model = model
        self.manufacturer = manufacturer
        self.ram = ram
        self.storage = storage
        self.screen_size = screen_size
        self.price = price

    def input_data(self):
        self.model = input("Введите модель смартфона: ")
        self.manufacturer = input("Введите производителя смартфона: ")
        self.ram = int(input("Введите объем оперативной памяти (ГБ): "))
        self.storage = int(input("Введите объем встроенной памяти (ГБ): "))
        self.screen_size = float(input("Введите размер экрана (дюймы): "))
        self.price = float(input("Введите цену (в тенге): "))

    def output_data(self):
        print(f"Модель: {self.model}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Оперативная память: {self.ram} ГБ")
        print(f"Встроенная память: {self.storage} ГБ")
        print(f"Размер экрана: {self.screen_size} дюймов")
        print(f"Цена: {self.price} тенге")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        print(f"Цена со скидкой: {self.price:.2f} тенге")

smartphone = Smartphone("iPhone 16 Pro Max", "Apple", 8, 256, 6.9, 1229990 )
smartphone.output_data()
smartphone.apply_discount(10)

class Film:
    def __init__(self, title, year, director, genre, duration, rating):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def input_data(self):
        self.title = input("Введите название фильма: ")
        self.year = int(input("Введите год выпуска фильма: "))
        self.director = input("Введите имя режиссера: ")
        self.genre = input("Введите жанр фильма: ")
        self.duration = int(input("Введите продолжительность фильма (в минутах): "))
        self.rating = float(input("Введите рейтинг фильма: "))

    def output_data(self):
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Режиссер: {self.director}")
        print(f"Жанр: {self.genre}")
        print(f"Продолжительность: {self.duration} минут")
        print(f"Рейтинг: {self.rating}")

    def total_duration(self, films):
        total_time = sum(film.duration for film in films)
        hours = total_time // 60
        minutes = total_time % 60
        print(f"Общее время просмотра {len(films)} фильмов: {hours} часов и {minutes} минут")


film1 = Film("Inception", 2010, "Christopher Nolan", "Sci-Fi", 148, 8.8)
film2 = Film("The Matrix", 1999, "Wachowskis", "Action", 136, 8.7)

film1.output_data()
film2.output_data()
film1.total_duration([film1, film2])

class University:
    def __init__(self, name, year_founded, country, city, num_students, num_teachers):
        self.name = name
        self.year_founded = year_founded
        self.country = country
        self.city = city
        self.num_students = num_students
        self.num_teachers = num_teachers

    def input_data(self):
        self.name = input("Введите название университета: ")
        self.year_founded = int(input("Введите год основания университета: "))
        self.country = input("Введите страну расположения университета: ")
        self.city = input("Введите город расположения университета: ")
        self.num_students = int(input("Введите количество студентов: "))
        self.num_teachers = int(input("Введите количество преподавателей: "))

    def output_data(self):
        print(f"Название: {self.name}")
        print(f"Год основания: {self.year_founded}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Количество студентов: {self.num_students}")
        print(f"Количество преподавателей: {self.num_teachers}")

    def student_teacher_ratio(self):
        if self.num_teachers == 0:
            print("Количество преподавателей не может быть равно нулю.")
        else:
            ratio = self.num_students / self.num_teachers
            print(f"Среднее количество студентов на одного преподавателя: {ratio:.2f}")

university = University("Нархоз", 1755, "Казахстан", "Алмата", 40000, 5000)
university.output_data()
university.student_teacher_ratio()
