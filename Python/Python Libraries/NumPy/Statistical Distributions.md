
# Histograms

## Histograms, Part I

- 우리가 데이터셋을 처음 볼 때, 생각해야 하는 것
- 특정 값이 다른 값들보다 더 자주 등장하는지?
- 데이터셋의 범위가 어디인지? (i.e., the min and the max values?)
- 이상치가 존재하는지?
- 위 사항들을 *histogram*이라고 불리는 차트를 이용해 쉽게 볼 수 있다.

```py
d = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
```

>이러한 데이터셋이 주어졌을 때, 간단한 histogram은 우리에게 각 숫자들이 얼마나 많이 있는지 보여준다.

![hist1](https://s3.amazonaws.com/codecademy-content/courses/numpy/histogram-i-narrative-1.png)

## Histograms, Part II

- 대량의 데이터셋이 주어졌을 때 우린 데이터 값의 범위를 넓게 지정한다. 0-5, 6-10, 11-15 이런식으로
- 이러한 그룹핑은 *bins*라고 불린다.
- histogram에 있는 모든 bins들은 폭이 일정하다.

![hist2](https://s3.amazonaws.com/codecademy-content/courses/numpy/histogram-ii-narrative-1.png)

>the width of each bin would be 5

## Histograms, Part III

```py
from matplotlib import pyplot as plt

# This plots a histogram
plt.hist(data)

# This displays the histogram
plt.show()
```

- `plt.hist`에 인자를 주지않으면 matplotlib은 자동으로 10 bins짜리 그래프를 만든다.
- `plt.show()` 함수를 사용해서 꼭 그래프를 화면에 띄우자

- bins의 크기를 바꾸고 싶다면 `bins` 키워드를 사용해서 바꿔줄 수 있다.

```py
plt.hist(data, bins=5)
```

- range의 크기를 바꾸고 싶다면 `range` 키워드를 사용해서 바꿔줄 수 있다.

- range에는 두개의 숫자로 범위를 전달해야 하는데 뒤에 오는 숫자는 포함되지 않는다.

> tuple 형태로 전달해야 한다. (range는 확대의 개념임)

```py
plt.hist(data, range=(20, 51))

from matplotlib import pyplot as plt

d = np.array([1, 1, 1, 2, 2, 2,
    2, 2, 3, 3, 4, 4, 4, 4, 5])

plt.hist(d, bins=5, range=(1, 6))

plt.show()
```

![hist3](https://s3.amazonaws.com/codecademy-content/courses/numpy/test.svg)

>5 bins, 5 range

# Different Types of Distributions

- The *probability of success* was 30% (he makes 30% of free throws)
- The number of *trials* was 10 (he took 10 shots)
- The number of *successes* was 4 (he made 4 shots)

## Different Types of Distributions, Part I

- Histogram과 데이터셋들은 그래프의 모양에 따라 다양하게 정의될 수 있다.
  - 그 중 한가지 방법은 peaks의 갯수를 세어 나누는 방법이 있다.

### 1. Unimodal

![unimodal](https://s3.amazonaws.com/codecademy-content/courses/numpy/distribution_type_i/unimodal_new.svg)
> 한개의 distinct peak밖에 없다.

### 2. Bimodal

![bimodal](https://s3.amazonaws.com/codecademy-content/courses/numpy/distribution_type_i/bimodal_new.svg)

### 3. Multimodal

![multimodal](https://s3.amazonaws.com/codecademy-content/courses/numpy/distribution_type_i/multimodal_new.svg)
> 세개 이상의 peak을 가질 때 multimodal dataset이라고 부른다.

### 4. Uniform

![uniform](https://s3.amazonaws.com/codecademy-content/courses/numpy/distribution_type_i/uniform_new.svg)

> 딱히 그렇다 할 peak이 없다.

## Different Types of Distribution, Part II

### unimodal의 다양한 형태

1. unimodal의 좌우가 (대충)대칭일 때 Symmetric이라고 부른다.
![symmetric](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-symmetric-noline.svg)

2. peak의 오른쪽으로 꼬리가 길게 나타나고 데이터가 대부분 왼쪽에 몰려있는 형태를 skew-right 데이터셋이라고 부른다.
![skew-right](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-skew-right-noline.svg)

3. 반대의 경우 skew-left라고 부른다.
![skew-left](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-skew-left-noline.svg)

- 이러한 형태들은 mean(평균값)과 median(중간값)에 영향을 끼친다. skewed 형태의 그래프에선 mean은 딱히 쓸모가없어진다.
![mean](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-symmetric.svg)
![mean](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-skew-right.svg)
![mean](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/distribution-types-ii-skew-left.svg)

## Normal Distribution, Part I

- 가장 흔한 통계분포는 normal distribution이다.
- normal distribution은 symmetric이고 unimodal이다.
- 정규분포를 따르는 다양한 예시
  - The heights of a large group of people
  - 건강한 사람들의 혈압치
  - 측정 오류치

![mean, std](https://s3.amazonaws.com/codecademy-content/courses/numpy/normal_distribution.svg)

[직접 조종해보자](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/mean-std-norm-dist.html)

## Normal Distribution, Part II

- NumPy 라이브러리로 랜덤 숫자를 생성하는 방법
- `numpy.random.normal()`
  - loc : mean(중간값)
  - scale : standard deviation(표준편차) aka std
  - size : 랜덤 숫자의 갯수(?) 크기

```py
a = np.random.normal(0, 1, size=100000)
```

![random.normal](https://s3.amazonaws.com/codecademy-content/courses/numpy/symmetric.svg)
> 이렇게 생겼다.

```py
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000)

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data, bins=30, range=(5, 8.5),
        histtype='step', label='Brachiosaurus')

plt.hist(f_data, bins=30, range=(5, 8.5),
        histtype='step', label='Fictionosaurus')

plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()
```

![plot](https://i.imgur.com/c0CN0m9.png)

## Standard Deviations and Normal Distribution, Part I

- Normal distribution에서, mean(평균값)과 standard deviation(표준편차)이 그래프의 모양을 결정짓는다.

[Standard Deviation and Normal Distribution](https://s3.amazonaws.com/codecademy-content/courses/numpy/norm_dist.html)

## Standard Deviations and Normal Distribution, Part II

- 평균이 50이고 표준 편차가 10 인 정규 분포가 있다고 가정했을 때

```py
lower_bound = mean - std
            = 50 - 10
            = 40

upper_bound = mean + std
            = 50 + 10
            = 60
```

- 데이터셋의 68%가 40 ~ 60 사이에 있다고 예상할 수 있다.

- 평균값과 표준편차값에 상관없이 데이터의 68%가 +/- 1 평균의 표준편차 내에 존재한다.(???????????)

- 68% of our samples will fall between +/- 1 standard deviation of the mean

- 95% of our samples will fall between +/- 2 standard deviations of the mean

- 99.7% of our samples will fall between +/- 3 standard deviations of the mean

```py
import numpy as np

one_above = 1100  # 평균 + 표준편차

one_below = 900   # 평균 - 표준편차

print(one_above, one_below)

one_std = 2000 * 0.68  
# 데이터의 68%가 900 ~ 1100 사이에 존재한다.

print(one_std)
```

## Binomial Distribution, Part I

- The *probability of success* was 30% (he makes 30% of free throws)
- The number of *trials* was 10 (he took 10 shots)
- The number of *successes* was 4 (he made 4 shots)
- binomial distribution은 중요하다. 왜냐면 특정값이 어떻게 존재하는지 알 수 있기 때문 (우리가 예상했던 값이 아니더라도)

- 아래 그래프를 통해 농구선수가 4번의 골을 넣었더라도 이상한 일이 아니라는걸 알 수 있다.
(10번 다 넣으면 이상한거겠지)

![throws](https://s3.amazonaws.com/codecademy-content/courses/numpy/free_throws.svg)

## Binomial Distributions, Part II

- `numpy.random.binomial` 함수를 통해 binomial 랜덤 숫자를 만들 수 있다.
  - N : 샘플 혹은 시도횟수
  - P : 성공 확률, 가능성
  - size : 사이즈

> 10000번의 시도, 10번의 시도, 30%의 확률

```py
# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)

a = np.random.binomial(10, 0.30, size=10000)
```

> Matplotlib를 이용해 그래프를 만들어 보자.

```py
plt.hist(a, range=(0, 10), bins=10, normed=True)
plt.xlabel('Number of "Free Throws"')
plt.ylabel('Frequency')
plt.show()
```

![frequency](https://s3.amazonaws.com/codecademy-content/courses/numpy/free_throws.svg)

> 500개의 이메일을 보내는데 그 중 5%만이 이메일을 연다.
10000번의 시도를 했을 때의 그래프를 나타내는 방법

```py
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

emails = np.random.binomial(500, 0.05, size=10000)

plt.hist(emails)  # 필수
plt.show()        # 필수
```

![a](https://i.imgur.com/mePMTU5.png)

## Binomial Distributions and Probability

> Our basketball player has a 30% chance of making any individual basket. He took 10 shots and made 4 of them, even though we only expected him to make 3. What percent chance did he have of making those 4 shots?

4번의 성공을 할 확률을 구해보자.

```py
a = np.random.binomial(10, 0.30, size=10000)
np.mean(a == 4)
>> 0.1973  # 19.73% -> 20%의 확률
```

- 랜덤 숫자이기 때문에 결과는 매번 조금씩 달라진다.

- 10000번의 시도, 0.3의 확률이면 소수점 이하 두번째 자리까지 정확하다.

```py
import numpy as np

emails = np.random.binomial(500, 0.05, size=10000)

# 아무도 메일을 열어보지 않을 확률
no_emails = np.mean(emails == 0)

# 500명중 8% 이상이 열어볼 경우
b_test_emails = np.mean(emails > 40)  # 500의 8% = 40

print(no_emails, b_test_emails)
```
