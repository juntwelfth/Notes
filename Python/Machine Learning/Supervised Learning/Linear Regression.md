# Linear Regression

## Introduction to Linear Regression

- 머신러닝의 주된 목적은 일상에 존재하는 데이터들을 예측하기 위함이다.
- Linear Regression(선형회귀)의 몇가지 예
  - 집값과 평당 가격이 표본으로 있고, 집의 크기가 주어졌을 때 가격 예측하기
  - GDP를 놓고 GDP에 따른 세금 예측하기
  - 과자봉지에 남은 과자와 이미 먹은 과자가 주어졌을 때 이 과자가 얼마나 더 오래갈지 예측하기

- 야구선수의 키와 몸무게
![사진](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/weight_height.png)

- 아래와 같이 선을 그릴 수 있다.
![사진](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/weight_height_line.png)

## Points and Lines

- 선은 선의 **slope**, **intercept**에 따라 결정된다.
- 다르게 말하자면, 각각의 좌표 위 y는

$$y = mx + b$$

- `m` : slope, `b` : intercept, `y` : y축에 주어진 좌표, `x` : x축에 주어진 좌표
  - **slope** : 선이 얼마나 기울어져있는지
  - **intercept** : 선이 y축과 어디서 만나는지

- Linear Regression의 목표는 최적의 `m`과 `b`를 찾는것이다.

```py
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 12
#intercept:
b = 40

y = [month * m + b for month in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()
```

