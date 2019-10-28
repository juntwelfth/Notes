# Linear Regression - Distance Formula

## Euclidean Distance

- 거리계산의 가장 대표적인 방식이다.

$$\sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + ... + (a_n - b_n)^2}$$

![euclid](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/distance-formula/euclidean.svg)

$$d = \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2}$$

## Manhattan Distance

- 유클리드 거리법과 비슷하다.
- 맨하탄 거리에서 길을 찾는것과 비슷하다해서 맨하탄 거리법
- 맨하탄 거리법은 유클리드 거리법보다 항상 같거나 길다.

$$\lvert a_1 - b_1 \rvert + \lvert a_2 - b_2 \rvert +...+ \lvert a_n - b_n \rvert$$

![manhattan](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/distance-formula/manhattan.svg)

$$d = \lvert a_1-b_1 \rvert + \lvert a_2-b_2 \rvert$$

## Hamming Distance

- 같은 길이의 두 문자열에서, 같은 위치에서 서로 다른 기호들이 몇 개인지를 센다.
- 주로 스펠링체크 같은 분야에 쓰인다.
- '12345678'과 '12245578'의 해밍거리는 2이다.
- 'toned'와 'roses'의 해밍거리는 3이다.

## SciPy Distances

- Euclidean Distance `.euclidean()`
- Manhattan Distance `.cityblock()`
- Hamming Distance `.hamming()`

- `scipy` Hamming Distance 함수는 항상 0과 1 사이의 숫자로 표현된다.

> 예를들어 `[1, 2, 3]`과 `[7, 2, -10]`에서 Hamming Distance는 `2`인데 `scipy`에선 `2/3`이라고 나온다.
