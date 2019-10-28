# Quartiles

- 데이터를 네개의 그룹으로 나누는 방법

![quartiles](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/quartiles.svg)

>위 그림에서 Q1은 `10` Q2는 `13` Q3은 `22`이다.
0%   ~ 25%   =      ~ 10
25% ~ 50%   = 10 ~ 13
50% ~ 75%   = 13 ~ 22
75% ~ 100% = 22 ~

## The Second Quartile

- The Second Quartile(Q2)은 median(중간값)과 같다.
- Quartile을 찾기위해 우선 데이터를 정렬해야 한다.

$$[8, 15, 4, −108, 16, 23, 42]$$

>위 데이터셋을 정렬하면 아래와 같이 된다.

$$[-108, 4, 8, 15, 16, 23, 42]$$

>이제 이 정렬된 데이터셋에서 중간값을 찾을 수 있다. `15`
중간값 밑으로 세개의 포인트, 위로 세개의 포인트

- 짝수개의 데이터 집합

$$[4, 8, 15, 16, 23, 42]$$

>위와 같이 데이터의 갯수가 짝수개면 중간값 두개를 더한 후 평균을 내면 된다.

```py
(15 + 16) / 2 = 15.5
```

## Q1 and Q3

### Method One

- Q2의 값을 이용해 Q1과 Q3의 값을 찾을 수 있다.

$$[-108, 4, 8, 15, 16, 23, 42]$$

>**Q2**의 값은 `15`. 따라서 `15`를 기점으로 데이터를 나눠준다.

$$[-108, 4, 8]$$

>위 데이터집합에서 중간값은 `4`이며, **Q1**값도 `4`이다.

$$[16, 23, 42]$$

>위 데이터집합에서 중간값은 `23`이며, **Q3**값도 `23`이다.

### Method Two: Including Q2

- 데이터집합의 사분위수를 구하는데에는 정해진 방법이 없다. 따라서 두가지의 다른 방법을 사용할 수 있다.

$$[-108, 4, 8, 15, 16, 23, 42]$$

>첫번째 방법으로 **Q1**이 `4`라는것을 찾아냈고, **Q2**를 찾을 땐 **Q1**보다 작은 숫자들을 비교했다.

- 두번째 방법은 **Q1**값을 포함한채로 찾는것이다.

$$[-108, 4, 8, 15]$$

>전체 데이터 집합의 중간값을 포함한 데이터의 집합에서 중간값을 찾는다.

- (4 + 8) / 2 = `6`

$$[15, 16, 23, 42]$$

> 전체 데이터 집합의 중간값을 포함한 데이터의 집합에서 중간값을 찾는다.

- (16 + 23) / 2 = `19.5`

## Quartiles in NumPy

- 수동으로 Quartile들을 찾는 방법을 썼었는데, 이 방법은 데이터가 많아지면 많아질수록 더 힘들어진다.
- 이를 위한 NumPy 라이브러리의 메소드를 이용할 수 있다.
- `quantile()`
quartile은 quantile에 속한다.

```py
from song_data import songs
import numpy as np

dataset = [50, 10, 4, -3, 4, -20, 2]
third_quartile = np.quantile(dataset, 0.75)

songs_q1 = np.quantile(songs, 0.25) # Q1
songs_q2 = np.quantile(songs, 0.5)  # Q2
songs_q3 = np.quantile(songs, 0.75) # Q3

favorite_song = 219
quarter = 2
```

## Quantiles

- Quantiles는 데이터를 동일한 수로 나눠 그룹화시킨 것이다.
- 예를들어 내 시험성적이 상위 10%인지 알고싶으면 전체 데이터를 10개의 그룹으로 나눠 비교해보면 된다.

![quantiles](Untitled-d04ba940-5f1b-4845-a5ea-adb53592c1a7.png)

>1. 9개의 특정한 값을 설정해 10개의 그룹으로 나눴다.
>2. 이 9개의 특정한 값이 quantile이다.
>3. 정확한 말로는 10개의 quantile 혹은 분위가 있는것이다.

## Quantiles in NumPy

- NumPy 라이브러리에는 `quantile()`이라는 메소드가 있다.
- 이 메소드는 데이터 집합의 quantile을 출력해준다.
  - 데이터셋을 첫번째 인자로 받고
  - 두번째 인자로는 `0`부터 `1`사이의 퍼센티지를 받는다.

```py
import numpy as np

dataset = [5, 10, -20, 42, -9, 10]
ten_percent = np.quantile(dataset, 0.10)
```

- 데이터 집합의 10%가 되는 데이터를 `ten_percent`에 저장한다. `-14.5`

>`-14.5`는 엄밀히 따지자면 quantile은 아니다.

```py
np.quantile(songs, 0.23)
```

>상위 23%를 알아내려면 이런식으로 해주면된다.

## Many Quantiles

- 두개 이상의 quantile을 출력하고 싶을 때

- 5개의 quantile 혹은 데이터를 다섯개의 그룹으로 나누는 네개의 값을 얻고자 할 때

```py
dataset = [5, 10, -20, 42, -9, 10]
ten_per = np.quantile(dataset, [0.2, 0.4, 0.6, 0.8])
```

![ten](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/even.svg)

```py
dataset = [5, 10, -20, 42, -9, 10]
ten_per = np.quantile(dataset, [0.2, 0.4, 0.7, 0.8])
```

![ten](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/uneven.svg)

## Common Quantiles

- 가장 흔한 quantile 중 하나는 2-quantile이다. 이 값은 데이터를 두개의 동일한 사이즈의 그룹으로 나눈다. (중간값과 같다.)

![2-quantile](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/median.svg)

- 두번째로는 4-quantile 혹은 quartile. 데이터를 네개의 동일한 사이즈의 그룹으로 나눈다.

![quartile](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/quartiles.svg)

- 마지막으로 percentiles. 데이터를 100개의 동일한 사이즈의 그룹으로 나눈다.
- 상위 80%, the 80th percentile 등등으로 불리운다.

>1. 만약 `n`개의 quantile이 있다면, 데이터는 `n +    1`개의 그룹으로 나눠진다.
>2. median (중간값)은 quantile이다. (2-quantile)
>3. quartile과 percentile 또한 quantile이다.

## Range Review

- 데이터셋을 설명할 때 가장 중요한 요소중에 하나인 범위
- 하지만 outlier이 섞여있으면 범위값이 이상해진다.

![range](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/outliers.svg)

- 위 그림에서 대부분의 데이터는 `0`과 `20`사이에 몰려있다.

- 하지만 `-20`, `40`과 같은 outlier들이 존재해 범위값이 `60`이 된다.

- 이와같은 경우를 피하기 위해 **Interquartile range** (IQR)이 필요하다.

## Interquartile Range

- IQR은 Q3 - Q1이다.

![iqr](https://s3.amazonaws.com/codecademy-content/courses/statistics/quantiles/interquartile.svg)

- 첫번째 quartile은 데이터의 25%, 세번째는 75%이다. 이 두 점 사이의 거리를 구하면 interquartile range를 구할 수 있다.

## IQR in SciPy

- NumPy를 이용하여 quartiles를 찾고, IQR을 계산했었다.
- SciPy 라이브러리엔 IQR을 한번에 계산하는 메소드가 있다.
- `iqr()` 메소드는 데이터셋을 인자로 받고, Interquartile Range를 반환한다.

```py
From scipy.stats import iqr

dataset = [4, 10, 38, 85, 193]
interquartile_range = iqr(dataset)
```

>scipy가 아닌 scipy`.stats`에서 불러왔다.
