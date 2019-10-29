# Function Methods

## Bind

- `bind()`
- call, apply와 다르게 함수를 바로 실행시키지 않고, this 값이 바인딩된 함수를 리턴한다.

```js
function add(x, y) {
  this.val = x + y;
  console.log(this.val);
}

let obj = {val: 0};

let boundFn = add.bind(obj, 2, 8);  // boundFn은 함수
boundFn();  // 10, add함수는 여기서 실행된다.
```

## Prototype의 의미

- 인스턴스가 생성(instantiation)될 때 원형(original form), 즉 프로토타입(prototype)의 모양대로 인스턴스가 생성
- 인스턴스의 메소드는 Object.prototype.something으로 표현

> prototype === 원형

## Class

- JavaScript는 prototype 기반 언어
- prototype을 기반으로 객체 지향 프로그래밍(OOP)를 흉내냄
- 문법적인 편의로 class란 keyword를 도입 (ES6)

## Understanding Prototype

```js
function Car(model, brand) {
  this.model = model;
  this.brand = brand;
}

var spark = new Car("spark", "chevrolet");
var avante = new Car("avante", "hyundai");

function Car(model, brand) {
  this.model = model;
  this.brand = brand;
}

Car.prototype.ride = function() {
  console.log("vroooom! " + this.model)
};

var spark = new Car("spark", "chevrolet");
spark.ride(); // "vrooom! spark"
var avante = new Car("avante", "hyundai");
avante.ride(); // "vrooom! avante"
```

## Extending Prototype

- JavaScript에서 기본적으로 제공되는 객체에 사용자 정의 메소드를 직접 추가할 수 있음 (*그러나, 추천하지 않음*)
- 메소드 확장은, 다른 코드와 충돌을 일으킬 수 있음

```js
Number.prototype.invert = function() {
  return -(this)
}

var num = 5;
num.invert(); // -5

Array.prototype.pluck = function(propertyName) {
  return this.map(function(el) {
    return el[propertyName];
  });
}

var arr = [
  { first: "hoyong", last: "lee" },
  { first: "johnny", last: "koo" }
];
arr.pluck("first"); // ["hoyong", "ilmo"]
```
