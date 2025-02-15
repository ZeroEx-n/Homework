// let lucky = 10

// let user = prompt('U number')

// while(lucky != user){
//   console.log('loose')
  
//   user = prompt('U number')
// }
// console.log('win')

// function checkAge(a){
//     if(a < 18){
//     return false
//     }else{
//         return true
//     }
// }

// let age = prompt('How old are you')
// let result = checkAge(age)
    
// if(result){
//     console.log('Success')
// }else{
//     console.log('Error')}


function sr(a, b) { 
        if (a < b) { 
            return "1 число больше чем число 2"; 
        } 
        if (b < a) { 
            return "2 число больше чем число 1"; 
        } 
        else { 
            return "числа равны"; 
        } 
    } 
     
    let a = prompt("введите 1 число"); 
     
    let b = prompt("введите 2 число"); 
     
    console.log(sr(a, b));

  

function ch(tg) { 
        if (tg % 2 == 0) { 
            console.log("четное"); 
        } 
        else { 
            console.log("нечетное"); 
        } 
     
    } 
    let tg = prompt("введите число"); 
     
    ch(tg)