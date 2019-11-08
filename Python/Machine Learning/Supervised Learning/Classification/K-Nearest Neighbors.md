# K-Nearest Neighbors Classifier

**K-Nearest Neighbors**(KNN)는 분류하는 알고리즘이다. 포인트는 유사한 속성을 가진 데이터 포인트가 유사한 범주에 속하는 경향이 있다는 것이다.

![knn](https://s3.amazonaws.com/codecademy-content/courses/learn-knn/nearest_neighbor.gif)

위 사진에서 모든 포인트들은 `x`값과 `y`값을 가지고있다. 2차원 함수 위에 그려질 수 있다는 뜻이다.

각각의 색깔은 KNN 알고리즘이 분류를 하려고 시도하는 클래스들을 나타낸다. 위 사진에서 데이터들은 `green` 클래스 혹은 `red` 클래스에 속해있다. 하얀색 데이터 포인트는 아직 클래스가 정의되지 않았다는 뜻이다. 알고리즘의 목표는 이러한 하얀색 포인트들을 분류하는 것이다.

다음으로 원의 크기가 점점 커지는것에 주목하자. `k = 3`일 때 두개의 초록색 점과 한개의 빨간색 점이 있다. 따라서 이 경우엔 알고리즘이 하얀색 포인트를 초록색으로 분류할것이다. 하지만 `k`를 `5`로 증가시키면 원도 늘어나고 분류도 바뀐다. 세개의 빨간점과 두개의 초록색점이 있기 때문에 하얀색 포인트는 빨간색으로 분류가된다.

이것이 KNN 알고리즘의 핵심포인트이다. 각 포인트의 클래스가 알려진 데이터셋이 있는 경우 알 수 없는 클래스로 새 포인트를 가져와서 가장 가까운 이웃들을 찾아 분류할 수 있다.

## Distance Between Points - 2D

우선 기본적으로 알수없는 점의 가장 가까운 `k`개의 이웃을 추정할 때 컴퓨터는 가장 가까운게 뭔지 알 수 없어서 수학적으로 접근을 해야한다.

$$\sqrt{(125-115)^2 + (1977-1981)^2} = 10.77$$

거리계산을 하는데, 여기서 거리란 두 점 사이의 간격이라는 뜻이라고 생각하면 되고 어떤 단위든지 다 가능하다.

## Distance Between Points - 3D

영화의 런닝타임과 출시연도만으로 영화등급 예측기를 만드는것은 꽤나 한정적이다. 영화에 관한 데이터는 많고 많다. 1차원을 더 추가해보자.

세번째 차원을 영화예산이라고 가정했을 때 이 두 점 사이의 거리를 3차원으로 찾아야한다.

![3D](https://codecademy-content.s3.amazonaws.com/courses/learn-knn/threed.png)

만약 우리가 3차원만으로 만족하지 못한다면 어떻게 해야할까? 안타깝게도, 3차원보다 더 높은 차원의 포인트를 시각화하는것은 매우 어렵다. 하지만 그렇다고해서 포인트 사이의 거리를 찾을 수 없다는 것을 의미하지는 않는다. (시각화가 어렵지 거리 구하는건 쉽다.)

$$\sqrt{(A_1-B_1)^2+(A_2-B_2)^2+...+(A_n-B_n)^2}$$

이러한 수식을 이용해 n개의 포인트를 이용, n차원의 공간에서 거리를 계산할 수 있게된다.

```py
# 런닝타임, 출시연도, 예산
star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
    diff = 0
    for i in range(len(movie1)):
        # 각각의 포인트의 차이를 제곱해서 더해주기
        diff += (movie1[i] - movie2[i]) ** 2
    # 루트해주기
    return diff ** 0.5
```

## Data with Different Scales: Normalization

세번째로 추가한 영화 예산에는 문제가있다.

출시연도와 영화예산 두가지를 놓고 비교해보자. 두 영화의 출시일 사이의 최대 차이는 약 125년이다. (Lumère Brothers는 1890년대에 영화를 만들었다.) 반면에 두 영화의 예산차이는 수백만달러가 넘을 수도 있다.

이러한 상황에서 발생하는 문제는 거리공식이 스케일이나 단위 상관없이 모든 숫자를 동일하게 취급한다는 것이다.

예를들어 1920년에 만들어진 영화와 2010년에 만들어진 영화는 90년이라는 엄청난 시간의 차이가 있음에도 불구하고 90이라는 숫자는 예산으로 생각하면 90원밖에 차이가 나지 않는 것이다. 말도안되는 수치다.

또, 예산이 그 무엇보다 숫자의 스케일이 가장 크기때문에 다른 차원의 데이터들의 중요성보다 훨씬 중요해진다는 말이다. 두 영화의 출시연도가 90년이 차이나는 것과 영화예산이 수백만달러가 차이나는것을 비교해봤자 아무 의미가 없을것이다.

이러한 문제점은 모든 데이터포인트가 0과 1 사이에 존재하게 만들면 된다. Min-Max 데이터 정규화를 사용하면 된다.

$$value-min\over max-min$$

```py
release_dates = [1897, 1998, 2000, 1948, 1962,
                 1950, 1975, 1960, 2017, 1937,
                 1968, 1996, 1944, 1891, 1995,
                 1948, 2011, 1965, 1891, 1978]

def min_max_normalize(lst):
    # 가장 작은 숫자
    minimum = min(lst)
    # 가장 큰 숫자
    maximum = max(lst)

    normalized = []

    for i in lst:
        # value - min을 max - min으로 나눠주기
        # Max-Min Normalization
        normalized.append(
            (i - minimum) / (maximum - minimum))

    return normalized
```

## Finding the Nearest Neighbors

이제 데이터가 정규화되었고 두 점 사이의 거리를 찾는 함수를 작성했으므로 알 수 없는 데이터들의 분류를 할 수 있게되었다.

이를 위해 분류되지 않은 특정 포인트에서 가장 가까운 이웃 `k`개를 찾아야한다.

가장 가까운 5개의 인접항목을 찾으려면 분류되지 않은 새로운 영화를 데이터셋의 다른 모든 영화와 비교해야한다. 이것은 우리가 거리공식을 반복해서 사용한다는 것을 의미한다. 우리는 궁극적으로 정렬된 거리 목록과 그 거리와 관련된 영화를 얻고싶다.

아래와 같이 생긴 결과를 얻고싶은 것이다.

```py
[
    [0.30, 'Superman II'],
    [0.31, 'Finding Nemo'],
    ...
    ...
    [0.38, 'Blazing Saddles']
]
```

```py
from movies import movie_dataset, movie_labels

# 위에서 이미 구현했던 거리구하는 함수
def distance(movie1, movie2):
    squared_difference = 0
    for i in range(len(movie1)):
        squared_difference +=
            (movie1[i] - movie2[i]) ** 2

    final_distance = squared_difference ** 0.5

    return final_distance

# 새로 구현한 k개의 인접항목을 구하는 함수
def classify(unknown, dataset, k):
    distances = []

    # Dictionary dataset에 있는
    # key를 title로 불러오기
    for title in dataset:
        # dataset[title] : value값 가져오기
        distance_to_point =
            distance(dataset[title], unknown)

        # 거리도 계산 후 리스트로 결과와 제목 추가
        distances.append(
            [distance_to_point, title])

    # 리스트 정렬 거리별로
    distances.sort()

    # 0부터 k번째까지 slice
    neighbors = distances[:k]
    return neighbors
```

## Count Neighbors

이제 `k`개의 인접항목을 찾아냈고 list로 저장했다.

```py
[
    [0.083, 'Lady Vengeance'],
    [0.236, 'Steamboy'],
    ...
    ...
    [0.331, 'Godzilla 2000']
]
```

우리의 목표는 이제 이 `k`개의 인접항목 목록에서 좋은영화와 나쁜영화의 수를 세는것이다. 만약 좋은영화의 수가 더 많으면 알고리즘은 이 영화를 좋은영화로 분류할 것이고 그 반대의 경우엔 나쁜영화로 분류할것이다.

만약 좋은영화의 수와 나쁜영화의 수가 같으면 어떻게 되는걸까? 만약 `k = 8`이고 4개의 인접항목이 좋은영화, 4개의 인접항목이 나쁜영화로 분류되어 있다면 결과는 어떻게될까? 여러 다른 방법들이 존재하지만 그 중 하나는 더 가까운 포인트에 있는 인접항목의 클래스를 선택하는 것이다.

```py
from movies import movie_dataset, movie_labels


# 위에서 이미 구현했던 거리구하는 함수
def distance(movie1, movie2):
    squared_difference = 0
    for i in range(len(movie1)):
        squared_difference +=
            (movie1[i] - movie2[i]) ** 2

    final_distance = squared_difference ** 0.5

    return final_distance

# 위에서 구현한 k개의 인접항목을 구하는 함수
def classify(unknown, dataset, k):
    distances = []
    num_good = 0
    num_bad = 0

    # Dictionary dataset에 있는
    # key를 title로 불러오기
    for title in dataset:
        # title제목을 가진 영화의 정보
        movie = dataset[title]

        # dataset[title] : value값 가져오기
        distance_to_point =
            distance(movie, unknown)

        # 거리도 계산 후 리스트로 결과와 제목 추가
        distances.append(
            [distance_to_point, title])

    # 리스트 정렬 거리별로
    distances.sort()

    # 0부터 k번째까지 slice
    neighbors = distances[:k]

    for movie in neighbors:
        title = movie[1]
        if labels[title] == 0:
            num_bad += 1
        elif labels[title] == 1:
            num_good += 1

    return 1 if num_good > num_bad else 0
```

## Training and Validation Sets

이제 분류 할 수있는 **K Nearest Neighbors**(KNN) 알고리즘을 구현했다. 데이터가 존재하지 않는 영화를 따로 알고리즘에 적용시켜 IMDb 등급이 7.0 이상인지 예측할 수 있다. 그리고 이 알고리즘이 얼마나 효과적인지 테스트를 해봐야한다.

대부분의 머신러닝 알고리즘과 마찬가지로 데이터를 training set, validation set로 나눠준다.

이 세트들이 생성되고나면 validation set에 있는 모든 포인트를 KNN알고리즘에 전달한다. 그 후 validation set에서 영화를 가져와 training set에 있는 모든 영화와 비교를하고 K Nearest Neighbors를 찾은 후 예측을한다. 예측을 한 후에 실제 답을 보고 올바른지 확인할 수 있다.

validation set에서 모든 동영상에 대해 이 작업을 수행하면 classifier가 정답을 얻은 횟수와 잘못된 정답을 얻은 횟수를 계산할 수 있게된다. 이 두 숫자를 이용, validation accuracy(유효성 검사 정확도)를 계산할 수 있다.

어떤 K를 사용하냐에 따라 정확도는 달라진다.

```py
from movies import training_set, training_labels, validation_set, validation_labels


def distance(movie1, movie2):
    squared_difference = 0
    for i in range(len(movie1)):
        squared_difference += (movie1[i] - movie2[i]) ** 2
    final_distance = squared_difference ** 0.5
    return final_distance


def classify(unknown, dataset, labels, k):
    distances = []
    # Looping through all points in the dataset
    for title in dataset:
        movie = dataset[title]
        distance_to_point = distance(movie, unknown)
        # Adding the distance and point associated with that distance
        distances.append([distance_to_point, title])
    distances.sort()
    # Taking only the k closest points
    neighbors = distances[0:k]
    num_good = 0
    num_bad = 0
    for neighbor in neighbors:
        title = neighbor[1]
        if labels[title] == 0:
            num_bad += 1
        elif labels[title] == 1:
            num_good += 1
    #-------- 여기까지 위와 동일
    # 정확도 검사
    if num_good > num_bad:
        return 1
    else:
        return 0
```

## Choosing K

`k`가 바뀌면 검사 정확도도 바뀌게된다. 첫번째로 고려해야 할 사항은 `k`가 매우 작은 경우다. `k = 1`일 때 *overfitting*(과적합)으로 인해 검사의 정확도가 상당히 낮을것이다. Overfitting은 머신러닝 알고리즘을 작성할 때 거의 항상 나오는 개념이다. Overfitting은 training set에 너무 의존할 때 발생한다. 실제 세계의 데이터는 항상 training set와 동일하게 작동한다고 가정해야한다. KNN에서 인접항목을 충분히 고려하지 않으면 overfitting이 발생한다. 한개의 특이치가 알수없는 포인트의 클래스를 결정지을 수 있기 때문이다.

![overfitting](https://s3.amazonaws.com/codecademy-content/courses/learn-knn/overfit.png)

왼쪽 상단의 진한 파란색 포인트는 누가봐도 특이치이다. `k = 1`일 때 일반영역의 모든 포인트는 초록색으로 분류되어야 하지만 진한 남색으로 분류된다. classifier가 training data의 작은 단점에 너무 크게 의존했기 때문이다.

반면에 `k`가 매우 크면 classifier는 underfitting을 겪게된다. underfitting은 분류 기준이 training set에서 작은 문제에 충분한 주의를 기울이지 않을 때 발생한다. `100`개의 포인트가 있고 `k = 100`이라고 가정해보자. 모든 포인트는 다 같은 방법으로 분류될 것이다. 포인트간의 거리는 중요하지 않아진다. 너무 극단적인 예지만 `k`가 너무 큰 경우 classifier가 training data를 이해하지 못하는 경우를 보여준다.

```py
def find_validation_accuracy(training_set,
    training_labels, validation_set,
    validation_labels, k):
      num_correct = 0.0

  for i in validation_set:
    guess = classify(validation_set[i], training_set, training_labels, k)
    if guess == validation_labels[i]:
      num_correct += 1
  return num_correct / len(validation_set)
```

## Graph of K

아래 그래프는 `k`가 증가함에 따라 검사의 정확도를 보여준다. `k`가 작으면 overfitting이 발생하고 정확도가 낮아진다. 반면에 `k`가 너무 커지면 underfitting이 발생하고 정확도가 다시 떨어지기 시작한다.

![graph](https://s3.amazonaws.com/codecademy-content/courses/learn-knn/k.png)

## sklearn

파이썬 `sklearn` 라이브러리엔 이 과정을 손쉽게 할 수 있는 기능이 있다. 먼저 `KNeighborsClassifier` 오브젝트를 만들어야한다. 이 오브젝트는 `k`를 매개변수로 받는다.

```py
classifier = KNeighborsClassifier(n_neighbors = 3)
```

그러고 난 후 classifier를 훈련시켜야 한다. `fit()` 메소드는 두개의 매개변수를 받는다. 첫번째는 포인트들의 list, 두번째는 그 포인트들과 관련된 label(레이블)들이다.

```py
training_points = [
    [0.5, 0.2, 0.1],
    [0.9, 0.7, 0.3],
    [0.4, 0.5, 0.7]
]

training_labels = [0, 1, 1]
classifier.fit(training_points, training_labels)
```

마지막으로 학습이 끝난 후 새로운 포인트들을 분류시키면 된다. `predict()`메소드는 분류시키고 싶은 포인트들의 list를 매개변수로 받고 각 포인트들에 대한 예측값의 집합을 list로 반환한다.

```py
unknown_points = [
    [0.2, 0.1, 0.7],
    [0.4, 0.7, 0.6],
    [0.5, 0.8, 0.1]
]

guesses = classifier.predict(unknown_points)
```

## K-Nearest Neighbor Regreesor

K-Nearest Neighbors 알고리즘은 전형적으로 분류하는데 사용되는 강력한 Supervised Machine Learning 알고리즘이다.

이 과정은 최종단계를 제외하면 분류와 거의 동일하다.

먼저 거리공식을 사용하여 새로운 영화와 인접한 항목 `k`개를 찾는다. 중요한것은 좋은 인접항목과 나쁜 인접항목의 개수를 세는 대신 평균 점수를 계산한다는 것이다.

예를들어, 평점이 지정되지 않은 영화와 가장 가까운 3개의 이웃이 각각 `5.0`, `9.2`, `6.8`의 평점을 가진경우 이 영화의 평점은 `7.0`이 될것으로 예상할 수 있다.

## Weighted Regression

영화의 평점을 예측하려고 하는데 가장 가까운 이웃이 아래와 같이 생겼다고 해보자.

| Movie | Rating | Distance to movie X |
| ----- | ------ | ------------------- |
| A     | 5.0    | 3.2                 |
| B     | 6.8    | 11.5                |
| C     | 9.0    | 1.1                 |

평균을 구하면 영화 X의 예상 평점은 6.93이다. 하지만 영화 X는 영화 C와 가장 유사하므로 평균을 계산할 때 C의 평점이 더 중요하다. 이러한 계산을 할 때 가중치를 설정해주면 된다.

$${{5.0 \over 3.2} + {6.8 \over 11.5} + {9.0 \over 1.1} \over {1 \over 3.2} + {1 \over 11.5} + {1 \over 1.1}} = 7.9$$

분자는 모든 평점의 합을 각각의 거리로 나눈 값이다. 분모는 1에서 각각의 거리를 나눈 값이다. 평점이 앞서 계산한 평균값과 달리 7.9로 올라갔다는 사실을 알 수 있다.

## Scikit-learn

마찬가지로 `KNeighborsRegressor`를 이용하여 간단히 구현할 수 있다.

먼저 regressor를 만드는데 매개변수로 `n_neighbors`를 이용해 `k`를 지정해줘야한다.

또 가중평균치를 사용할지 안할지 `weights` 키워드를 이용해서 지정해줄 수 있다. 만약 `weights`가 `"uniform"`인 경우 모든 인접항목들은 평균적으로 동일하게 다뤄진다. 만약 `"distance"`인 경우 평균 가중치가 사용된다.

```py
classifier = KNeighborsRegressor(
    n_neighbors = 3, weights = "distance")
```

그 다음 `fit()`을 이용해 모델을 훈련데이터에 맞춰준다.

```py
training_points = [
    [0.5, 0.2, 0.1],
    [0.9, 0.7, 0.3],
    [0.4, 0.5, 0.7]
]

training_labels = [5.0, 6.8, 9.0]
classifier.fit(training_points, training_labels)
```

그 다음 `predict`를 이용해 예측한다.

```py
unknown_points = [
    [0.2, 0.1, 0.7],
    [0.4, 0.7, 0.6],
    [0.5, 0.8, 0.1]
]

guesses = classifier.predict(unknown_points)
```
