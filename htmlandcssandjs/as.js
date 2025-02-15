// 1. Запрос имени пользователя и вывод приветствия
let userName = prompt("Введите ваше имя:");
alert("Привет, " + userName + "!");

// 2. Запрос года рождения и расчет возраста
const currentYear = 2025; 
let birthYear = prompt("Введите ваш год рождения:");
let age = currentYear - birthYear;
alert("Вам " + age + " лет.");

// 3. Запрос длины стороны квадрата и вывод периметра
let sideLength = prompt("Введите длину стороны квадрата в сантиметрах:");
let perimeter = sideLength * 4;
alert("Периметр квадрата: " + perimeter + " см.");

// 4. Запрос радиуса окружности и вывод площади
let radius = prompt("Введите радиус окружности в сантиметрах:");
let area = Math.PI * Math.pow(radius, 2);
alert("Площадь окружности: " + area + " квадратных сантиметров.");

// 5. Запрос расстояния между городами и расчет необходимой скорости
let distance = prompt("Введите расстояние между городами в километрах:");
let hours = prompt("За сколько часов вы хотите добраться?");
let speed = distance / hours;
alert("Необходимая скорость: " + speed + " км/ч.");

// 6. Конвертор валют из долларов в евро
const exchangeRate = 0.85; 
let dollars = prompt("Введите сумму в долларах:");
let euros = dollars * exchangeRate;
alert(dollars + " долларов = " + euros + " евро.");

// 7. Подсчет количества файлов, помещающихся на флешку
let flashDriveGb = prompt("Введите объем флешки в Гб:");
const fileSizeMb = 820; 
let flashDriveMb = flashDriveGb * 1024; 
let filesCount = Math.floor(flashDriveMb / fileSizeMb);
alert("На флешку помещается " + filesCount + " файлов размером по 820 Мб.");
