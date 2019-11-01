# Normalization

## Why

많은 머신러닝 알고리즘은 features의 데이터 포인트를 비교하여 트렌트를 찾으려고 한다.

그런데 feature의 규모가 다른경우 문제가 생긴다.

예를들어 주택의 데이터셋을 고려할 때, 두가지 잠재적 특징은 방의 개수와 집이 언제지어졌는지 이 두가지일 것이다. 머신러닝 알고리즘은 어느집이 가장 적합한지 예측하려고 시도할 수 있다.

알고리즘이 데이터포인트를 비교할 때, 더 큰 스케일을 가진 feature가 다른 feature를 완전히 지배한다.

![pic1](https://s3.amazonaws.com/codecademy-content/courses/normalization/unnormalized.png)

이런식으로 데이터가 찌그러진다.

알고리즘은 2개의 방이있는 집과 20개의 방이있는 집 사이에 큰 차이가 있음을 인지해야한다. 하지만 두개의 서로 다른 집이 100년의 차이가 있을 수도 있다. 이 경우 객실 숫자의 차이는 전체 변화에 덜 영향을 끼친다.

더 극단적인 예로는 x축이 집의 비용이라고 생각해보자. 데이터는 더 찌그러질 것이다. 두 집의 집값이 수천달러의 차이를 가질 수 있기 때문에 객실수의 차이는 그다지 중요하지 않다.

Normalization의 목표는 모든 데이터 포인트가 동일한 스케일을 갖도록해 각 기능이 똑같이 중요하게 여겨지게 하는 것이다.

![normalized](https://s3.amazonaws.com/codecademy-content/courses/normalization/normalized.png)

> Normalized된 데이터

## Min-Max Normalization

Min-Max Normalization은 데이터를 정규화하는 가장 흔한 방법중 하나다. 모든 요인에대해 해당 요인의 최저점이 0이되고 최고점이 1이된다. 그리고 다른 모든 값은 0과 1 사이의 소수점으로 표현된다.

예를들어 최소값이 20이고 최대값이 40인 경우 30의 값은 0.5로 변환된다.

$$value - min \over max - min$$

Min-Max Normalization에는 상당히 중요한 단점이 있다. outlier(특이치)를 잘 처리하지 못한다는 것이다.

예를들어 0과 40 사이에 99개의 값이 있고 나머지 하나의 값이 100이라면 99개의 값이 모두 0 ~ 0.4 사이의 값으로 변환된다.

그리고 마찬가지로 찌그러졌다.

![n](https://s3.amazonaws.com/codecademy-content/courses/normalization/outlier.png)

정규화는 y축 찌그러짐은 해결했지만 x축 찌그러짐은 해결하지 못했다. 이 상황에서 데이터 포인트들을 비교한다면 y축이 압도적일 것이다. y축은 1씩 다를 수 있지만 x축은 0.4만 다를 수 있기 때문이다.

## Z-Score Normalization

Z-Score 정규화는 이 특이치 문제를 피할 수 있는 정규화 방법이다.

$$value - \mu \over \sigma$$

여기서 μ는 변수의 평균값, σ는 변수의 표준편차이다. 값이 변수의 모든 값의 평균과 정확히 같으면 0으로 normalized된다. 만약 이 값이 평균보다 낮으면 음수가되고 평균보다 크면 양수가된다. 이러한 음수 및 양수의 크기는 원래 변수의 표준편차에 의해 결정된다. 정규화되지 않은 데이터의 표준편차가 크면 정규화된 값이 0에 가까워진다.

![n2](https://s3.amazonaws.com/codecademy-content/courses/normalization/z-score.png)

데이터가 여전히 찌그러져 보이지만 데이터 포인트들은 두 변수에 대해 거의 동일한 척도로 나타난다. --- 거의 모든 포인트들은 x축과 y축 모두에서 -2 ~ 2 사이이다. 유일한 단점은 변수의 크기가 정확히 동일하지 않다는 것이다.

Min-Max 정규화를 통해 두 변수를 모두 0과 1 사이로 재구성 할 수 있었다. Z-Score 정규화를 사용하면 x축의 범위는 약 -1.5 ~ 1.5이고 y축의 범위는 약 -2 ~ 2가된다. 이 값은 이전보다 확실히 낫다. 0부터 40 사이 범위를 가졌던 x축은 더이상 y축을 지배하지 않는다.
