# Hypothesis Testing

## 1 Sample T-Testing

- 가설 테스트를 할 때 먼저 그럴리가 없다라고 생각한 뒤 테스트를 해야한다.
- 테스트 한 귀무 가설은 다음과 같이 표현할 수 있다.
  >*"표본세트는 목표 평균을 가진 모집단에 속한다."*

- 1 Sample T-Test의 결과는 p-value다. 우린 p-value값을 가지고 가설을 받아들일지 말지 결정할 수 있다.
- 예를 들어 p-value가 0.05보다 작으면 귀무가설을 기각하고 유효한 차이가 있음을 말할 수 있다.
- SciPy엔 `ttest_1samp`라는 메소드가 존재하고, 1 Sample T-Test를 실행한다.
- `ttest_1samp`는 두개의 인풋이 필요하다.
  1. 값의 분포
  2. 추정 평균값

- 또한 두개의 아웃풋을 내보낸다.
  1. T-Statics
  2. P-Value - 특정 평균과 분포에서 나온 표본의값이 얼마나 믿을만한지

```py
from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")
print(ages)
>>> [32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22]

ages_mean = np.mean(ages)
print(ages_mean)
>>> 31.0

x, pval = ttest_1samp(ages, 30)
```

```py
from scipy.stats import ttest_1samp
import numpy as np

correct_results = 0 # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000): # 1000 experiments
    # a : 쓸모없음(아직은)
    a, pval = ttest_1samp(daily_visitors[i], 30)

    # pval이 0.05보다 작으면 가설 기각.
    if pval < 0.05:
    correct_results += 1


print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
```

## 2 Sample T-Test

- 지난 주 웹사이트 방문자들이 지내는 평균 시간이 25분이었는데 이번주엔 28분으로 늘어났다. 평균이 바뀐걸까 아니면 자연스러운 현상일까?
- 이러한 차이를 테스트하는것이 바로 2 Sample T-Test이다.
- 2 Sample T-Test는 두개의 평범하게 널리 분포되어있는 데이터집단을 비교한다.

- 이 경우 Null hypothesis는 두 분포의 평균이 같다는 것이다.

- SciPy의 `ttest_ind` 함수를 이용해 2 Sample T-Test를 실행할 수 있다.
  - 2개의 분포를 인자로 받고
  - T-Statistic과 P-Value를 반환한다.

```py
from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")

week1_mean = np.mean(week1)
week2_mean = np.mean(week2)

week1_std = np.std(week1)
week2_std = np.std(week2)

a, pval = ttest_ind(week1, week2)
print(pval)
>>> 0.000676767690007
```

>`ttest_ind`의 ind는 *Independent*의 약자

## Dangers of Multiple T-Tests

- 세개의 모집단이 있고 T-Test를 하려고 할 때, 총 세번의 T-Test를 하게 된다.
- P-Value는 각각의 T-Test에서 가설을 잘못 기각할 확률이다. T-Test를 많이 하면 할수록 1종 오류인 오탐 (False Positive)이 발생할 가능성이 더 높아진다.
- P-Value가 0.05이면, 귀무가설이 맞다고 가정할 때 유효한 결과를 얻을 확률이 `1 - 0.05 = 0.95` 95%라는 말이다.
- 다시말하면 P-Value는 귀무가설이 맞다는 전제하에, 표본에서 실제로 관측된 통계치와 *'같거나 더 극단적인'* 통계치가 관측될 확률이다.
- 두번째 T-Test를 했을 때 0.95 * 0.95, 0.9025이므로 유효한 결과가 아닐 확률이 거의 10%라는 뜻이다.

```py
from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
print(a_mean, b_mean, c_mean)

a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)
print(a_std, b_std, c_std)

x, a_b_pval = ttest_ind(a, b)
print(a_b_pval)

x, a_c_pval = ttest_ind(a, c)
print(a_c_pval)

x, b_c_pval = ttest_ind(b, c)
print(b_c_pval)

error_prob = 1-0.95**3
print(error_prob)
```

