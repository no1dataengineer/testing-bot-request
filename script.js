// Bad JavaScript code example

var x = 10; // What is x?
let y = 20; // What is y?
const z = 30; // What is z?

function f(a, b) {
    var result;
    if (a > b) {
        result = a + b;
    } else if (a < b) {
        result = a - b;
    } else {
        result = a * b;
    }
    return result; // This function does too many things
}

function doStuff() {
    // No comments or meaningful variable names
    for (var i = 0; i < 10; i++) {
        console.log(i);
        if (i % 2 == 0) {
            console.log("Even");
        } else {
            console.log("Odd");
        }
    }
}

function weirdFunction(x) {
    var a = [1, 2, 3, 4, 5];
    for (var i = 0; i < a.length; i++) {
        console.log(a[i]);
    }
    a.forEach(function(item) {
        console.log(item);
    });
    return x; // Returns the input without doing anything useful
}

doStuff(); // Calling function without purpose