![Figure1](https://i.imgur.com/PYIVOBS.png)

## Loss

- 머신러닝에서는 목표를 잘 당성했는지 나타내는 값을 잡는다.
- 학습을 통해 직접적으로 줄이고자 하는 값을 Loss(손실)이라고 한다.
- 학습을 통해 목표를 얼마나 못 달성했는지 나타내는 값을 Error(에러)라고 한다.
- Loss function(손실함수)은 Cost function(비용함수)라고도 불린다.
- 각 좌표에서 선까지의 거리를 제곱한 후에 더해준다.

![사진](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/linear-regression/points.svg)

>좌표 A는 3만큼 벗어났으니깐 9 ($3^2$), B는 1이다.

- 위 예시에선 총 손실값이 10이다. 만약 우리가 총 손실값이 10보다 적은 경우를 찾으면 더 좋겠지..

```py
x = [1, 2, 3]
y = [5, 1, 3]

# y = x
m1 = 1
b1 = 0

# y = 0.5x + 1
m2 = 0.5
b2 = 1

y_predicted1 = [x * m1 + b1 for x in x]
y_predicted2 = [x * m2 + b2 for x in x]

total_loss1 = 0

for i in range(len(y)):
    total_loss1 += (y[i] - y_predicted1[i]) ** 2

total_loss2 = 0

for i in range(len(y)):
    total_loss2 += (y[i] - y_predicted2[i]) ** 2

print(total_loss1)
print(total_loss2)

better_fit = 2
```

## Minimizing Loss

- Linear Regression Model (선형회귀모델)의 목표는 모든 데이터의 평균 손실값을 최소로하는 slope값과 intercept값을 찾는것이다.

[About Minimizing Loss](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/line-fitter/line-fitter.html)

## Gradient Descent for Intercept

- 우리가 손실값을 최소화하려고 할 때, 각 매개변수를 바꾸고 움직이면서 손실값을 줄이는데
- 마치 언덕을 내려가는 것 같이 최저점에 다닿으면 멈추는것이다.
- 이러한 것을 Gradient Descent라고 부른다.

- `N`은 데이터셋에서 좌표를 뜻한다.
- `m`은 현재 gradient guess를 뜻한다.
- `b`는 현재 intercept guess를 뜻한다.

![Loss vs b value](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/loss_curve.svg)

- 예를 들어, 우리가 intercept를 찾고있는데 intercept를 `10`이라고 가정했을 때 더 내려갈 수 있는 공간이 있으므로 intercept값을 높여준다.

  ![Loss vs b value](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/Linear_regression_gif_1.gif)

- `b`를 구하는 식

$$\frac{2}{N}\sum_{i=1}^{N}-(y_i-(mx_i+b))$$

```py
def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)

    for i in range(N):
        y_val = y[i]
        x_val = x[i]

        diff += (y_val - ((m * x_val) + b))

    b_gradient = -2/N * diff

    return b_gradient
```

## Gradient Descent for Slope

- `m`을 구하는 식
- `x_value * (y_value - (m * x_value + b))`

$$\frac{2}{N}\sum_{i=1}^{N}-x_i(y_i-(mx_i+b))$$

```py
def get_gradient_at_m(x, y, m, b):
    diff = 0
    N = len(x)

    for i in range(N):
        x_val = x[i]
        y_val = y[i]

        diff += x_val * (y_val - (m * x_val + b))

    m_gradient = -2 / N * diff

    return m_gradient
```

## Put it Together

- `new_b = current_b - (learning_rate * b_gradient)`

```py
def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -(2/N) * diff
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff
    return m_gradient

def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)

    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)

    return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0
b, m = step_gradient(months, revenue, b, m)
# Call your function here to update b and m
print(b, m)    # 2.355, 17.78333333333333
```

## Convergence

- 최적의 m(slope)과 b(intercept)를 찾기 위해선 convergence를 정의해야한다.
- Convergence는 매개변수를 바꾸는데 손실값이 더이상 변하지 않을 때 혹은 현저히 느리게 변하기 시작할 때를 말한다.

![img](https://i.imgur.com/R55sltg.png)

- 이러한 그래프가 있을 때 iterations의 convergence는 800, b는 47(즈음)이다.

## Learning Rate

- 최적의 `m` 값과 `b` 값을 찾을 때 추정값을 설정하는데, 추정값의 간격을 설정해야한다.
- 간격을 설정할 땐 learning rate를 설정해야 한다.
- learning rate가 너무 작은 숫자이면 값을 얻어내는데에 오랜 시간이 걸린다. (값을 얻어내기 전에 시스템이 종료될 수 있음)
- learning rate가 너무 큰 숫자이면 최적의 값을 스킵할수도 있다. (값을 아예 못 얻어낼 수도 있다.) Oh NO!!!

![Learning Rate too Large](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/Linear_regression_gif_2.gif)

모델 학습에 최적의 learning rate를 찾는것이 필수는 아니다.

대충 적당한 learning rate를 찾기만 하면 된다.

## Put it Together II

- 여태까지 배운것들과 learning rate를 함께 사용하는 방법

```py

import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -(2/N) * diff
    return b_gradient

def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff
    return m_gradient

def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0

    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)

    return b, m

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()
```

![Imgur](https://i.imgur.com/UGrCUho.png)

## Use Your Functions on Real Data

- 실제 데이터를 가지고 만들어보기

```py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

b, m = gradient_descent(X, y, num_iterations=1000, learning_rate=0.0001)

y_predictions = [x * m + b for x in X]


plt.plot(X, y, 'o')
plt.plot(X, y_predictions)

plt.show()
```

![Imgur](https://i.imgur.com/XxuDLII.png)

## Scikit-Learn

- 위의 모든 과정이 파이썬 Scikit-Learn 라이브러리에 존재하는 메소드로 해결이 가능하다.
- `linear_model` 모듈안에 `LinearRegression()`이라는 함수가 존재한다.

```py
from sklearn.linear_model import LinearRegression
```

- 먼저 `LinearRegression` 모델을 생성한 후 `x`와 `y`값에 `fit`을 해준다.

```py
line_fitter = LinearRegression()
line_fitter.fit(X, y)
```

- `fit()` 메소드는 두개의 유용한 변수를 반환한다.
  1. `line_fitter.coef_` : slope (m)
  2. `line_fitter.intercept_` : intercept (b)

- 또한 `predict()` 함수를 사용해서 x값을 전달해 y값의 추정값을 알아내는 방법도 있다.

```py
y_predicted = line_fitter.predict(X)
```

- `num_iterations`, `learning_rate`는 scikit-learn에 기본값이 내장되어있기 때문에 신경쓰지 않아도 된다.

```py

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28,
  30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)

sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales_predict)

plt.plot(temperature, sales, 'o')
plt.show()
```

1. `line_fitter = LinearRegression()`으로 먼저 `sklearn` linear regression 모델을 만든다.

2. `fit` 메소드를 이용해 `temperature`와 `sales`를 설정한다.

3. `temperature`에 대한 `sales`의 추정값을 `sales_predict`에 저장한다.
(`predict()` 메소드 사용)

![Imgur](https://i.imgur.com/KgpMTBP.png)
