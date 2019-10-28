
# Variance

- 데이터셋의 mean, median, mode를 찾는것은 중요하다. 하지만 아래와 같은 경우를 보자.

```py
dataset_one = [-4, -2, 0, 2, 4]
dataset_two = [-400, -200, 0, 200, 400]
```

>위 두 데이터셋은 평균값, 중간값이 서로 같다. `0`

```py
import numpy as np
import matplotlib.pyplot as plt

teacher_one_grades = [83.42, 88.04, 82.12, 85.02,
    82.52, 87.47, 84.69, 85.18, 86.29, 85.53,
    81.29, 82.54, 83.47, 83.91, 86.83, 88.5,
    84.95, 83.79, 84.74, 84.03, 87.62, 81.15,
    83.45, 80.24, 82.76, 83.98, 84.95, 83.37,
    84.89, 87.29]
teacher_two_grades = [85.15, 95.64, 84.73, 71.46,
    95.99, 81.61, 86.55, 79.81, 77.06, 92.86,
    83.67, 73.63, 90.12, 80.64, 78.46, 76.86,
    104.4, 88.53, 74.62, 91.27, 76.53, 94.37,
    84.74, 81.84, 97.69, 70.77, 84.44, 88.06,
    91.62, 65.82]

print("Teacher One mean: "
    + str(np.mean(teacher_one_grades)))
>>> Teacher One mean: 84.46766666666666

print("Teacher Two mean: "
    + str(np.mean(teacher_two_grades)))
>>> Teacher Two mean: 84.298

plt.subplot(211)
plt.title("Teacher One Grades")
plt.xlabel("Grades")
plt.hist(teacher_one_grades)
plt.xlim(65, 105)


plt.subplot(212)
plt.title("Teacher Two Grades")
plt.xlabel("Grades")
plt.hist(teacher_two_grades, bins = 20)
plt.xlim(65, 105)

plt.tight_layout()
plt.show()
```

