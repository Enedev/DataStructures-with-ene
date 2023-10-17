function operation(a, b, c) {
    let result;
    if (c === "+") {
        result = a + b;
        } else if (c === "-") {
        result = a - b;
        } else if (c === "*") {
        result = a * b;
        } else if (c === "/") {
        result = a / b;
        }
    return result;
}
  
console.log(operation(2, 3, "+"));
        