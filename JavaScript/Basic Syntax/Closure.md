# Closure

Class: Basic Syntax
Created: Sep 25, 2019 2:28 AM
Edited: Sep 25, 2019 2:48 AM
Reviewed: No

[JavaScript](./JavaScript-22d52fd4-fa33-4035-9899-e1f4222518ae.csv)

---

---

# Closure

---

## Closure

- 내부함수와 같은 느낌이다.
- 함수 내에서 리턴값으로 함수를 리턴할 수도 있다.
- Local Scope, Function Scope, Global Scope 모두 접근 가능하다.

    function outerFn() {
      let outerVar = 'outer';
      console.log(outerVar);
    
      function innerFn() {
        let innerVar = 'inner';
        console.log(innerVar);
      }
      return innerFn;
    }
    
    outerFn();

리턴값으로 `innerFn()`의 내용이 그대로 리턴된다.

    function outerFn() {
      let outerVar = 'outer';
      console.log(outerVar);
    
      function innerFn() {
        let innerVar = 'inner';
        console.log(innerVar);
      }
      return innerFn;
    }
    
    outerFn()();                // 'outer', 'inner' 둘다 출력한다.
    let innerFn = outerFn();    // 'outer'를 출력하고 innerFn에 innerFn() 함수가 저장된다.
    innerFn();                  // 'inner'만 출력한다.

`outerFn()`은 함수 그 자체를 실행시키고 `outerFn()()`은 내부함수까지 실행시킨다.

전역변수와 지역변수는 다른 메모리 공간에 저장된다.

---

# 예제

---

## 커링

- 함수 하나가 `n`개의 인자를 받는 대신, `n`개의 함수를 만들어 각각 인자를 받게하는 방법

    function adder(x) {
      return function(y) {
        return x + y;
      }
    }
    
    adder(2)(3);  // 5

    let add100 = adder(100);
    add100(2);    // 102
    add100(10);   // 110
    
    let add5 = adder(5);
    add5(7);      // 12
    add5(10);     // 15

특정 `x`의 값을 지정해놓고, 계속 재사용이 가능하다.

    function htmlMaker(tag) {
      let startTag = '<' + tag + '>';
      let endTag = '</' + tag + '>';
      return function(content) {
        return startTag + content + endTag;
      }
    }

    let divMaker = htmlMaker('div');
    divMaker('code'); // <div>code</div>
    divMaker('HI');   // <div>HI</div>
    
    let h1Maker = htmlMaker('h1');
    h1Maker('Jun');   // <h1>Jun</h1>
    h1Maker('Il');    // <h1>Il</h1>

외부함수의 변수가 저장되어 템플릿 함수로도 사용이 가능하다.

---

## 클로저 모듈 패턴

- 변수를 스코프 안쪽에 가두어 함수 밖에서 수정할 수 없게 하는 것

    function makeCounter() {
      let privateCounter = 0;
    
      return {
        increment: function() {
          privateCounter++;
        },
        decrement: () => {
          privateCounter--;
        },
        getValue: () => { 
          return privateCounter; 
        }
      }
    }

    let counter1 = makeCounter();
    counter1.increment();
    counter1.increment();
    counter1.getValue();    // 2
    
    let counter2 = makeCounter();
    counter2.decrement();
    counter2.decrement();
    counter2.decrement();
    counter2.decrement();
    counter2.decrement();
    
    counter2.getValue();    // -5
    
    counter1.getValue();    // 2

---

[JavaScript](./JavaScript-22d52fd4-fa33-4035-9899-e1f4222518ae.csv)