>세번의 T-Test를 하면 14.26%정도의 가설이 틀릴 확률이 생긴다.

## ANOVA (Analysis of Variance)

- 숫자로 이루어진 데이터집합을 두개 이상 비교할 때 1종오류 확률을 `0.05`로 방어하는 가장 좋은 방법은 ANOVA를 사용하는 것이다.
- ANOVA는 모든 데이터집합의 평균이 같다는 귀무가설을 테스트한다.
- ANOVA를 통해 귀무가설을 기각하면 적어도 하나의 데이터집합의 평균이 다르다는 것을 얘기한다. (어떤 데이터집합인지 알려주진 않는다.)

- SciPy 기능 `f_oneway`를 통해 여러개의 데이터집합을 ANOVA(분석)할 수 있다.
  - 서로 다른 데이터집합을 인풋으로 받고
  - T-Statistic과 P-Value를 반환한다.

수학자, 예술가, 심리학자 셋이서 게임의 점수를 비교하는 경우

```py
x, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)
```

- 이 경우 귀무가설은 세명의 평균점수가 같다는것이다.
- 만약 귀무가설이 기각되면 (p-value가 `0.05`보다 작다면) 한 쌍의 데이터집합이 크게 다르다는 것을 알 수 있다.
- ANOVA를 사용하면 어떤 쌍의 데이터집합이 크게 다른지 알 순 없다.

## Assumptions of Numerical Hypothesis Tests

