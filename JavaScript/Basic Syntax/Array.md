# Array

Class: Basic Syntax
Created: Sep 23, 2019 2:34 PM
Edited: Oct 10, 2019 1:37 PM
Reviewed: No

[JavaScript](./JavaScript-22d52fd4-fa33-4035-9899-e1f4222518ae.csv)

---

---

# Array Methods

---

## Array.isArray(obj)

- arguments : 검사할 객체
- return value : `true` / `false`
- 검사할 객체가 배열이면 `true`, 아니면 `false`를 반환

    Array.isArray([]); // true
    Array.isArray([1]); // true
    Array.isArray(); // false
    Array.isArray('Array'); // false
    Array.isArray({}); // false

---

## arr.forEach(callback)

- IMMUTABLE
- arguments : `element`의 길이만큼 반복하는 함수
    - parameters
        - 순서대로 (현재 `element`, 현재 `index`, 배열 그 자체)
- return value : 없음
- element마다 함수를 반복 실행 합니다

    function printArray(currentElement, index, array) {
      console.log(index + ': ' + currentElement);
    }
    
    ['hello', 3, 5].forEach(printArray);
    // 0: hello
    // 1: 3
    // 2: 5

CALLBACK?

`argument`로 넘겨주는 함수(A)

이 함수(A)를 `parameter`로 받는 함수(B)가 callback 함수(A)를 즉시 실행할지, 나중에 실행할 지 결정할 수 있다

    function system(callback) {
      callback(); // 실행 가능한 콜백 함수
    }
    
    function foo() { console.log('실행 가능한 콜백 함수'); }
    system(foo);

---

## arr.map(callback)

- IMMUTABLE
- arguments : `element`의 길이만큼 반복하는 함수
    - `parameters`
        - 순서대로 (현재 `element`, 현재 `index`, 배열 그 자체)
- return value : `callback`이 실행되면서 `return`하는 값들을 모은 새로운 배열
- `callback` 내에서 `return` 필요
- 기존 배열과 동일한 길이를 갖고, 형태가 다른 새로운 배열을 만들 때 유용

    [1, 3, 5].map(function(currentElement, index, array) {
      return currentElement * 2;
    });
    // [2, 6, 10]

---

## arr.filter(callback)

- IMMUTABLE
- arguments : `element`의 길이만큼 반복하는 함수
    - parameters
        - 순서대로 (현재 `element`, 현재 `index`, 배열 그 자체)
- return value : 조건을 통과한 `element`들을 담은 새로운 배열
- `callback` 내에서 `boolean` 형태의 `return` 필요
- 기존 배열에서 조건에 따라 특정 `element`를 걸러낼 때 유용

    [1, 3, 5].filter(function(currentElement, index, array) {
      return currentElement > 1
    });
    // [3, 5]

---

## arr.push(newElement)

- MUTABLE
- arguments : 추가할 `element` (여러 개 가능)
- return value : 추가된 `array`의 길이
- 배열 마지막에 요소를 추가

    ['code', 'states'].push('course'); // ['code', 'states', 'course']
    [1, 3, 5].push(7, 9); // [1, 3, 5, 7, 9]

---

## arr.pop()

- MUTABLE
- return value : 제거된 `element` 반환
- 배열 마지막 요소를 제거

    var arr = ['code', 'states', 'course'];
    arr.pop(); // 'course'
    console.log(arr); // ['code', 'states'];

---

## arr.slice([begin[, end]])

- IMMUTABLE
- arguments : 처음/마지막 `index`
- return value : 새로운 배열 객체 반환
- `index`의 범위만큼 `element`를 추출

    var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
    console.log(animals.slice(2));
    // ["camel", "duck", "elephant"]
    
    console.log(animals.slice(2, 4));
    // ["camel", "duck"]

---

## arr.splice(start[, deleteCount[, item1[, item2[, ...]]]])

- MUTABLE
- arguments
    - 처음 `index`
        - (삭제시) 삭제할 `element`의 갯수
        - (추가시) 배열에 추가할 `element` (여러 개 가능)
- return value : 새로운 배열 객체 반환
- 배열의 내용을 추가 / 삭제할 때 사용

    var myFish = ['angel', 'clown', 'mandarin', 'sturgeon'];
    myFish.splice(2, 0, 'drum'); // 'drum'을 두번째 인덱스에 삽입
    // ["angel", "clown", "drum", "mandarin", "sturgeon"]
    
    myFish.splice(2, 1); // 두번째 인덱스에서 하나의 항목('drum')을 삭제
    // ["angel", "clown", "mandarin", "sturgeon"]

---

## arr.reduce(callback[, initialValue])

- IMMUTABLE
- arguments : `element`의 길이만큼 반복하는 함수, 초기값
    - parameters
        - 순서대로 (누적값 `accumulator`, 현재값 `currentValue`, 현재 `index` , 원본배열)
- return value : 최종 누적값
- 모든 `element`의 계산을 누적해 하나의 결과를 리턴할 때 유용

---

## arr.join([separator = ','])

- IMMUTABLE
- arguments : 연결자
- return value : 연결자로 `element`를 연결한 결과 문자열

    var a = ['바람', '비', '불'];
    var myVar1 = a.join();      // myVar1에 '바람,비,불'을 대입
    var myVar2 = a.join(', ');  // myVar2에 '바람, 비, 불'을 대입
    var myVar3 = a.join(' + '); // myVar3에 '바람 + 비 + 불'을 대입
    var myVar4 = a.join('');    // myVar4에 '바람비불'을 대입

---

## arr.indexOf(searchElement)

- IMMUTABLE
- arguments : 배열에서 찾을 `element`
- return value : 배열 내의 요소의 최초의 인덱스. 발견되지 않으면 -1
- element 존재 여부를 파악할 때 유용

    var array = [2, 9, 9];
    array.indexOf(2);     // 0
    array.indexOf(7);     // -1

비슷한 목적을 가진 메소드로는 includes, find가 있음

---

## array.concat(arr)

- 배열에 배열을 추가하는 함수

    let array1 = ['a', 'b', 'c'];
    let array2 = ['d', 'e', 'f'];
    
    console.log(array1.concat(array2));
    // expected output: Array ["a", "b", "c", "d", "e", "f"]

새로운 배열을 만들어낸다.

---

[JavaScript](./JavaScript-22d52fd4-fa33-4035-9899-e1f4222518ae.csv)