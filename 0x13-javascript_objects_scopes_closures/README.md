![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Javascript objects scopes and  closures

![meme](./you-get-a-proto.jpeg)

## About
JavaScript is a powerful language with many features, and some of its most important concepts include objects, closures, and scopes. Objects are one of the primary building blocks of JavaScript, and they allow you to store data and functions together in a single entity. Closures are another fundamental concept that allows functions to "remember" their surrounding state, even after they have been called and returned. Finally, scopes define the context in which variables and functions are accessible within your code, and understanding them is critical to writing efficient and effective JavaScript code. Together, these concepts form the backbone of the language and are essential for any developer looking to master JavaScript. Let's have a look at all of these confusing javascript principles in detail, and get lost in the callback hell ... prototype chain.

## Resources
__Read or watch__
1. [Javascript objects basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
2. [Object oriented Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
3. [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
4. [super -ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
5. [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
6. [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
7. [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
8. [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
9. [this/self](https://alistapart.com/article/getoutbindingsituations/)
10. [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following  __Without the help of Google__

* [X] How to create an object in JavaScript
* [X] What ```this``` means
* [X] What undefined means
* [X] Why the variable type and scope is important
* [X] What is a closure
* [X] What is a prototype
* [X] How to inherit an object from another

## Quiz
[Quizes](./quiz.md)

## Tasks :page_with_curl:

* **0. Rectangle #0**
  * [0-rectangle.js](./0-rectangle.js): JavaScript script that defines an empty
  class `Rectangle`.

* **1. Rectangle #1**
  * [1-rectangle.js](./1-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [0-rectangle.js](./0-rectangle.js) with:
    * Constructor that initializes instance attributes `width` and `height` with
    given parameters `w` and `h`.

* **2. Rectangle #2**
  * [2-rectangle.js](./2-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [1-rectangle.js](./1-rectangle.js) with:
    * If provided `w` and `h` are less than or equal to `0`, creates an empty object.

* **3. Rectangle #3**
  * [3-rectangle.js](./3-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [3-rectangle.js](./3-rectangle.js) with:
    * Instance method `print()` that prints the rectangle using the `X` character.

* **4. Rectangle #4**
  * [4-rectangle.js](./4-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [4-rectangle.js](./4-rectangle.js) with:
    * Instance method `rotate()` that swaps the `width` and `height` of the `Rectangle`.
    * Instance method `double()` that multiplies the `width` and `height` of the
    `Rectangle` by `2`.

* **5. Square #0**
  * [5-square.js](./5-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`.
    * Constructor takes one argument `size`.

* **6. Square #1**
  * [6-square.js](./6-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`. Builds on [5-square.js](./5-square.js) with:
    * Instance method `charPrint(c)` that prints the `Square` using the character
    `c`.
    * If `c` is `undefined`, uses the character `X`.

* **7. Occurrences**
  * [7-occurrences.js](./7-occurrences.js): JavaScript function that returns the
  number of occurrences in a list.

* **8. Esrever**
  * [8-esrever.js](./8-esrever.js): JavaScript function that reverses a list.

* **9. Log me**
  * [9-logme.js](./9-logme.js): JavaScript function that prints the number of
  arguments already printed as well as the new argument value.
  * Output: `<number arguments already printed>: <current argument value>`

* **10. Number conversion**
  * [10-converter.js](./10-converter.js): JavaScript function that converts a number
  from base 10 to another base passed as argument.

* **11. Factor index**
  * [100-map.js](./100-map.js): JavaScript script that imports an array and creates
  a new array with each value equal to the value of initial list times the index of
  the new list.
  * Prints both the initial and new list.

* **12. Sorted occurences**
  * [101-sorted.js](./101-sorted.js): JavaScript script that imports a dictionary
  of occurrences by user ID and computes a new dictionary of user ID's by occurrences.
  * Prints the new dictionary.

* **13. Concat files**
  * [102-concat.js](./102-concat.js)
