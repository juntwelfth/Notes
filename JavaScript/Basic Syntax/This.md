# This

## Execution Context

- 코드가 실행되면 전역 메모리 (`Global Memory`)가 생성된다.
- 전역 `Execution Context`가 생성된다.
- 함수가 실행되면 지역 메모리 (`Local Memory`)가 생성된다.
  - Lexical Scope
- `Local Execution Context`가 생성된다.

어떤 함수가 호출되면, Execution Context가 만들어진다.
`Call Stack`에 `push`되고, 함수를 벗어나면 `Call Stack`에서 `pop`된다.

`Scope`별로 생성된다.

`Scope` 내 변수 및 함수 (`Local`, `Global`)가 담기며, 인자와 호출된 근원 (`caller`), `this`가 담긴다.

`Execution Context`의 모습

## this

- 특수한 식별자
- `Execution Context`의 구성 요소 중 하나로, 함수가 실행되는 동안 사용할 수 있다.
- 5가지 예제
    1. Global : window
    2. Function 호출 : window
    3. Method 호출 : 부모 Object
    4. Construction Mode : 인스턴스 객체
    5. `call()`, `apply()` 호출 : `call()`, `apply()`의 첫번째 인자로 전달받은 객체

```js
var name = 'Global Variable';
console.log(this.name);   // "Global Variable"
this.name === window.name // true

function foo() {
  return this.name;  // "Global Variable"
}

foo() === window.name  // true
```

전역으로 선언한 `var`과 `function`의 부모 객체는 `window`이다.

```js
var name = 'Global Variable';

function outer() {
  function inner() {
    console.log(this.name);  // "Global Variable"
  }
  inner();
}

outer();
```

내부 함수에서도 `this`는 `window`이다.

```js
var counter = {
  val = 0,
  increment: function() {
    this.val += 1;
  }
};

counter.increment();
console.log(counter.val);  // 1
counter['increment'];
console.log(counter.val);  // 2
```

객체 내부 함수에서의 `this`는 객체이다. (부모 객체)

```js
var obj = {
  fn: function(a, b) {
    return this;
  }
};

var obj2 = {
  method: obj.fn
};

console.log(obj2.method() === obj2);  // true
console.log(obj.fn() === obj);        // true
```

자바스크립트에서 `this`는 호출된 그 시점의 부모객체를 가리킨다.

```js
function F(v) {
  this.val = v;
}

var f = new F('WooHoo!');

console.log(f.val);    // "WooHoo!"
console.log(val);      // Reference Error

function identify() {
  return this.name.toUpperCase();
}

function speak() {
  var greeting = "Hello, I'm " + identify.call(this);
  console.log(greeting);
}

var me = { name: "Kyle" };
var you = { name: "Reader" };

identify.call(me);    // KYLE
identify.call(you);   // READER
speak.call(me);       // "Hello, I'm KYLE"
speak.call(you);      // "Hello, I'm READER"

var add = function(x, y) {
  this.val = x + y;
}

var obj = {
  val: 0
};

add.apply(obj, [2, 8]);
console.log(obj.val);   // 10
add.call(obj, 2, 8);
console.log(obj.val);   // 10
```

`call`과 `apply`의 첫번째 인자는 `this`이다.
`apply`를 호출할 땐 배열을 넣어야 한다.
첫번째 인자로 객체를 넘겨주기 싫을 땐 null을 쓰자.

```js
function add(x, y) {
  return x + y;
}

add.call(null, 2, 4)     // 6
add.apply(null, [2, 4])  // 6
```

`let arr = [1, 2, 3, 4, 5, 6, 7]` 이러한 배열이 있을 때

`Math.max.apply(null, arr)` 이러한 호출로 `max`값을 얻을 수 있다.
