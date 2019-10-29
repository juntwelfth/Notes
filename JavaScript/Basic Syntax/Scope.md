# Scope

## let

- 지역 변수
- `Block Scope`
- 함수내에서 쓰이면 함수 밖에선 쓰지 못한다.
- 반복문내에서 쓰이면 반복문 밖에서 쓰지 못한다.

```js
let greeting = 'Hello';

function greetSomeone() {
  let firstName = 'Josh';
  return greeting + ' ' + firstName;
}

greetSomeone(); // => 'Hello Josh'
firstName; // => ReferenceError
```

전역변수와 지역변수는 다른 메모리 공간에 저장된다.

## var

- 지역변수
- `Function Scope`
- 반복문에서 선언된 변수는 함수 밖에서 쓸 수 있다.
- var를 사용한 재 정의시 에러가 나지 않는다.

```js
function greetSomeone(firstName) {
  var time = 'night';
  if(time === 'night') {
    var greeting = 'Good Night';
  }
  return greeting + ' ' + firstName;
}
greetSomeone('Steve');

function greetSomeone(firstName) {
  let time = 'night';
  if(time === 'night') {
    let greeting = 'Hello';
  }
  return greeting + ' ' + firstName;
}
greetSomeone('Steve');
```

`var` 키워드로 선언한 변수는 `function scope`를 가지고 있기 때문에 에러가 나지 않는다.

`let` 키워드로 선언한 변수는 `block scope`를 가지고 있기 때문에 에러가 난다.

```js
var myName = "Paul";
console.log(window.myName); // Paul

function foo() {
  console.log('bar');
}

console.log(foo === window.foo); // true
```

`var` 키워드로 선언된 변수는 window객체와 연결된다.

전역변수에 너무 많은 변수를 저장하지 말자.

## const

- 상수
- `Block Scope`

```js
[1, 3, 5].map(function(currentElement, index, array) {
  return currentElement * 2;
});
// [2, 6, 10]
```

## 선언없는 변수

- 절대 금지

```js
function showAge() {
  // age는 전역 변수로 취급됩니다
  age = 90;
  console.log(age);
}
showAge(); // 90
console.log(age); // 90
```

이러한 실수를 방지하기 위해 strict 모드가 존재한다.

```js
'use strict';

function showAge() {
  age = 90; // 여기서 에러가 발생합니다!
  console.log(age);
}
showAge(); // 90
console.log(age); // 90
```
