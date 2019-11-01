# Multiple Linear Regression

## Introduction

**Linear Regression**(*선형회귀*)은 다른 변수와의 관계에서 변수의 값을 예측하고 싶을 때 유용하다.

예를들어, 집값을 예측할 때 고려해야 할 한가지 요인은 집의 크기이다.

가격이라는 변수와 크기라는 변수 사이의 관계는 중요하다. 하지만 집값을 결정하는 요인에는 *위치*, *대기 질*, *인구통계*, *주차장* 등등 다양하다.

이런식으로 종속변수를 사용하여 집값을 예측하는 경우 **Multiple Linear Regression**을 사용한다.

**Multiple Linear Regression**은 두개이상의 독립 변수를 사용해 종속변수의 값을 예측하는데 사용되고, 아래의 수식을 사용한다.

$$y = b + m_1x_1 + m_2x_2 + ... + m_nx_n$$

## Training Set vs Test Set

대부분의 머신러닝 알고리즘과 같이 데이터셋을 나눠야한다.

- **Training Set**: 모델에 맞는 데이터
- **Test Set**: 처음 테스트 할 때 분할된 데이터

![set vs set](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/multiple-linear-regression/split.svg)

보통, *Training Set*엔 80%, *Test Set*에 20%를 배치하는것이 좋다.

`x`와 `y`값을 가지고 있다고 가정해보자.

```py
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =
    train_test_split(x, y, train_size=0.8, test_size=0.2)
```

- `train_size`: Train Set에 사용할 비율 (0.0 ~ 1.0)
- `test_size`: Test Set에 사용할 비율 (0.0 ~ 1.0)
- `random_state`: 난수 생성시 사용할 시드 (optional)

## Scikit-Learn

**Multiple Linear Regression**(다중 선형 회귀)은 **Linear Regression** 할 때와 똑같이 `linear_model`에서 `LinearRegression`을 import해주면 된다.

```py
from sklearn.linear_model import LinearRegression
```

`LinearRegression` 모델을 만든 후 `fit` 메소드에 `x_train`과 `y_train` 데이터를 전달해준다.

```py
mlr = LinearRegression()

mlr.fit(x_train, y_train)
# finds the coefficients and the intercept value
```

또한 `predict()`를 이용해 x값을 전달하면 y값의 추정치가 반환된다.

```py
y_predicted = mlr.predict(x_text)
# takes values calculated by `.fit()` and the `x` values,
# plugs them into the multiple linear regression equation,
# and calculates the predicted y values.
```

전부다 합치면 아래와 같이 생겼다.

```py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# Street Easy라는 홈페이지에서 제공하는 맨하탄 집값 정보
streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# 이렇게 총 14개의 columns를 x에 넣어주기
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway',
        'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
        'has_washer_dryer', 'has_doorman', 'has_elevator',
        'has_dishwasher', 'has_patio', 'has_gym']]

# df에서 rent는 y에 넣어주기
y = df[['rent']]

# x, y, train split(80%), test split(20%), random seed
x_train, x_test, y_train, y_test =
    train_test_split(x, y, train_size = 0.8, test_size = 0.2,
        random_state=6)

# 먼저 LinearRegression을 열어주고(?)
mlr = LinearRegression()
# 각각 데이터에서 train set(훈련셋)를 적용시켜준다.
mlr.fit(x_train, y_train)
# x의 테스트셋을 넣어주면 y의 추정값이 반환된다.
y_predict = mlr.predict(x_test)

# 우리집 테스트
my_house = [[6, 2, 2704.32, 7, 2, 50, 1, 0, 1, 0, 0, 0, 1, 0]]
predict = mlr.predict(my_house)
```

## Equation

다시한번, 두개 이상의 독립 변수를 사용하는 다중 선형 회귀의 방정식은 다음과 같다.

$$y = b + m_1x_1 + m_2x_2 + ... + m_nx_n$$

- $m_1$, $m_2$, $m_3$ ... $m_n$ : **coefficients** (계수)
- *b* : **intercept**

이 값들을 통해 y의 추정치를 얻을 수 있다.

다시, `sklearn`의 `LinearRegression()` 메소드를 이용해 이러한 값들을 쉽게 얻을 수 있다.

`fit()` 메소드는 모델에 유용한 두개의 변수를 반환한다.

- `.coef_` : coefficients
- `.intercept_` : intercept

**Coefficients**는 어떤 독립 변수가 더 많은 무게를 가지고 있는지 결정하는데 도움이된다.

