# Training Set vs Validation Set vs Test Set

## Testing

**Supervised Machine Learning Algorithms**은 분류와 예측을 수행할 수 있는 어메이징한 도구다. 그러나 이러한 예측이 얼마나 정확한지 자문해보는 것이 중요하다. 결국 누가 분류하냐에 따라 이러한 예측들이 틀린것일 수도 있다는것이다. 운좋게도 **supervised machine learning algorithms**에는 이미 사전 정의된 데이터 포인트의 데이터셋이 있다는 점을 활용할 수 있다.

- 알고리즘의 효과를 테스트하기 위해 데이터를 다음과 같이 나눠준다.
  - training set
  - validation set
  - test set

## Training Set vs Validation Set

**Training set**는 알고리즘이 학습할 데이터이다. 학습은 어떤 알고리즘을 사용하냐에 따라 다르게 보여진다.

예를 들어 선형회귀를 사용할 때 **Training set**의 포인트들은 최적의 선을 그리기 위해 사용된다.
**K-Nearest Neighbors**에서 **Training set**의 포인트들은 인접한 포인트들이 된다.

**Training set**를 이용하여 훈련을 한 후, **validation set**의 포인트들이 분류의 정확도 또는 오류를 계산하는데 사용된다. 여기서 중요한점은 **validation set**에 존재하는 모든 데이터 푀인트들의 실제 이름을 알고 있지만 모르는 척 하는것이다. **validation set**의 모든 포인트들을 **classifier**의 인풋으로 사용할 수 있다. 그런 다음 해당 포인트에 대한 분류를 얻는다. 이제 **validation set**의 실제 라벨을 볼 수 있으며 올바른지 여부를 확인할 수 있다. **validation set**의 모든 포인트들에 대해 이 작업을 수행하면 유효성 검사 오류를 계산할 수 있다.

## N-Fold Cross-Validation

가끔씩 데이터셋이 너무 작아서 80/20으로 나눠도 여전히 분산되어있는 경우가 있다. 이럴 때 **N-Fold Cross-Validation**을 사용하면 된다. 중요한 점은 전체 과정을 N번 수행하고 정확도를 평균한다는 것이다.

예를들어 **10-fold cross-validation**에서 처음 10%의 데이터를 **validation set**으로 설정하고 정확도, 정밀도, 리콜 및 F1 점수를 계산한다. 그런다음 **validation set**을 데이터의 두번째 10%로 설정하고 다시 계산한다. 이 과정을 열번 반복하고 모든 정확도의 평균을 계산하면 모델의 평균 성능이 얼마나 좋은지 알아낼 수 있다.

![10-fold](https://s3.amazonaws.com/codecademy-content/programs/data-science-path/cross_validation.svg)
