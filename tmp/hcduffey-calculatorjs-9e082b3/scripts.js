let total = 0;
let currentNumber = 0;
let firstNumber = 0; 
let operation = null;

function performOperation(operation, firstNumber, secondNumber) {
    switch(operation) {
        case "+": return(firstNumber + secondNumber);
        case "-": return(firstNumber - secondNumber);
        case "%": return(Math.floor(firstNumber / secondNumber));
        case "*": return(firstNumber * secondNumber);
    }
}

let display = document.querySelector('.display');
display.innerText = total;

let buttonListener = document.querySelector(".container");

buttonListener.addEventListener("click", function(event) {
    switch(event.target.innerText) {
        case "C":
            currentNumber = 0;
            operation = null;
            total = 0;
            display.innerText = total;
            break;

        case "←":
            currentNumber = Math.floor(currentNumber/10);
            display.innerText = currentNumber;
            break;

        case "=": 
            if(operation) {
                total = performOperation(operation, total, currentNumber);
            }
            else {
                total = currentNumber;
            }
            currentNumber = 0;
            operation = null;
            display.innerText = total;
            break;

        case "+":
        case "-":
        case "*":
        case "%":    
            if(operation) {
                total = performOperation(operation, total, currentNumber);
            }
            else if(total === 0) {
                total = currentNumber;
            }
            operation = event.target.innerText;
            currentNumber = 0;
            display.innerText = total;
            break;
            
        case "0":
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        case "7":  
        case "8":
        case "9":          
            let number = Number.parseInt(event.target.innerText);
            currentNumber = (currentNumber * 10) + number;
            display.innerText = currentNumber;
            break;

        default:         
            display.innerText = currentNumber;
    } 
});
