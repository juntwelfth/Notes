# Statistical Distributions with NumPy

Class: Analyze Data
Created: Sep 30, 2019 11:48 PM
Edited: Oct 13, 2019 12:48 PM
Reviewed: No
Sub_Class: NumPy

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Histograms

---

## Histograms, Part I

- 우리가 데이터셋을 처음 볼 때, 생각해야 하는 것
- 특정 값이 다른 값들보다 더 자주 등장하는지?
- 데이터셋의 범위가 어디인지? (i.e., the min and the max values?)
- 이상치가 존재하는지?
- 위 사항들을 *histogram*이라고 불리는 차트를 이용해 쉽게 볼 수 있다.

    d = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]

이러한 데이터셋이 주어졌을 때, 간단한 histogram은 우리에게 각 숫자들이 얼마나 많이 있는지 보여준다.

![](Untitled-92f188b9-63f1-4418-b869-32889497384f.png)

---

## Histograms, Part II

- 대량의 데이터셋이 주어졌을 때 우린 데이터 값의 범위를 넓게 지정한다. 0-5, 6-10, 11-15 이런식으로
- 이러한 그룹핑은 *bins*라고 불린다.
- histogram에 있는 모든 bins들은 폭이 일정하다.

![](Untitled-bc3343d7-0cc6-4c98-9d13-f07699150dbb.png)

the width of each bin would be 5

---

## Histograms, Part III

    # This imports the plotting package.  We only need to do this once.
    from matplotlib import pyplot as plt 
    
    # This plots a histogram
    plt.hist(data)
    
    # This displays the histogram
    plt.show()

- `plt.hist`에 인자를 주지않으면 matplotlib은 자동으로 10 bins짜리 그래프를 만든다.
- `plt.show()` 함수를 사용해서 꼭 그래프를 화면에 띄우자

bins의 크기를 바꾸고 싶다면 `bins` 키워드를 사용해서 바꿔줄 수 있다.

    plt.hist(data, bins=5)

range의 크기를 바꾸고 싶다면 `range` 키워드를 사용해서 바꿔줄 수 있다.

range에는 두개의 숫자로 범위를 전달해야 하는데 뒤에 오는 숫자는 포함되지 않는다.

tuple 형태로 전달해야 한다. (range는 확대의 개념임)

    plt.hist(data, range=(20, 51))

    from matplotlib import pyplot as plt
    
    d = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])
    
    plt.hist(d, bins=5, range=(1, 6))
    
    plt.show()

![](Untitled-729c7835-d3e5-4de3-90f8-d3525be74e79.png)

5 bins, 5 range

---

# Different Types of Distributions

- The *probability of success* was 30% (he makes 30% of free throws)
- The number of *trials* was 10 (he took 10 shots)
- The number of *successes* was 4 (he made 4 shots)

---

## Different Types of Distributions, Part I

- Histogram과 데이터셋들은 그래프의 모양에 따라 다양하게 정의될 수 있다.
    - 그 중 한가지 방법은 peaks의 갯수를 세어 나누는 방법이 있다.
        - Unimodal

            ![](Untitled-ed2bc089-84ef-422b-bf25-f2b912e5c8c8.png)

            한개의 distinct peak밖에 없다.

        - Bimodal

            ![](Untitled-6c0833b5-0126-47f0-806d-44a2a9469642.png)

        - Multimodal

            ![](Untitled-8ab51e69-c81f-49cd-81e8-ed8d429220b7.png)

            세개 이상의 peak을 가질 때 multimodal dataset이라고 부른다.

        - Uniform

            ![](Untitled-f3826ecd-a3a6-4948-9237-ba25b15b0bf7.png)

            딱히 그렇다 할 peak이 없다.

![](Untitled-ec1ab89d-9f26-4e71-a1fb-db1270d0abea.png)

순서대로 multimodal, unimodal, bimodal

---

## Different Types of Distribution, Part II

- unimodal의 다양한 형태
    - unimodal의 좌우가 (대충)대칭일 때 Symmetric이라고 부른다.

        ![](Untitled-4dc323ad-b47a-4062-a225-5b812b7f9c46.png)

- peak의 오른쪽으로 꼬리가 길게 나타나고 데이터가 대부분 왼쪽에 몰려있는 형태를 skew-right 데이터셋이라고 부른다.

    ![](Untitled-72114fb1-980b-4f81-be45-691933c69f13.png)

- 반대의 경우 skew-left라고 부른다.

    ![](Untitled-190813e7-3b5d-4abf-9b85-c4f3e49a55a9.png)

- 이러한 형태들은 mean(평균값)과 median(중간값)에 영향을 끼친다. skewed 형태의 그래프에선 mean은 딱히 쓸모가없어진다.

    ![](Untitled-e1cd642e-28d0-4748-99cd-ae6262373ab6.png)

    ![](Untitled-6ee58c11-b573-49c0-b958-e9f4b45234e8.png)

    ![](Untitled-784d55f2-a61f-464b-99c0-1d35b10f36c6.png)

---

# Normal Distribution

---

## Normal Distribution, Part I

- 가장 흔한 통계분포는 normal distribution이다.
- normal distribution은 symmetric이고 unimodal이다.
- 정규분포를 따르는 다양한 예시
    - The heights of a large group of people
    - 건강한 사람들의 혈압치
    - 측정 오류치

![](Untitled-5d0a696e-9491-4434-896c-3d38bc613648.png)

[https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/mean-std-norm-dist.html](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/mean-std-norm-dist.html)

---

## Normal Distribution, Part II

