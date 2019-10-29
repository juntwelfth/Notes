# Javascript Styles

- 2 **spaces** – for indentation
- **No unused variables**
- **No semicolons**

Style Guide와 관련해서 가장 많은 실수는 indentation, spacing, semicolons, and variable naming에 관련된 것들입니다. 이러한 항목들을 특히 신경 써 주시면 실수를 줄일 수 있습니다!

Style Guide로 트집을 잡는 것처럼 느끼실 수도 있지만, 코드를 읽기 좋게 작성하는 것은 매우 중요한 일입니다. 그렇지 않을 경우, 기술적인 인터뷰에서 발생하는 각각의 오류는 치명적이지 않더라도, 그것들이 쌓여서 느리고 비생산적인 인터뷰 결과를 가져올 수 있습니다. Style Guide에 익숙해지는 과정에서 가장 중요한 것은 섬세하고 날카로운 눈으로 자신의 코드를 스스로 검토할 수 있도록 하는 것입니다.

## **Indentation – 들여쓰기**

논리적으로 종속되어 있는 코드를 쓸 때, 종속된 code block는 주인 code block보다 두 칸 들여쓰기 합니다.

들여쓰기를 할 때 탭이 아닌 스페이스를 사용하세요. 탭은 안됩니다.

> 들여쓰기와 관련된 탭과 스페이스 사이의 논쟁은 프로그래밍 세계에서는 아주 오래된 논쟁입니다. 그렇기에 취향의 차이일 뿐 이것이 맞다 틀리다의 문제는 아닙니다. 그러나, 많은 JavaScript 프로젝트에서 대부분의 프로젝트가 2개의 스페이스를 쓰고 있고, 점차 들여쓰기 논쟁의 승리자가 되었습니다. 들여쓰기 약속은 프로그래밍 언어마다 조금씩 다릅니다. 다수의 오픈소스 프로젝트가 진행중인 GitHub에서는, Star(일종의 '좋아요')를 받은 프로젝트의 85% 이상의 JavaScript 프로젝트가 스페이스 들여쓰기를 사용하고 있습니다.여러분이 절대로 피해야 할 단 한가지가 있다면, 바로 스페이스와 탭을 혼용해서 쓰는 것입니다. 이것은 금기입니다!

새로운 code block를 시작할 때면 이전 code block보다 2칸 더 들여쓰기 후 코드를 쓰기 시작하세요

Good:

```js
if (condition) {
  action();
}
```

Bad:

```js
if (condition) {
action();
}
```

Code block의 마지막 줄을 쓸 때 마지막 줄의 시작은, 시작할 때 줄의 시작과 동일한 곳에서 해주세요. 종속된 code block의 시작에 맞추면 안됩니다.

Good:

```js
if (condition) {
  action();
}
```

Bad:

```js
if (condition) {
  action();
  }
```

Code block이 바뀌고 해당 code block에 맞춰 줄을 바꿀 때 2칸 들여쓰기 규칙을 지켜야 합니다. 규칙을 어긴 나쁜 예는 다양하지만, 그 중 한가지를 아래에 소개합니다.

Bad:

```js
transmogrify({
    a: {
    b: function(){
    }
}});
```

## **Naming – 이름 짓기**

### **Variable names – 변수의 이름**

변수의 이름은 한 단어(**Descriptive** word)로 표현하는 것이 가장 좋습니다. 당신이 다루고 있는 문제의 영역(domain), 핵심을 잘 묘사해주는 단어일수록 좋습니다. 또한, 구조적인 부분보다는 변수가 존재하는 목적을 고려해서 변수의 이름을 지어야 합니다.

Good:

```js
let animals = ['cat', 'dog', 'fish'];
```

Bad:

```js
let targetInputs = ['cat', 'dog', 'fish'];
```

Bad:

```js
let array = ['cat', 'dog', 'fish'];
```

array와 같은 Collections을 값으로 갖는 변수의 이름은 복수 명사가 좋습니다.

Good:

```js
let animals = ['cat', 'dog', 'fish'];
```

Bad:

