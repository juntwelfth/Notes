# String Methods

## indexOf()

- 괄호안에 찾고자하는 문자열을 넣어주자.
- 찾으면 찾은 위치를 알려준다.
- 못찾으면 -1을 반환한다.

```js
'Blue Whale'.indexOf('Blue');        // 0
'Blue Whale'.indexOf('blue');        // -1
'Blue Whale'.indexOf('Whale');       // 5
'Blue Whale Whale'.indexOf('Whale'); // 5

'canal'.lastIndexOf('a');
```

`lastIndexOf()`는 뒤에서부터 찾는다.

## includes()

- 하나의 문자열이 다른 문자열에 포함되어 있는지를 판별하고, true 또는 false 로 반환한다.

```js
let myName = 'Junil Seo';

let lastName = 'Seo';

myName.includes(lastName)    // true

'Junil is hungry'.includes('is')       // true
'Junil is hungry'.includes('Jiyoung')  // false
```

## split()

- 주어진 기준에 따라 문자열을 나눠 배열로 반환한다.

```js
let str = 'Hello from the other side';
console.log(str.split(' '));
// ['Hello', 'from', 'the', 'other', 'side']
```

CSV파일을 불러올 때 유용함

## substring(start, end)

- 시작 `index` (포함), 끝 `index` (포함하지 않음)
- 시작과 끝 index 사이의 문자열을 반환한다.

```js
let result = 'Mozilla'.substring(1, 3);

console.log(result);
// 'oz'
```

## arr.push(newElement)

- MUTABLE
- arguments : 추가할 `element` (여러 개 가능)
- return value : 추가된 `array`의 길이
- 배열 마지막에 요소를 추가

```js
['code', 'states'].push('course'); // ['code', 'states', 'course']
[1, 3, 5].push(7, 9); // [1, 3, 5, 7, 9]
```

## arr.pop()

- MUTABLE
- return value : 제거된 `element` 반환
- 배열 마지막 요소를 제거

```js
var arr = ['code', 'states', 'course'];
arr.pop(); // 'course'
console.log(arr); // ['code', 'states'];
```

## arr.slice([begin[, end]])

- IMMUTABLE
- arguments : 처음/마지막 `index`
- return value : 새로운 배열 객체 반환
- `index`의 범위만큼 `element`를 추출

```js
var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
console.log(animals.slice(2));
// ["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
// ["camel", "duck"]
```

## arr.splice(start[, deleteCount[, item1[, item2[, ...]]]])

- MUTABLE
- arguments
  - 처음 `index`
    - (삭제시) 삭제할 `element`의 갯수
    - (추가시) 배열에 추가할 `element` (여러 개 가능)
- return value : 새로운 배열 객체 반환
- 배열의 내용을 추가 / 삭제할 때 사용

```js
var myFish = ['angel', 'clown', 'mandarin', 'sturgeon'];
myFish.splice(2, 0, 'drum'); // 'drum'을 두번째 인덱스에 삽입
// ["angel", "clown", "drum", "mandarin", "sturgeon"]

myFish.splice(2, 1); // 두번째 인덱스에서 하나의 항목('drum')을 삭제
// ["angel", "clown", "mandarin", "sturgeon"]
```

## arr.reduce(callback[, initialValue])

- IMMUTABLE
- arguments : `element`의 길이만큼 반복하는 함수, 초기값
  - parameters
    - 순서대로 (누적값 `accumulator`, 현재값 `currentValue`, 현재 `index` , 원본배열)
- return value : 최종 누적값
- 모든 `element`의 계산을 누적해 하나의 결과를 리턴할 때 유용

## arr.join([separator = ','])

- IMMUTABLE
- arguments : 연결자
- return value : 연결자로 `element`를 연결한 결과 문자열

```js
var a = ['바람', '비', '불'];
var myVar1 = a.join();      // myVar1에 '바람,비,불'을 대입
var myVar2 = a.join(', ');  // myVar2에 '바람, 비, 불'을 대입
var myVar3 = a.join(' + '); // myVar3에 '바람 + 비 + 불'을 대입
var myVar4 = a.join('');    // myVar4에 '바람비불'을 대입
```

## arr.indexOf(searchElement)

- IMMUTABLE
- arguments : 배열에서 찾을 `element`
- return value : 배열 내의 요소의 최초의 인덱스. 발견되지 않으면 -1
- element 존재 여부를 파악할 때 유용

```js
var array = [2, 9, 9];
array.indexOf(2);     // 0
array.indexOf(7);     // -1
```

비슷한 목적을 가진 메소드로는 includes, find가 있음

## array.concat(arr)

- 배열에 배열을 추가하는 함수

```js
let array1 = ['a', 'b', 'c'];
let array2 = ['d', 'e', 'f'];

console.log(array1.concat(array2));
// expected output: Array ["a", "b", "c", "d", "e", "f"]
```

새로운 배열을 만들어낸다.
