# Loop

## For in

- 배열에서는 `index`값을 반환한다.
- 객체에서는 `key`값을 반환한다.

```js
let obj = {'a': 3, 'b': 4, 'c': 6}
let arr = {'a', 'b', 'c', 'd', 'e'}

for(i in arr){console.log(i)}
// 0 1 2 3 4

for(i in obj){console.log(i)}
// a b c
```
