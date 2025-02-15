
let shoppingList = [
    { product: "Молоко", quantity: 2, bought: false },
    { product: "Хлеб", quantity: 1, bought: true },
    { product: "Яйца", quantity: 12, bought: false },
    { product: "Масло", quantity: 1, bought: true }
  ];
  
 
  function printShoppingList(list) {
    let notBought = list.filter(item => !item.bought);
    let bought = list.filter(item => item.bought);
  
    console.log("Не купленные:");
    notBought.forEach(item => {
      console.log(`${item.product} - ${item.quantity}`);
    });
  
    console.log("\nКупленные:");
    bought.forEach(item => {
      console.log(`${item.product} - ${item.quantity}`);
    });
  }
  
  
  function addPurchase(list, product, quantity) {
    let found = list.find(item => item.product === product);
    if (found) {
      found.quantity += quantity; 
    } else {
      list.push({ product: product, quantity: quantity, bought: false });
    }
  }
  

  function buyProduct(list, product) {
    let item = list.find(item => item.product === product);
    if (item) {
      item.bought = true; 
    }
  }

  printShoppingList(shoppingList);
  addPurchase(shoppingList, "Молоко", 1); 
  buyProduct(shoppingList, "Яйца"); 
  printShoppingList(shoppingList);
  

  let receipt = [
    { product: "Молоко", quantity: 2, price: 50 },
    { product: "Хлеб", quantity: 1, price: 30 },
    { product: "Яйца", quantity: 12, price: 60 },
    { product: "Масло", quantity: 1, price: 200 }
  ];
  
  function printReceipt(receipt) {
    console.log("Чек:");
    receipt.forEach(item => {
      console.log(`${item.product} - ${item.quantity} шт. по ${item.price} руб.`);
    });
  }
  
  function getTotalAmount(receipt) {
    return receipt.reduce((total, item) => total + (item.quantity * item.price), 0);
  }
  
  function getMostExpensiveItem(receipt) {
    return receipt.reduce((mostExpensive, item) => {
      return (item.quantity * item.price) > (mostExpensive.quantity * mostExpensive.price) ? item : mostExpensive;
    });
  }
  
  function getAveragePrice(receipt) {
    let totalItems = receipt.reduce((total, item) => total + item.quantity, 0);
    let totalPrice = getTotalAmount(receipt);
    return totalPrice / totalItems;
  }
  
  printReceipt(receipt);
  console.log(`Общая сумма: ${getTotalAmount(receipt)} руб.`);
  let mostExpensive = getMostExpensiveItem(receipt);
  console.log(`Самая дорогая покупка: ${mostExpensive.product} за ${mostExpensive.price} руб.`);
  console.log(`Средняя стоимость товара: ${getAveragePrice(receipt).toFixed(2)} руб.`);
  