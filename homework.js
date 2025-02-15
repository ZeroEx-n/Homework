let car = {
    manufacturer: "Toyota",
    model: "Camry",
    year: 2020,
    averageSpeed: 100,
    printInfo: function() {
      console.log(`Производитель: ${this.manufacturer}`);
      console.log(`Модель: ${this.model}`);
      console.log(`Год выпуска: ${this.year}`);
      console.log(`Средняя скорость: ${this.averageSpeed} км/ч`);
    },
  

    calculateTime: function(distance) {
      let timeWithoutBreaks = distance / this.averageSpeed;
      let breaks = Math.floor(timeWithoutBreaks / 4);
      let totalTime = timeWithoutBreaks + breaks; 
      return totalTime;
    }
  };
  
  
  car.printInfo();
  let distance = 500; 
  let time = car.calculateTime(distance);
  console.log(`Необходимое время для преодоления ${distance} км: ${time} часов (с учетом перерывов).`);
  