# Introduction to Statistics

## NumPy and Mean

- `numpy.mean()`
- 평균값

```py
import numpy as np

survey_responses = [5, 10.2, 4, .3 ... 6.6]

>>> survey_array = np.array(survey_responses)
>>> np.mean(survey_array)
5.220
```

> 먼저 `list`를 `numpy array`로 변환시킨 후 `mean` 키워드를 이용해 평균값을 구했다.

### Mean and Logical Operations

- mean 키워드를 써서 평균값을 구하지만 조건을 걸면 퍼센트를 구한다.
- `numpy.mean(target > 3)`

```py
>>> np.mean(survey_array > 8)
0.2    # 20%라는 뜻

import numpy as np

class_year = np.array([1967, 1949, 2004, 1997,
    1953, 1950, 1958, 1974, 1987, 2006, 2013,
    1978, 1951, 1998, 1996, 1952, 2005, 2007,
    2003, 1955, 1963, 1978, 2001, 2012, 2014,
    1948, 1970, 2011, 1962, 1966, 1978, 1988,
    2006, 1971, 1994, 1978, 1977, 1960, 2008,
    1965, 1990, 2011, 1962, 1995, 2004, 1991,
    1952, 2013, 1983, 1955, 1957, 1947, 1994,
    1978, 1957, 2016, 1969, 1996, 1958, 1994,
    1958, 2008, 1988, 1977, 1991, 1997, 2009,
    1976, 1999, 1975, 1949, 1985, 2001, 1952,
    1953, 1949, 2015, 2006, 1996, 2015, 2009,
    1949, 2004, 2010, 2011, 2001, 1998, 1967,
    1994, 1966, 1994, 1986, 1963, 1954, 1963,
    1987, 1992, 2008, 1979, 1987])

# class_year가 2005 이상인 숫자들이 몇퍼센트인지 구하는 식
millennials = np.mean(class_year > 2005)
print(millennials)    # 0.2 (20퍼센트)
```

> 특정 값의 평균값을 퍼센트로 구할 수 있다.

`np.mean(survey_array > 8)`은 8보다 큰 수의 요소들을 true (1)로 변환시키고 true값들만 더한 후에 총 갯수로 나눈다.

### Calculating the Mean of 2D Arrays

- 2차원 배열의 평균값을 구하는 여러가지 방법
- 2차원 배열 전체의 평균값을 구할 수도 있고
- `axis=1` (row)으로 나눠서 평균값을 구할 수도 있고
- `axis=0` (column)로 나눠서 평균값을 구할 수도 있다.

```py
# 2차원 배열
>>> ring_toss = np.array([[1, 0, 0],
                          [0, 0, 1],
                          [1, 0, 1]])

# 2차원 배열 전체의 평균값
>>> np.mean(ring_toss)
0.44444444444444442

# 각 row의 평균값
>>> np.mean(ring_toss, axis=1)
array([ 0.33333333,  0.33333333,  0.66666667])

# 각 column의 평균값
>>> np.mean(ring_toss, axis=0)
array([ 0.66666667,  0.        ,  0.66666667])
```

## Outliers

- 특이치, 특잇값

```py
[50, 50, 51, 49, 48, 127]
```

- 3학년 학생들의 키를 쟀는데 실수로 단위를 잘못 변환했을 경우
- 이 경우 127은 outlier이다.

```py
[50, 50, 51, 49, 48, 45]
```

- 종종 outlier들은 실수로 입력된 값이 아닐 때도 있다.

- 학교에 조기입학을 해서 실제로는 동급생보다 한 살 어린 사람의 키 또한 outlier이다.

```py
[50, 50, 51, 49, 48, 58.5]
```

- 단순히 동급생들보다 키가 비정상적으로 큰 사람의 결과값 또한 outlier이다.

