# Object

## keys()

- ECMA 5+
- Object의 길이를 구할때 용이하다.

```js
let obj = {};
let obj2 = { a: 1, b: 2, c: 3 };

Object.keys(obj).length    // 0
Object.keys(obj2).length   // 3
```

## entries()

- ECMA 7+
- Object의 길이를 구할때 용이하다.

```js
let obj = {};
let obj2 = { a: 1, b: 2, c: 3 };

Object.entries(obj).length    // 0
Object.entries(obj2).length   // 3
```

## 생김새

```js
let object = {
  name: "Junil",
  age: 24,
  friends: "Jiyoung"
}
```

1. 중괄호 `{`, `}`로 감싸져있다.

2. `key`, `value`가 한 쌍을 이루고있다. `key: value` ( 콜론 `:` 으로 구분된다 )

3. 배열과 같이 각 `property`가 쉼표로 나뉘어진다.

4. 객체는 주로 연관성있는 아이들끼리 모아놓는다.
   > 예를들면 사람의 정보라던지, 중간고사 점수라던지..

## 특징

- 객체속에 객체가 존재할 수 있다.

```js
let object = {
  name: "Junil",
  age: 24,
  friends: {
    name: "Jiyoung",
    age: 26
  }
};
```

객체안에 객체가 얼마든지 중첩될 수 있다.

배열도 들어갈 수 있다. (key에는 들어갈 수 없음)

## 객체의 값 사용하기 (불러오기)

- 첫번째 방법
- Dot notation

  ```js
  let user = {
    firstName: 'Junil',
    lastName: 'Seo',
    age: 24,
    email: 'abcdefg@gmail.com',
    address: 'seoul'
  }
  
  
  // user의 이름을 가져오기
  user.firstName;    // 'Junil'
  
  // user의 나이를 가져오기
  user.age;          // 24
  ```

- 두번째 방법
- Bracket notation

  ```js
  let user = {
    firstName: 'Junil',
    lastName: 'Seo',
    age: 24,
    email: 'abcdefg@gmail.com',
    address: 'seoul'
  }
  
  
  // user의 이름을 가져오기
  user['firstName']    // 'Junil'
  
  // user의 나이를 가져오기
  user['age']          // 24
  ```

객체의 `key`값이 뭐가 올 수 있는지는 확실치않음.......

일단 `string`은 확실히 가능, `배열` 확실히 불가능, `숫자` 가능

value값에는 다양한 종류가 올 수 있음... ex) `undefined`, `null`, `함수`

연습

```js
let tweet = {
  writer: 'stevelee',
  createdAt: '2019-09-10 12:03:33',
  content: '프리코스 재밌어요!'
};
```

> stevelee라는 아이디를 가진 유저가 트위터에 새로운 글을 올렸습니다.
그가 작성한 글 "프리코스 재밌어요!" 라는 내용을
bracket notation으로 어떻게 가져올 수 있을까요?
dot notation으로 가져오는 방법도 생각해봅시다!

```js
tweet[content];  // ????
```

에러가 난다.

> bracket notation을 쓸 때에는 bracket 안쪽의 내용을 문자열 형식으로 전달해야 함

## 객체에 값 추가하기

- Dot notation, Bracket notation 두 방식으로 전부 가능하다

  ```js
  let user = {
    // firstName: 'Junil'
    lastName: 'Seo',
    // age: 24,
    email: 'abcdefg@gmail.com',
    address: 'seoul'
  }
  
  
  // user의 이름을 가져오기
  user['firstName']    // 에러
  
  // user의 나이를 가져오기
  user['age']          // 에러
  
  // 추가시켜주기
  user['firstName'] = 'Junil'
  user.age = 24
  
  // 다시 user의 이름을 가져오기
  user['firstName']    // 'Junil'
  
  // 다시 user의 나이를 가져오기
  user['age']          // 24
  ```

## 값 삭제하기

- `delete` 키워드를 이용해서 삭제할 수 있다.

  ```js
  let user = {
    firstName: 'Junil',
    lastName: 'Seo',
    age: 24,
    email: 'abcdefg@gmail.com',
    address: 'seoul'
  }
  
  delete user.firstName;
  delete user['age'];
  
  console.log(user);
  // 아래와 같이 출력됨
  {lastName: 'Seo', email: 'abcdefg@gmail.com', address: 'seoul'}
  ```

## 값이 존재하는지 확인하기

- `in`

```js
let user = {
  firstName: 'Junil',
  lastName: 'Seo',
  age: 24,
  email: 'abcdefg@gmail.com',
  address: 'seoul'
}

'age' in user;    // true

delete user['age'];

'age' in user;    // false
```
