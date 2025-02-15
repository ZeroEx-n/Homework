let age = prompt("Введите ваш возраст:");

if (age >= 0 && age <= 2) {
    alert("Вы ребенок");
} else if (age >= 12 && age <= 18) {
    alert("Вы подросток");
} else if (age >= 18 && age <= 60) {
    alert("Вы взрослый");
} else if (age > 60) {
    alert("Вы пенсионер");
} else {
    alert("Некорректный возраст");
}

let num = prompt("Введите число от 0 до 9:");

switch (num) {
    case "1":
        alert("!");
        break;
    case "2":
        alert("@");
        break;
    case "3":
        alert("#");
        break;
    case "4":
        alert("$");
        break;
    case "5":
        alert("%");
        break;
    case "6":
        alert("^");
        break;
    case "7":
        alert("&");
        break;
    case "8":
        alert("*");
        break;
    case "9":
        alert("(");
        break;
    case "0":
        alert(")");
        break;
    default:
        alert("Некорректный ввод");
}

let number = prompt("Введите трехзначное число:");

let digits = number.split(""); 

if (digits[0] === digits[1] || digits[0] === digits[2] || digits[1] === digits[2]) {
    alert("В числе есть одинаковые цифры");
} else {
    alert("В числе нет одинаковых цифр");
}

let year = prompt("Введите год:");

if ((year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0)) {
    alert("Год високосный");
} else {
    alert("Год не високосный");
}

let nyumber = prompt("Введите пятиразрядное число:");

let strNyumber = nyumber.toString();
if (strNyumber === strNyumber.split("").reverse().join("")) {
    alert("Число является палиндромом");
} else {
    alert("Число не является палиндромом");
}

let usd = prompt("Введите количество USD:");
let currency = prompt("Выберите валюту для перевода (EUR, UAN, AZN):");

let rate;
if (currency === "EUR") {
    rate = 0.85; 
} else if (currency === "UAN") {
    rate = 26.5; 
} else if (currency === "AZN") {
    rate = 1.7; 
} else {
    alert("Некорректная валюта");
    throw new Error("Некорректная валюта");
}

let convertedAmount = usd * rate;
alert(`Сумма в ${currency}: ${convertedAmount}`);


let price = prompt("Введите сумму покупки:");

let discount;
if (price >= 200 && price < 300) {
    discount = 0.03;
} else if (price >= 300 && price < 500) {
    discount = 0.05;
} else if (price >= 500) {
    discount = 0.07;
} else {
    discount = 0;
}

let finalPrice = price - (price * discount);
alert(`Сумма к оплате со скидкой: ${finalPrice}`);

let circumference = prompt("Введите длину окружности:");
let perimeter = prompt("Введите периметр квадрата:");

let radius = circumference / (2 * Math.PI);
let side = perimeter / 4;

if (radius * 2 <= side) {
    alert("Окружность может поместиться в квадрат");
} else {
    alert("Окружность не может поместиться в квадрат");
}


let score = 0;

let answer1 = prompt("Вопрос 1: Какой язык программирования используется для веб-разработки?\n1) Java\n2) Python\n3) JavaScript");
if (answer1 === "3") score += 2;

let answer2 = prompt("Вопрос 2: Сколько будет 2 + 2?\n1) 4\n2) 5\n3) 6");
if (answer2 === "1") score += 2;

let answer3 = prompt("Вопрос 3: Кто написал 'Гарри Поттера'?\n1) Дж. К. Роулинг\n2) Лев Толстой\n3) А. С. Пушкин");
if (answer3 === "1") score += 2;

alert(`Вы набрали ${score} баллов`);

let day = parseInt(prompt("Введите день:"));
let month = parseInt(prompt("Введите месяц:"));
let yyear = parseInt(prompt("Введите год:"));

let date = new Date(yyear, month - 1, day); 

date.setDate(date.getDate() + 1); 

alert(`Следующая дата: ${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}`);