[Outliers and Mean](https://s3.amazonaws.com/codecademy-content/courses/numpy/clustered_outliers.html)

### Sorting and Outliers

- outliers를 간단히 알아볼 수 있는 방법은 정렬을 하고 첫번째 요소나 마지막 요소가 크게 벗어나 있는지 확인하면 된다.
- `numpy.sort()` function을 사용해 정렬할 수 있다.

```py
>>> heights = np.array([49.7, 46.9, 62, 47.2,
                          47, 48.3, 48.7])

>>> np.sort(heights)
array([46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])

import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85,
    94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87,
    86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88,
    191, 95, 96, 87,99, 93, 90, 86, 87, 100, 187,
    98, 101, 101, 96, 94, 96, 87, 86, 92, 98, 94,
    98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94,
    91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90,
    98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90,
    91, 90, 92, 92])

sorted_temps = np.sort(temps)
print(sorted_temps)
[ 85  85  85  85  85  86  86  86  86  86  86  
  86  87  87  87  87  87  87  87  88  88  88  
  88  88  88  88  88  89  89  90  90  90  90  
  90  90  90  90  91  91  91  92  92  92  92  
  92  93  93  93  93  93  94  94  94  94  94  
  94  94  95  95  96  96  96  96  96  96  97  
  97  97  97  97  98  98  98  98  98  98  99  
  99  99  99  99 100 101 101 187 191 195 196 198 199]
```

## NumPy and Median

- 평균과는 달리 배열에서 중간에 위치하는 값을 반환한다.
- `np.median()`

```py
np.array([1, 1, 2, 3, 4, 5, 5])
```

> median = 3

```py
np.array([1, 1, 1, 2, 99, 99, 99])
```

> median = 2

```py
np.array([1, 1, 2, 3, 4, 5, 5, 6])
```

> median = (3 + 4) / 2 = 3.5

- 배열의 요소 갯수가 짝수일 경우 가운데 숫자 두개의 평균값을 반환한다.

```py
>>> my_array = np.array([50, 38, 291, 59, 14])
>>> np.median(my_array)
50.0
```

> NumPy 라이브러리 함수를 사용해 바로 값을 구할 수도 있다.

### Mean vs Median

- Dataset에서 median과 mean은 중요한 비교대상이다.
- mean(평균값)은 outliers에 영향을 받는 반면 median은 영향을 받지 않는다.

## Percentiles Pt.1

- median은 데이터셋의 중간값이다. 이 말의 뜻은 데이터의 50%가 median 값보다 낮고 데이터의 50%가 median 값보다 높다는 뜻이다.
- 이 비율을 다르게 하고 싶을 때 percentile을 이용할 수 있다.
- N번째 percentile은 N%의 데이터가 이 숫자 밑에 있다는 뜻이다.
- `numpy.percentile()` 함수를 쓸 수 있고, 인자로는 배열과 percentile 두개가 들어간다.

```py
d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
```

11개의 숫자가 데이터셋에 존재할 때, 40th percentile은 40%의 데이터를 기준으로 나눈다는 뜻이다. (설명하기 넘 어려운것)

![percentile](https://s3.amazonaws.com/codecademy-content/courses/numpy/NumPy+40+percentile.svg)

- 40th percentile은 4를 반환한다.

```py
>>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8])
>>> np.percentile(d, 40)
4.00
```

percentile값은 배열을 정렬한 후에 구하는 방식이다.

```py
patrons = np.array([ 2, 6, 14, 4, 3, 9,
    1, 11, 4, 2, 8])
# sorted_patrons =([ 1, 2, 2, 3, 4, 4,
#   6, 8, 9, 11, 14])

thirtieth_percentile = np.percentile(patrons, 30)
seventieth_percentile = np.percentile(patrons, 70)

print("thirtieth_percentile : {}, \
    seventieth_percentile : {}"
    .format(thirtieth_percentile,
    seventieth_percentile))

# thirtieth_percentile : 3.0,
# seventieth_percentile : 8.0
```

## Percentiles Pt.2

- 몇몇 percentiles는 고유 명칭을 가지고 있다.
- The **25th percentile** is called the *first quartile*
- The **50th percentile** is called the *median*
- The **75th percentile** is called the *third quartile*
- minimum, first quartile, median, third quartile, maximum 이렇게 다섯개는 *five-number summary*라고 불리운다.

> first quartile과 third quartile의 차이를 interquartile range라고 부른다.

```py
d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
```

이러한 배열이 주어졌을 때

```py
np.percentile(d, 25)
>>> 3.5
np.percentile(d, 75)
>>> 6.5
```

`numpy.percentile()` 함수를 이용해 25th, 75th percentiles를 구할 수 있다.

> 6.5 에서 3.5를 빼주면 interquartile range를 구할 수 있다.

- interquartile range는 데이터가 얼마나 넓게 분포되어 있는지 보여준다.
- 더 작으면 작을수록 적은 변화, 더 크면 클수록 큰 변화를 나타낸다.

> interquartile range는 median, mean, 50th percentile과 다른 값이다!

## NumPy and Standard Deviation

- interquartile range와 마찬가지로 데이터가 얼마나 넓게 분포되어 있는지 보여준다.
- `numpy.std()`

[Standard Deviation](https://s3.amazonaws.com/codecademy-content/courses/numpy/std.html)

> Standard deviation이 적을수록 편차가 적어진다.

```py
>>> nums = np.array([65, 36, 52, 91, 63, 79])
>>> np.std(nums)
17.716909687891082
```