```js
let animalList = ['cat', 'dog', 'fish'];
```

Bad:

```js
let animal = ['cat', 'dog', 'fish'];
```

### **Boolean names – Boolean 이름**

Boolean에 관한 변수의 이름은 전형적인 형식을 가집니다. Boolean 값은 참 혹은 거짓이므로, 관련 변수의 이름 앞에 `is` 혹은 `are`를 붙입니다.

예: `isValid` 또는 `areAvailable`

Good:

```js
let areEqual = true;
```

Bad:

```js
let pass = true;
```

### **Function names – 함수 이름 짓기**

함수 관련 변수의 이름을 지을 때는 동사로 시작해야 합니다. 예를 들면 calculateTotal 혹은 listInventory 등 “{verbObject}” 와 같은 형식입니다. 이런 형식을 사용하면, 변수 이름의 의미가 자명해집니다. 또한, code를 빠르게 훑어보는 사람들이 함수의 입력값과 출력값, 그리고 둘 사이의 변환 과정을 파악하기가 쉬워집니다.

Bad:

```js
let waterBlocks = function() {
  // count how many blocks of ater are collected between each tower
}
```

Good:

```js
let countWaterBlocks = function() {
  // do stuff
}
```

Good:

```js
let counterWaterBlocksBetweenTowers = function() {
  // do stuff
}
```

### **Capital letters in variable names – 변수 이름에서의 대문자**

