# JSON

## What is JSON

- JavaScript Object Notation
- 브라우저와 서버사이에서 오고가는 데이터의 형식이다.

## JSON.stringify(value, replacer, space)

- value(필수): JSON 문자열로 변환할 값이다.(배열, 객체, 또는 숫자, 문자 등이 될 수 있다.)
- replacer(선택): 함수 또는 배열이 될 수 있다. 이 값이 null 이거나 제공되지 않으면, 객체의 모든 속성들이 JSON 문자열 결과에 포함된다.
- 특징
  - string
    - `'foo'` → `"'foo'"` 문자열에 자체가 string이 되어 반환됨
  - 배열
    - 배열의 요소가 `undefined`, 함수가 오면 `null`로 변환된다.
      - 빈 배열은 `'[]'` 리턴
  - 객체
    - key값 혹은 value값이 undefined, 함수일 경우 생략되어 반환된다.

        ```js
        { x: 1, y: 2 } → '{ "x": 1, "y": 2 }'
        ```

    - 빈 객체는 `'{}'` 리턴