예를들어 -1.345의 coefficient는 0.238의 coefficient보다 렌트 가격에 더 많은 영향을 미치며, 전자는 가격에 부정적인 영향을 미치고, 후자는 가격에 긍정적인 영향을 미친다.

## Correlations

Manhattan Model에서 14개의 변수가 있었다. 이 14개의 변수가 곧 coefficient다.

```py
[ -302.73009383  1199.3859951  4.79976742
  -24.28993151  24.19824177  -7.58272473
  -140.90664773  48.85017415  191.4257324
  -151.11453388  89.408889  -57.89714551
  -19.31948556  -38.92369828 ]
```

- 차례대로
  - `bedrooms` - 침실 개수
  - `bathrooms` - 화장실 개수
  - `size_sqft` - 평방피트 (평 x 35.583)
  - `min_to_subway` - 지하철 역까지 도보 소요시간
  - `floor` - 층 수
  - `building_age_yrs` - 건물 나이
  - `no_fee` - 중개수수료 유무 (0 / 1)
  - `has_roofdeck` - 루프덱 유무 (0 / 1)
  - `has_washer_dryer` - 세탁기 유무 (0 / 1)
  - `has_doorman` - 도어맨 유무 (0 / 1)
  - `has_elevator` - 엘리베이터 유무 (0 / 1)
  - `has_dishwasher` - 식기세척기 유무 (0 / 1)
  - `has_patio` - 안마당 유무 (0 / 1)
  - `has_gym` - 헬스장 유무 (0 / 1)

이 요소들이 가격에 실질적으로 영향을 미치지 않는것이 있는지 rent와 비교해서 그래프로 나타내봐야 한다.

### Interpreting graphs

회귀분석에서 독립변수는 종속변수와 양의 선형관계를 갖거나 음의 선형관계를 갖거나 아예 관계가 없다.

***음의 선형관계는 X값이 증가하면 Y값이 감소하는 것을 의미한다.***

***양의 선형관계는 X값이 증가하면 Y값도 증가하는 것을 의미한다.***

그래프를 봤을 때 하락추세가 보이면 음의 선형관계가 존재한다는 의미이다.
반대로 상승추세가 보이면 양의 선형관계가 존재한다는 의미이다.

![graphs](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/multiple-linear-regression/correlations.png)

왼쪽은 양의 선형관계, 오른쪽은 음의 선형관계
***Positive Linear Relationship***, ***Negative Linear Relationship***

## Evaluating the Model's Accuracy

**Multiple Linear Regression** 모델의 정확도를 평가하려고 할 때 사용할 수 있는 기술 중 하나는 **Residual Analysis**이다.

실제 값 y와 예측 값 ŷ의 차이는 **residual e**이다.

$$e = y - ŷ$$

StreetEasy 데이터셋에서 실제 임대료는 y, 예측 임대료는 ŷ이다. 실제 임대료 y는 이러한 예측된 임대료 ŷ와 매우 비슷해야한다.

`sklearn`의 `linear_model.LinearRegression`에 있는 `score()` 메소드는 예측값의 the coefficient of determination R²를 반환한다. (결정계수 R²)

$$1 - {u \over v}$$

여기서 u는 residual 제곱의 합이다.

```py
((y - y_predict) ** 2).sum()
```

v는 제곱의 총 합이다. (TSS)

```py
((y - y.mean()) ** 2).sum()
```

*TSS는 y 변수에 얼마나 많은 변화가 있는지 알려준다.*

*R²은 모든 x 변수에 의해 설명된 y의 백분율 변동이다.*

예를 들어, 평방피트와 침실 개수를 기준으로 임대료를 예측하려고 할 때,
R²는 0.72가 된다. --- 모든 x 변수 (평방피트, 침실 수)가 임대료의 72% 변동을 뜻한다.

x 변수에 건물의 나이를 추가하면 이 세번째 x 변수가 추가됨에의해 R²값이 올라갈 것으로 예상할 수 있다.

새로운 R²값이 0.95라고 해보자. --- 평방피트, 침실 수 그리고 건물의 나이가 임대료 변동에 95%의 영향을 미친다는 것을 뜻한다.

가장 좋은 R²값은 1.00이다. (음수가 될 수도 있다.) 일반적으로 0.7의 R²값은 양호한것으로 간주한다.

```py
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway',
    'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
    'has_washer_dryer', 'has_doorman', 'has_elevator',
    'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test =
    train_test_split(x, y, train_size = 0.8,
        test_size = 0.2, random_state=6)

mlr = LinearRegression()

model=mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

# R²값 출력
print(mlr.score(x_train, y_train))  # 0.772
print(mlr.score(x_test, y_test))    # 0.805
```