- 대부분의 사람들은 변수가 포함한 [class](http://en.wikipedia.org/wiki/Class_(computer_science))를 지시하기 위해 변수 이름의 첫 글자를 대문자로 씁니다.
- 몇몇 사람들은 `new` 키워드를 사용한 함수에 한해서 대문자를 쓰기도 합니다.
- 상수(constant), 즉 프로그램 전체에서 일정한 값을 가지는 변수의 이름을 정할 때는 그 변수의 이름은 전체를 대문자로 씁니다.

See code:

```js
// Example of a capitalized class constructor function name.
function Animal() {
}
// Example of an all-caps constant variable name.
const MAX_ITEMS_IN_QUEUE = 100;
```

## **Symbols / punctuation - 기호 / 구두점찍기**

### **중괄호를 생략하지 마십시오 (문법적으로 생략 가능한 때에도)**

Good:

```js
for (key in object) {
  alert(key);
}
```

Bad:

```js
for (key in object)
  alert(key);
```

### **Quoting - 인용**

JavaScript의 문자열을 쓸 때, 그 처음과 끝에는 작은 따옴표를 주로 쓰세요. 큰 따옴표 말구요!

작은 따옴표 혹은 큰 따옴표를 한 종류만 꾸준하게 사용하세요. 섞어 쓰는 것은 좋지 않습니다. 작은 따옴표를 쓰면 HTML을 쉽게 삽입할 수 있습니다. HTML은 태그 속성에 주위에 큰 따옴표를 붙이기 때문입니다.

Good:

```js
let dog = 'dog';
let cat = 'cat';
```

Acceptable:

```js
let dog = "dog";
let cat = "cat";
```

Bad:

```js
let dog = 'dog';
let cat = "cat";
```

줄 바꿈이 필요한 문자열을 정의할 때는 ``` ([backquote](https://www.computerhope.com/jargon/b/backquot.htm))를 사용하는 것도 한 방법입니다.

```js
let multilineText = `this is line one
this is line two
this is line three`;
```

### **Semicolons – 세미콜론**

코드 문장의 끝에는 항상 `;` 세미콜론을 쓰세요.

Good:

```js
alert('hi');
```

Bad:

```js
alert('hi')
```

`if`, `for`, `while` 구문의 끝에는 세미콜론을 사용하지 않아야 합니다.

Good:

```js
if (condition) {
  response();
}
```

Bad:

```js
if (condition) {
  response();
};
```

함수 표현식, 즉 함수가 일반적인 구문의 끝에 쓰여진 경우, 마치 `if`, `for`, `while` 구문의 끝처럼 보일지라도 코드 끝에 세미콜론을 써야합니다.

Good:

```js
let greet = function () {
  alert('hi');
};
```

Bad:

```js
let greet = function () {
  alert('hi');
}
```

세미콜론을 쓰지 않아도 된다고 주장하는 사람들도 더러 있으며, [ESLint Standard Style](https://standardjs.com/)에서는 [세미콜론을 쓸 필요가 없다고 이야기하고 있습니다](https://www.youtube.com/watch?v=gsfbh17Ax9I). 하지만 여전히 많은 프로젝트에서는 세미콜론을 선호합니다.

## **Operators and keywords - 연산자와 키워드**

### **엄격한 비교 연산자를 사용하세요**

`==` 혹은 `!=` 를 사용하는 경우, 의도치 않게 비교 대상의 type이 변하여 비교 연산이 실행될 수 있습니다. 그러므로 반드시 `===` 와 `!==` 를 사용하세요.

Good:

```js
// this comparison evaluates to false, because the number zero is not the same as the empty string.
if (0 === '') {
  alert('looks like they\'re equal');
}
```

Bad:

```js
// This comparison evaluates to true, because after type coercion, zero and the empty string are equal.
if (0 == '') {
  alert('looks like they\'re equal');
}
```

### **3항 연산자 (x ? y : z)**

```js
x ? y : z;
```

`x`가 참이면 `y`를, 거짓이면 `z`를 실행합니다.

3항 연산자는 code를 compact하게 만듭니다. 그러나 읽기 어렵습니다.

다음 중 어느 것이 읽기 쉽습니까?

Uses ternary:

```js
return (actual === expected) ?
  'passed' :
  'FAILED ['+ testName + '] Expected "'+expected+'",but got '+'"'+actual+'"';
```

Uses simple if-statement:

```js
if (actual !== expected) {
  console.log('FAILED ' + testName + ': Expected ' + expected + ', but got ' + actual);
} else {
  console.log('passed');
}
```

아주 짧고 명확한 코드를 쓸 때만 3항 연산자를 사용하세요. 3항 연산자를 사용할 수 있다고 남용하지 마세요.

### **not 연산자(`!`)의 사용**

일반적으로 not 연산자(`!`)는 부정하는 대상 코드의 바로 앞에 붙여 사용합니다.

Bad:

```js
if (! isEqual) {
```

Good:

```js
if (!isEqual) {
```

### **`switch` 구문**

`switch` 구문은 권장하지 않습니다.

`switch` 구문은 `break` 구문 누락으로 인해 오류가 발생하기 쉽습니다. 자세한 내용은 [이 블로그 글](https://ericleads.wordpress.com/2012/12/11/switch-case-considered-harmful/)을 읽어보세요.

## **짧게 쓰기**

### **코드는 뜻이 분명하고 실행 되는 한, 되도록 짧게 쓰세요.**

Not as good:

```js
function square(n) {
  let squaredN = n * n;
  return squaredN;
}
```

Good:

```js
function square(n) {
  return n * n;
}
```

자명한 코드를 쓰는 것이 코드 작성의 제 1원칙입니다. 자명한 코드란, 코멘트나 힌트 없이, 다른 누구에게 설명을 부탁하지 않아도, 작성된 코드의 과정과 결과가 이해하기 쉬운 코드입니다.

### **되도록 부정을 사용하지 마세요.**

너무 많은 부정을 사용해서 코드를 작성하게 되면, 명확성이 떨어질 수 있습니다.

A bit confusing to work out:

```js
if(!equalSizes || !equalValues) {
  // negative outcome
} else {
  // positive outcome
}
```

More straightforward:

```js
if(equalSizes && equalValues) {
  // positive outcome
} else {
  // negative outcome
}
```

### **Boolean 결과값을 바로 return하세요**

Boolean 값을 조건문의 결과값으로 return하는 대신 바로 return 하세요

Verbose:

```js
if(charSet.size < text.length) {
  return false;
}
return true;
```

Concise:

```js
return charSet.size > text.length;
```

## **코드 문장과 구문 사이 공간**

### **코드 사이 공간이 얼마나 필요한가**

- 줄 바꿈을 최소로 사용해야 합니다. 줄 바꿈을 덜 쓸수록 한 화면에서 더 많은 코드를 볼 수 있습니다.

Good:

```js
function square(n) {
  return n * n;
}

function assertEqual(actual, expected, testName) {
  // compare actual and expected
}
```

Bad:

```js
function square(n) {
  return n * n;
}



function assertEqual(actual, expected, testName) {
  // compare actual and expected
}
```

- 최대한 간단하게 코드를 작성하십시오. 긴 코드는 읽기 어렵습니다. 읽기 쉬운 코드가 좋은 코드입니다.
  - 줄을 바꿔야할 때도 있고, 줄 바꿈을 자제해야 할 때도 있습니다. 판단 기준은 어떻게 작성해야 이해하기 쉬운가? 입니다.

### **padding 및 추가적인 들여쓰기**

일반적으로, 보기 어렵지 않다면 들여쓰기를 얼마든지 추가해도 좋습니다.

더 명확하게 보이려고 들여쓰기를 사용할 수 있습니다. 그러한 경우, 처음과 끝에 똑같이 들여쓰기를 사용하세요.

Good:

```js
alert('I chose to put no visual padding around this string');
```

Good:

```js
alert( 'I chose to put visual padding around this string' );
```

Bad:

```js
alert( 'I only put visual padding on one side of this string');
```

변수의 이름과 값을, 같은 항목끼리 묶어서 보기 위해서 들여쓰기를 사용하는 것은 추천하지 않습니다. 만약 이러한 목적으로 들여쓰기를 사용한다면 변수 이름을 변경할 때마다 불필요한 들여쓰기를 너무 많이 사용하게 됩니다.

discouraged:

```js
let firstItem      = getFirst();
let secondItem     = getSecond();
let thirteenthItem = getThirteenth();
```

### **콤마(`,`) 사이에 띄어쓰기**

Bad:

```js
assertEqual(Math.pow(3,2),9,'Math.pow squares properly');
```

Good:

```js
assertEqual(Math.pow(3, 2), 9, 'Math.pow squares properly');
```

### **연산자 사이에 띄어쓰기**

Bad:

```js
'Failed ['+testName+']'...
```

Good:

```js
'Failed [' + testName + ']'...
```

Bad:

```js
if(actual===expected){
  // action
}else{
  // alternate action
}
```

Good:

```js
if(actual === expected){
  // action
} else {
  // alternate action
}
```

## **주석**

- 주석을 쓰기보다는 명확한 변수이름과 함수이름을 쓰는 것이 좋습니다.
- 코드 구조와 이름을 제대로 작성했다면 코드 자체의 "story"(데이터 흐름과 처리과정)를 충분히 전달할 수 있습니다. 주석으로 "story"를 전달하려는 것은 좋지 않은 방법입니다.
- 주석은 파일을 필요 이상으로 길게 만듭니다. 주석은 작동하는 코드가 아니기 때문입니다.
- 주석은 코드를 쓴 이유 즉, 코드의 **목적**을 설명해야 합니다. 코드가 어떻게 작동하는지를 설명하면 안됩니다.
- 쓸데없는 주석은 지워주세요. 불필요한, 날짜가 지난, 임시적인 주석들이 쓸데없는 주석에 해당합니다.

## **JavaScript gotchas - 자바스크립트를 잡아라!**

### **Snake vs. Camel Casing - 뱀 모양 vs 낙타 모양**

JavaScript에서는 변수의 이름을 지정할 때 'Camel Casing'으로 지정합니다. 이것은 Ruby 같은 다른 프로그래밍 언어에서 사용하는 'Snake Casing'과 다릅니다.

Good:

```js
let camelCased = 'Used in javascript';
```

Bad:

```js
let snake_cased = 'Used in other languages';
```

JavaScript에서 '뱀 모양'을 사용하는 경우는, 상수 이름을 지을 때입니다.

```js
const MAX_ITEMS_IN_QUEUE = 100;
```
