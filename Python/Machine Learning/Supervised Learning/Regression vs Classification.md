# Regression vs Classification

Supervised Learning(학습모델)에는 두가지의 주요한 타입이있다.

1. *Regression* - 회귀 모델
2. *Classification* - 분류 모델

## Regression

회귀모델은 연속적인 숫자(실수)를 예측하는 것이다.

- 예를들어:
  - 특정 인물의 교육 수준, 나이등을 고려해 연봉을 예측하는 것
  - 나이와 몸무게등을 고려해 키를 예측하는 것
  - 특정 인물의 나이와 초고속 인터넷 사용가능 여부를 놓고 급여를 예측하는 것
  - 자동차의 연식과 크기에 기반해 연비를 예측하는 것

![gif](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/regression_v_classification/regression.gif)

- 출력값에 연속성이 있다면 Regression모델이라고 볼 수 있다.

Linear Regression은 가장 널리 사용되고 있는 Regression 알고리즘이다. 사업과 관련된 예로는 고객이 이탈할 가능성 또는 고객이 창출할 수익을 예측하는데 사용될 수 있다. 복잡한 모델이 이경우에 더 적합하다. 하지만 단순성을 잃는다.

## Classification

Classification은 *불연속적인* 데이터를 예측하는데 사용된다. 출력값(결과)는 무한한 값이 아니다. 대부분의 상황에서 가능한 결과는 두가지 뿐이고, 이를 **Binary Classification**(이진분류)라고 부른다. (True/False, 0 or 1, Man/Woman)

- 예를들어:
  - 이메일이 스팸인지 아닌지 예측
  - 비가 올지 안올지 예측
  - 사용자가 헤비유저인지 캐주얼유저인지 예측

**Multi-label Classification**은 나올 수 있는 예측값이 여러개가 있을 때 사용된다.

고객 분류, 이미지 카테고리 분류, 텍스트 이해를 위한 감정분석 등에 유용하다.

이러한 분류를 수행하기 위해 **Naive Bayes**, **K-Nearest Neighbors**, **SVM**과 같은 모델을 사용할 수 있다.

![gif](https://s3.amazonaws.com/codecademy-content/programs/machine-learning/regression_v_classification/classification.gif)