- NumPy 라이브러리로 랜덤 숫자를 생성하는 방법
- `numpy.random.normal()`
    - loc : mean(중간값)
    - scale : standard deviation(표준편차) aka std
    - size : 랜덤 숫자의 갯수(?) 크기

    a = np.random.normal(0, 1, size=100000)

![](Untitled-886c41d8-ed94-4859-a8f7-d9e9a3248e58.png)

이렇게 생겼다.

    import codecademylib
    import numpy as np
    from matplotlib import pyplot as plt
    
    # Brachiosaurus
    b_data = np.random.normal(6.7, 0.7, size=1000)
    
    # Fictionosaurus
    f_data = np.random.normal(7.7, 0.3, size=1000)
    
    plt.hist(b_data,
             bins=30, range=(5, 8.5), histtype='step',
             label='Brachiosaurus')
    plt.hist(f_data,
             bins=30, range=(5, 8.5), histtype='step',
             label='Fictionosaurus')
    plt.xlabel('Femur Length (ft)')
    plt.legend(loc=2)
    plt.show()

![](Untitled-82ccfbd2-f695-4c69-aae6-5a9e5dc4d081.png)

---

# Standard Deviations and Normal Distribution

---

## Standard Deviations and Normal Distribution, Part I

- Normal distribution에서, mean(평균값)과 standard deviation(표준편차)이 그래프의 모양을 결정짓는다.

[https://s3.amazonaws.com/codecademy-content/courses/numpy/norm_dist.html](https://s3.amazonaws.com/codecademy-content/courses/numpy/norm_dist.html)

---

## Standard Deviations and Normal Distribution, Part II

- 평균이 50이고 표준 편차가 10 인 정규 분포가 있다고 가정했을 때

    lower_bound = mean - std
                = 50 - 10
                = 40
    
    upper_bound = mean + std
                = 50 + 10
                = 60

데이터셋의 68%가 40 ~ 60 사이에 있다고 예상할 수 있다.

평균값과 표준편차값에 상관없이 데이터의 68%가 +/- 1 평균의 표준편차 내에 존재한다.(???????????)

68% of our samples will fall between +/- 1 standard deviation of the mean

95% of our samples will fall between +/- 2 standard deviations of the mean

99.7% of our samples will fall between +/- 3 standard deviations of the mean

    import numpy as np
    
    one_above = 1100  # 평균 + 표준편차
    
    one_below = 900   # 평균 - 표준편차
    
    print(one_above, one_below)
    
    one_std = 2000 * 0.68  # 데이터의 68%가 900 ~ 1100 사이에 존재한다.
    
    print(one_std)

---

# Binomial Distribution

---

## Binomial Distribution, Part I

- The *probability of success* was 30% (he makes 30% of free throws)
- The number of *trials* was 10 (he took 10 shots)
- The number of *successes* was 4 (he made 4 shots)
- binomial distribution은 중요하다. 왜냐면 특정값이 어떻게 존재하는지 알 수 있기 때문 (우리가 예상했던 값이 아니더라도)

- 아래 그래프를 통해 농구선수가 4번의 골을 넣었더라도 이상한 일이 아니라는걸 알 수 있다.
(10번 다 넣으면 이상한거겠지)

    ![](Untitled-09959639-8da2-4a61-8ab9-38ac0e546a4d.png)

---

## Binomial Distributions, Part II

- `numpy.random.binomial` 함수를 통해 binomial 랜덤 숫자를 만들 수 있다.
    - N : 샘플 혹은 시도횟수
    - P : 성공 확률, 가능성
    - size : 사이즈

10000번의 시도, 10번의 시도, 30%의 확률

    # Let's generate 10,000 "experiments"
    # N = 10 shots
    # P = 0.30 (30% he'll get a free throw)
    
    a = np.random.binomial(10, 0.30, size=10000)

Matplotlib를 이용해 그래프를 만들어 보자.

    plt.hist(a, range=(0, 10), bins=10, normed=True)
    plt.xlabel('Number of "Free Throws"')
    plt.ylabel('Frequency')
    plt.show()

![](Untitled-706e6285-008f-48a5-b52c-a49e694c6dd9.png)

500개의 이메일을 보내는데 그 중 5%만이 이메일을 연다.

10000번의 시도를 했을 때의 그래프를 나타내는 방법

    import codecademylib
    import numpy as np
    from matplotlib import pyplot as plt
    
    emails = np.random.binomial(500, 0.05, size=10000)
    
    plt.hist(emails)  # 필수
    plt.show()        # 필수

![](Untitled-66b101dc-5b0e-4142-9ad3-060000cdfafa.png)

---

## Binomial Distributions and Probability

> Our basketball player has a 30% chance of making any individual basket. He took 10 shots and made 4 of them, even though we only expected him to make 3. What percent chance did he have of making those 4 shots?

4번의 성공을 할 확률을 구해보자.

    a = np.random.binomial(10, 0.30, size=10000)
    np.mean(a == 4)
    >> 0.1973  # 19.73% -> 20%의 확률

랜덤 숫자이기 때문에 결과는 매번 조금씩 달라진다.

10000번의 시도, 0.3의 확률이면 소수점 이하 두번째 자리까지 정확하다.

    import numpy as np
    
    emails = np.random.binomial(500, 0.05, size=10000)
    
    # 아무도 메일을 열어보지 않을 확률
    no_emails = np.mean(emails == 0)
    
    # 500명중 8% 이상이 열어볼 경우
    b_test_emails = np.mean(emails > 40)  # 500의 8% = 40
    
    print(no_emails, b_test_emails)

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)