![s](https://i.imgur.com/YTiu2Qr.png)

## Distance From Mean

- 데이터들이 얼마나 분산되어있는가?
  - 데이터가 많이 퍼져있으면 분산값이 크고
  - 데이터가 적게 퍼져있으면 분산값이 작다.
- 이를 계산하기 위해 평균값에서부터 거리를 잰다.

$$\text{difference} = X - \mu$$

- `X` : Data Point

- `mu` : 평균값 (mean)

```py
import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)  # 85.8

# 각 포인트에서 평균값을 빼준다. (음수가 나올 수도 있다.)
difference_one = grades[0] - mean    # 2.2
difference_two = grades[1] - mean    # -3.8
difference_three = grades[2] - mean  # -0.8
difference_four = grades[3] - mean   # -1.8
difference_five = grades[4] - mean   # 4.2
```

## Average Distances

- 각각의 distance들의 평균값을 구해준다.

```py
import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = 88 - mean
difference_two = 82 - mean
difference_three = 85 - mean
difference_four = 84 - mean
difference_five = 90 - mean

#Part 1: Sum the differences
difference_sum = difference_one
    + difference_two + difference_three
    + difference_four + difference_five

#Part 2: Average the differences
average_difference = difference_sum / 5

#IGNORE CODE BELOW HERE
print("The sum of the differences is "
    + str(format(difference_sum, "f")))
>>> The sum of the differences is 0.000000

print("The average difference is "
    + str(format(average_difference, "f")))
>>> The average difference is 0.000000
```

>결과값이 뭔가 이상하다.

## Square The Differences

- 아래 예제를 보면

```py
[-5, 5]
```

>두 수의 평균값은 `0`이다. 위의 과정과 같이 각 포인트에서 평균값을 빼는데 이런 경우엔 `-5 - 0 = -5` 그리고 `5 - 0 = 5` 변화가 없게된다.

```py
[-200, 200]
```

>위 코드도 마찬가지다. 평균값이 `0`이다.
결국 음수가 문제인 것이다.

- 이런 경우를 피하기 위해 포인트 - 평균값을 제곱해주면 된다.

$$\text{difference} = (X−\mu)^2$$

```py
import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

# When calculating these variables,
# square the difference.
difference_one = (88 - mean) ** 2
difference_two = (82 - mean) ** 2
difference_three = (85 - mean) ** 2
difference_four = (84 - mean) ** 2
difference_five = (90 - mean) ** 2

difference_sum = difference_one
    + difference_two + difference_three
    + difference_four + difference_five

variance = difference_sum / 5

print("The sum of the squared differences is "
    + str(difference_sum))
>>> The sum of the squared differences is 40.8

print("The variance is " + str(variance))
>>> The variance is 8.16
```

## Variance In NumPy

- 지금까지의 과정을 수식화하면 아래와 같다.

$$\sigma^2 = \frac{\sum_{i=1}^{N}{(X_i -\mu)^2}}{N}$$

1. Variance는 보통 sigma의 제곱으로 나타낸다.
2. Point 1번째 숫자부터 n번째 숫자까지 평균값과의 차이를 구한다.
3. 포인트와 평균값의 차이를 제곱해서 양수로 만든다.
4. 마지막으로 3번에서 구한 값을 전부 다 더한 후 N으로 나눠 평균값을 구한다. (전체 포인트의 갯수)

- 이 모든 과정이 NumPy 라이브러리의 `var()` 메소드로 구현 가능하다.

```py
dataset = [3, 5, -2, 49, 10]
variance = np.var(dataset)

import numpy as np
import matplotlib.pyplot as plt

teacher_one_grades = [80.24, 81.15, 81.29,
    82.12, 82.52, 82.54, 82.76, 83.37, 83.42,
    83.45, 83.47, 83.79, 83.91, 83.98, 84.03,
    84.69, 84.74, 84.89, 84.95, 84.95, 85.02,
    85.18, 85.53, 86.29, 86.83, 87.29, 87.47,
    87.62, 88.04, 88.5]

teacher_two_grades = [65.82, 70.77, 71.46,
    73.63, 74.62, 76.53, 76.86, 77.06, 78.46,
    79.81, 80.64, 81.61, 81.84, 83.67, 84.44,
    84.73, 84.74, 85.15, 86.55, 88.06, 88.53,
    90.12, 91.27, 91.62, 92.86, 94.37, 95.64,
    95.99, 97.69, 104.4]

# NumPy의 var 메소드를 이용,
# 각각의 분산값을 각각의 변수에 저장
teacher_one_variance = np.var(teacher_one_grades)
teacher_two_variance = np.var(teacher_two_grades)

# plot
plt.hist(teacher_one_grades, alpha = 0.75,
    label = "Teacher 1 Scores", bins = 7)

plt.hist(teacher_two_grades, alpha = 0.5,
    label = "Teacher 2 Scores", bins = 30)

plt.title("Student test grades in two classes")
plt.xlabel("Grades")
plt.legend()
plt.show()

# print
print(np.mean(teacher_one_grades))
>>> 84.46766666666666

print(np.mean(teacher_two_grades))
>>> 84.29799999999999

print(teacher_one_variance)
>>> 4.266517888888889

print(teacher_two_variance)
>>> 78.13198933333337
```

![grades](https://i.imgur.com/t7QUAfT.png)

## Standard Deviation

- Variance(분산값)은 데이터 혹은 평균값의 단위와 달라서 사용하기 애매하다.
- 하지만 variance는 데이터에서 평균값을 뺀 수의 제곱이기 때문에 사실상 같은 단위라고 봐도 무방하다. (여전히 단위는 다르다고 해야한다.)
- Standard Deviation(표준편차)은 Variance(분산값)의 제곱근이다.
  - `sigma`는 보통 표준편차를 나타낼 때 사용되는 기호다.
  따라서 `sigma`의 제곱은 variance이다.

$$σ = \sqrt{σ^2} = \sqrt{∑_{i=1}^N(X_i−μ)^2\over{N}}$$

>파이썬에서 제곱근을 나타내는 식은 `** 0.5` 이다.

```py
num = 25
print(num ** 0.5)
>>> 5
```

## Using Standard Deviation

- Variance와는 다르게 Standard Deviation은 단위가 매칭되어서 비교가 가능하다.
- 표준편차는 세단계가 있다.
  - +/- 1 : 68.3%의 데이터가 분포되어있다.
  - +/- 2 : 95.5%의 데이터가 분포되어있다.
  - +/- 3 : 99.7%의 데이터가 분포되어있다.
- 3 standard deviation이 넘는 데이터는 말도안되게 비정상적인 데이터다.
