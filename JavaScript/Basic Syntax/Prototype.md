# Prototype

## Array.something() 과 Array.prototype.something()

- `Array.something()`는 Array 클래스에서만 작동
- `Array.prototype.something()`는 Array 인스턴스에서만 작동

```js
var arr = [1,2,3,4];
arr.isArray(); // does it works?
Array.map(function(current, index) {
  return current;
}); // does it works?
```

보다시피 `arr.isArray()`, `Array.map`은 에러가 발생한다.

```js
var arr = [1,2,3,4]; // arr is an instance of Array
// same as
var arr = new Array(1,2,3,4);
```

`var arr = [1, 2, 3, 4]` 는
`var arr = new Array(1, 2, 3, 4)` 와 동일하다.

## Prototype의 의미

- 인스턴스가 생성(instantiation)될 때 원형(original form), 즉 프로토타입(prototype)의 모양대로 인스턴스가 생성
- 인스턴스의 메소드는 Object.prototype.something으로 표현

prototype === 원형

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