1. ### 수치 가설 테스트를 하기 전 다음 사항들이 충족되는지 확인해야 한다

   - 표본들은 각각 따로 정규분포 되어야한다.
   - 실제 데이터분석가들은 종종 제대로 정규분포되지 않은 데이터집합에 대해 가설을 행한다.
   - 더 중요한 것은 정규분포가 특히 가능성이 낮다고 믿을만한 몇가지 이유가 있는지 인지하는 것이다.
   - 데이터집합이 정상이 아니면 수치 가설 검정이 의도한대로 이루어지지 않는다.
   - 예를들어, 세개의 도시에서 교통량을 측정한다고 해보자. 각각의 도시의 데이터는 독립적이고 서로 영향을 주지 않아야하는데 각각의 데이터집합은 정규분포되어있다.
   >특정 아침시간과 특정 저녁시간에 교통량이 몰리는 형태
   ![Traffic Data Graph](https://s3.amazonaws.com/codecademy-content/courses/learn-hypothesis-testing/lesson_ii/histogram_data_traffic.svg)
   이 경우 numerical hypothesis test는 적절하지 않다.

2. ### 각각 그룹의 모집단 표준편차가 같아야한다

   - ANOVA와 2 Sample T-Test는 서로 표준편차가 크게다른 데이터집합을 사용하면 그룹 평균의 차이가 애매해질 수 있다.
   - 표준편차 간의 유사성을 확인하려면 두 표준편차를 나눈 비율이 1에 "충분히 가까운지" 확인하면 된다.
   - "충분히 가까운지"는 상황에 따라 다르겠지만 보통 10%이내면 충분하다.

3. ### Sample(표본)은 독립적이어야 한다

   - 둘 이상의 데이터셋을 비교할 때 서로의 값에 영향을 끼치면 안된다.
   - 즉, A셋의 정보에서 B셋의 정보를 얻을 수 있으면 안된다.
   - 표본이 독립적이지 않은 예시
     - 축구선수가 지옥훈련을 받기 전, 받는 중, 받고 난 후 세가지 경우에 대해 득점한 골의 수
     - 약물 투여 전, 투여 중, 투여 후 환자의 혈압상태
   > 올바른 테스트를 선택했는지 알 수 있도록 가설 테스트를 수행하기 전 데이터셋을 먼저 이해하는 것이 중요하다.

## Tukey's Range Test

- Tukey's Range Test는 데이터집합들 간의 차이를 확인할 수 있다.
- 예를들어, 상점 A, B, C 각각의 판매량을 전달해 주면 Tukey 테스트는 어떤 조합이 구별될 수 있는지 알려준다.
- `pariwise_tukeyhsd` 메소드를 이용하면 된다.
  > scipy가 아닌 statsmodel에서 불러와야한다.
  1. 모든 데이터가 담긴 리스트
  2. 각각의 데이터에 대한 라벨
  3. p-value 혹은 유의수준 (일반적으로 `0.05`)
- 드라마, 코미디, 다큐멘터리 영화의 평균 점수를 비교하는 예

```py
movie_scores = np.concatenate([drama_scores, comedy_scores, documentary_scores])

labels = ['drama'] * len(drama_scores) + \
         ['comedy'] * len(comedy_scores) + \
         ['documentary'] * len(documentary_scores)

tukey_results = pairwise_tukeyhsd(movie_scores, labels, 0.05)
```

## Binomial Test

- 1-Sample T-Test, 2-Sample T-Test, ANOVA, Tukey's Range Test는 평균값을 찾아서 비교하지 않으면 작동하지 않는다.
- 반면에 Binomial Test는 특정 카테고리가 기대치에 미치는지 테스트할 수 있다.
- 예시로는
  1. 분기별 목표 이메일 열람 수치와 실제 이메일 열람 수치
  2. 기대 설문 응답자 수와 실제 설문 응답자 수
  3. 동전의 앞면이 나올거라고 예상한 수치와 실제 앞면이 나온 경우
- 이 경우 귀무가설은 관찰된 행동과 예상되는 행동 사이 차이가 없다는 것이다.
- p-value가 0.05 미만인 경우 해당 가설을 기각하고 관측치와 기대치간 차이가 있음을 결론지을 수 있다.
- SciPy는 `binom_test`라는 메소드를 제공한다.
  1. 성공한 횟수
  2. 총 도전 횟수
  3. 기대 성공확률
- 동전을 1000번 flip했을 때 앞면이 나올확률이 50%라고 가정하고, 실제 앞면이 525번 나왔을 때 동전에 이상이 있는가?

```py
pval = binom_test(525, n=1000, p=0.5)
```

> p-value를 반환하여 지정된 확률로 샘플이 발생할 가능성이 얼마나 확실한지 알려준다. p-value가 0.05보다 작으면 귀무가설을 기각하고 동전에 이상이 있음을 증명할 수 있고, 앞면이 나올 확률이 통계적으로 50%가 아니라고 말할 수 있다.

## Chi Square Test

- ~~치가 아니고 카이스퀘어~~
- 데이터셋이 세개 이상 주어지면 더이상 Binomal Test를 사용할 수 없다. 대신 카이 제곱 검정을 사용해야한다.
- Chi Square Test 예시
  - 그룹 절반에게 초록색 버튼을 주고 나머지 절반에게 자주색 버튼을 줬을 때 어느 한 그룹이 버튼을 누를 확률이 더 높은지 A/B 테스트 할 때
  - 남녀에게 "세가지 제품중 가장 좋아하는 제품을 골라주세요" 라는 설문을 했을 때 남녀의 선호도가 크게 다른지
- `chi.contingency`
  - 테이블을 인풋으로 전달해줘야 한다. (크기는 상관없음)
  - Column : 각각 다른 상황, 예) 남녀간의 차이, 인터페이스 A와 B의 차이
  - Row : 다른 결과, 예) 설문조사 A vs B, Clicked a Link vs Didn't Click
- 귀무가설은 데이터 집합간에 큰 차이가 없다는 것이다.

```py
from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

X = [[30, 10],
     [35, 5],
     [28, 12]]

chi2, pval, dof, expected = chi2_contingency(X)

print(pval)
>>> 0.155082308077

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
# 4th gr | 20       |  20

X2 = [[30, 10],
     [35, 5],
     [28, 12],
    [20, 20]]
chi2, pval, dof, expected = chi2_contingency(X2)
print(pval)
>>> 0.155082308077  # 귀무가설 기각
```
