# Parameter

## ...args

- ES6
- Rest Parameter

```js
const getMaxNum = (...nums) => {
  return nums.reduce((acc, current) => {
    if(acc > current) {
      return acc;
    } else {
      return current;
    }
  });
}

getMaxNum(3, 5, 8, 10);  // 10
```

여러개의 매개변수를 `...nums`로 퉁칠 수 있다.

## arguments

- ES5

```js
const getMaxNum = (arguments) => {
  console.log(arguments);    // {0:3, 1:5, 2:8, 3:10}   <- 유사배열
}

getMaxNum(3, 5, 8, 10);
```

유사배열은 배열메소드를 사용할 수 없다.

## firstArg, secondArg, thirdArg

- 매개변수에 순서를 줄 수 있다.

```js
const returnFirstArg = firstArg => {
  return firstArg;
}

returnFirstArg("first", "second", "third");    // "first"

const returnSecondArg = (firstArg, secondArg) => {
  return secondArg;
}

const returnSecondArg("only give first arg")   // undefined

function returnAllArgs(...args) {
  let argumentsText = '';

  for (let i = 0; i < args.length; i++) {
    argumentsText += args[i];
  }
  
  return argumentsText;
}

returnAllArgs("first", "second", "third")      // "firstsecondthird"
```
