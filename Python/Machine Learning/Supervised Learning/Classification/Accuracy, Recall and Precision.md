# Accuracy, Recall, Precision, and F1 Score

## Accuracy

분류를 위한 머신러닝 알고리즘을 만든 후 해야할일은 예측력을 계산하는 것이다. 이러한 통계를 계산하려면 데이터를 훈련세트와 검증세트로 분리해야한다.

머신러닝 알고리즘을 사용하여 테스트에서 B 이상을 달성할지에 대한 여부를 예측하려고 한다고 가정해보자. 데이터 변수는 아래와 같이 생겼다.

- 이번 주에 공부한 시간
- 이번 주에 Netflix를 시청한 시간
- 시험 전날 잠든시간
- 시험 보기 전 모의고사 점수

알고리즘의 효과를 보고하는 가장 간단한 방법은 정확도를 계산하는 것이다. 정확도는 올바르게 분류된 포인트들의 개수를 찾아 전체 포인트의 개수로 나누는 것이다.

$$True\ P + True\ N \over True\ P + True\ N + False\ P + False\ N$$

- True P(ositive): 알고리즘이 B 이상을 예측했고, 실제로 B 이상을 받았을 때
- True N(egative): 알고리즘이 B 미만을 예측했고, 실제로 B 미만을 받았을 때
- False P(ositive): 알고리즘이 B 이상을 예측했지만 실제로 B 이상을 받지 못했을 때
- False N(egative): 알고리즘이 B 미만을 예측했지만 실제로 B 이상을 받았을 때

```py
labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

## 1. 네개의 변수를 설정
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

## 2. labels와 guesses loop
for i, j in zip(labels, guesses):
    # labels와 guesses의 요소가 동일하고
    # 예측값이 B 이상일 때
    if i == 1 and j == 1:
        true_positives += 1

    # labels와 guesses의 요소가 동일하고
    # 예측값이 B 미만일 때
    elif i == 0 and j == 0:
        true_negatives += 1

    # labels와 guesses의 요소가 다르고
    # 예측값이 실제값보다 클 때
    elif i < j:
        false_positives += 1

    # labels와 guesses의 요소가 다르고
    # 예측값보다 실제값이 더 클 때
    else:
        false_negatives += 1

accuracy = (true_positives + true_negatives)
    / (true_positives + true_negatives
    + false_positives + false_negatives)
```

## Recall

정확도는 데이터에 따라 매우 잘못된 통계일 수 있다. 만약 내일 1미터 이상의 눈이 쌓일지에 대한 여부를 예측하려는 알고리즘이 있다고 가정해보자. 그냥 항상 `False`를 예측하면 꽤나 정확한 분류자가 작성되었다. --- 이정도로 눈이 많이 내리는 날은 거의 없다. 그러니 이 분류자는 우리가 실제로 관심있어하는 정보를 찾아주지 않는다.

이 경우 도움이 되는 통계는 *recall*이다. Recall은 classifier(분류자)가 찾은 관련 항목의 백분율을 측정한다. 이 예에서 recall은 알고리즘이 올바르게 예측한 눈이 1미터 이상 오는 날의 숫자를 예측한 총 숫자로 나눈 값이다.

$$True\ P \over True\ P + False\ N$$

항상 `False`를 예측하는 알고리즘은 정확도가 매우 높지만 True Positive를 찾을 수 없으므로 리콜값은 `0`이다. 이런 터무니없는 분류자의 리콜은 매우낮아야한다.

## Precision

불행히도 recall도 완벽한 통계는 아니다. 예를들어, 항상 `True`를 반환하는 classifier를 만들 수 있다. 정확도는 낮지만 눈이 많이 올 때마다 정확하게 찾을 수 있기 때문에 recall값은 `1`이된다. 그러나 이 classifier는 이전의 경우만큼 의미도없고 터무니도없다. 알고리즘의 결함이 있음을 보여주는 통계는 바로 *precision* 정밀도이다.

눈 오는 날 예시에서 precision 정밀도는 올바르게 예측된 숫자를 눈이 올것이라고 예측한 숫자를 나눈 값이다.

$$True\ P \over True\ P + False\ P$$

매일 눈이 오는 날을 예측하는 알고리즘은 recall값이 `1`이지만 정확도는 매우낮다. 눈이 오는 날은 제대로 예측하지만 오탐이 너무 많다.

Precision과 Recall은 서로 반비례한다.

## F1 Score

알고리즘의 precision과 recall을 계산하는것이 유용하지만 알고리즘의 효과를 충분히 설명할 수 있는 숫자는 아직 없다. F1 Score가 그 역할을한다. F1점수는 정밀도와 리콜의 조화평균이다. 숫자들 사이에서 조화평균은 전체의 평균을 구하는 방법이다.

$$2 * {Precision * Recall \over Precision + Recall}$$

F1 점수는 정밀도와 리콜을 한개의 숫자로 통합한다. 일반적인 평균보다 조화평균을 더 많이 쓰는데 정밀도 또는 리콜이 `0`일 때 F1점수가 낮은값을 갖기를 원하기 때문이다.

예를들어 `recall = 1`이고 `precision = 0.01`일 때 정밀도가 너무 낮아 문제가있고, F1점수가 이걸 반영하게 하고 싶을 때

일반적인 평균값은 아래와같다.
$${1+0.01 \over 2} = 0.505$$

정밀도가 0.01인데 너무 높은값이 나온다. 그래서 조화평균을 사용해야한다.
$$2 * {1 * 0.01 \over 1 + 0.01} = 0.019$$

훨씬 합리적인 값이 나온다. F1점수는 이제 이 classifier의 효과를 정확하게 설명할 수 있다.

## scikit-learn

파이썬 `scikit-learn` 라이브러리에는 accuracy, recall, precision, F1을 계산해주는 메소드가있다. 각자 두개의 매개변수를 받는다. 실제 레이블의 list와 분류된 예측값의 list

```py
# 라이브러리 불러오기
from sklearn.metrics 
    import accuracy_score, recall_score, 
    precision_score, f1_score

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

print(accuracy_score(labels, guesses))
print(recall_score(labels, guesses))
print(precision_score(labels, guesses))
print(f1_score(labels, guesses))
```