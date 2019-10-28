# Different Plot Types

Class: Analyze Data,Visualize Data
Created: Oct 19, 2019 1:51 PM
Edited: Oct 25, 2019 11:00 AM
Reviewed: No
Sub_Class: Matplotlib

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Different Plot Types

---

## Simple Bar Chart I

- `plt.bar()` 메소드는 다양한 카테고리를 비교할 수 있는 bar chart를 만든다.
    1. x : x 포지션의 위치
    2. y : 각각 바의 높이
    - 대체로 x값에는 0, 1, 2, 3 ... 이런식으로 전달하고 y값엔 같은 값을 전달한다.

x값을 일일이 다 적어줄 수도 있지만 len을 이용해주면 더 편하다.

    heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
    x_values = range(len(heights))
    
    days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
    plt.bar(range(len(days_in_year)), days_in_year)
    plt.show()

![](Untitled-c502609d-919b-4c24-842d-a4dde365de90.png)

---

## Simple Bar Chart II

- 각각 그래프에 라벨 붙여주기

    # axes 오브젝트 만들기
    ax = plt.subplot()
    
    # x축 tick 설정하기
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
    
    # x축 틱의 라벨 설정하기
    ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'])
    
    # 라벨이 너무 길때
    ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'],
    rotation=30)

![](Untitled-0ae267f8-9947-4629-84b0-bbbecf5034d6.png)

---

## Side-By-Side Bars

- 각각의 카테고리끼리 비교하고 싶을 때 Side-By-Side Bar 형태의 그래프

![](Untitled-b0fb3dbd-e192-4435-9ef9-4c4cd8f41e12.png)

- Matplotlib bar의 기본 width값은 `0.8`이다.
- 각각의 파란색 바의 x축 값은 `0`, `2`, `4`, `6` ... 이다.
- 주황색바의 값은 `0.8`, `2.8`, `4.8`, `6.8` ... 이다.

파이썬 코드로 위를 재현하면

    # 파란색 바
    n = 1 # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = 7 # Number of sets of bars
    w = 0.8 # Width of each bar
    x_values1 = [t*element + w*n for element in range(d)]
    # 0.8	2.8	4.8	6.8	8.8	10.8 12.8

    # 주황색 바
    n = 2 # This is our first dataset (out of 2)
    t = 2 # Number of datasets
    d = 7 # Number of sets of bars
    w = 0.8 # Width of each bar
    x_values1 = [t*element + w*n for element in range(d)]
    # 1.6	3.6	5.6	7.6	9.6	11.6 13.6

---

## Stacked Bars

- 여러개의 카테고리를 비교함과 동시에 total value까지 같이 비교하고 싶을 때

![](Untitled-76100329-f31e-464c-9199-3b90bccf13f8.png)

- 먼저 파란색 바를 만든다.

    video_game_hours = [1, 2, 2, 1, 2]
    
    plt.bar(range(len(video_game_hours)), video_game_hours)

- 그 후 주황색 바를 만들고 `bottom`키워드를 이용해준다.

    book_hours = [2, 3, 4, 2, 1]
    
    plt.bar(range(len(book_hours)), book_hours, bottom=video_game_hours)

    from matplotlib import pyplot as plt
    
    drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
    sales1 =  [91, 76, 56, 66, 52, 27]
    sales2 = [65, 82, 36, 68, 38, 40]
    
    plt.bar(range(len(sales1)), sales1)
    plt.bar(range(len(sales2)), sales2, bottom=sales1)
    
    plt.legend(['Location 1', 'Location 2'])
    
    plt.show()

![](Untitled-7db31048-8223-46fb-90ce-1d22f0ceff0b.png)

- 3개 이상의 바가 합쳐질 때

    from matplotlib import pyplot as plt
    import numpy as np
    
    unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
    As = [6, 3, 4, 3, 5]
    Bs = [8, 12, 8, 9, 10]
    Cs = [13, 12, 15, 13, 14]
    Ds = [2, 3, 3, 2, 1]
    Fs = [1, 0, 0, 3, 0]
    
    x = range(5)
    
    # c의 시작점
    c_bottom = np.add(As, Bs)  # As의 높이 + Bs의 높이
    # Numpy add메소드로 리스트끼리의 더하기 가능
    
    # d의 시작점
    d_bottom = np.add(c_bottom, Cs)
    
    # f의 시작점
    f_bottom = np.add(d_bottom, Ds)
    
    plt.figure(figsize=(10, 8))
    plt.bar(x, As)
    plt.bar(x, Bs, bottom=As)
    plt.bar(x, Cs, bottom=c_bottom)
    plt.bar(x, Ds, bottom=d_bottom)
    plt.bar(x, Fs, bottom=f_bottom)
    
    plt.show()

---

## Error Bars

- 오차가 있을수 있다는 것을 표현하기 위한 그래프
- +/- 2를 표현하고 싶을 때 `yerr=2`를 `plt.bar`에 추가해주고, `capsize=10` 키워드를 이용해 보기쉽게 만들어준다.

    values = [10, 13, 11, 15, 20]
    yerr = 2
    plt.bar(range(len(values)), values, yerr=yerr, capsize=10)

- 오차값을 각각 바에 다르게 적용해주고 싶으면 `yerr`을 리스트로 만들어주면 된다.

    values = [10, 13, 11, 15, 20]
    yerr = [1, 3, 0.5, 2, 4]
    plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
    plt.show()

![](Untitled-cb5fd7b8-a061-442c-b42a-19e82ccc2344.png)

    from matplotlib import pyplot as plt
    
    drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
    ounces_of_milk = [6, 9, 4, 0, 9, 0]
    error = [0.6, 0.9, 0.4, 0, 0.9, 0]
    
    # Plot the bar graph here
    plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr=error, capsize=5)
    
    plt.show()

![](Untitled-2ede95e9-fbec-4a34-b924-abd92400dd74.png)

---

## Fill Between

- 에러값을 좀 더 그래프같이 표현하는 방법
- `plt.fill_between`을 이용해 에러를 shade해줄 수 있다.
- `plt.fill_between`은 세개의 인자를 받는다.
    - `x-values` : `plt.plot`의 x값과 같은 방식
    - y값의 lower-bound
    - x값의 upper-bound
- 일반적으로 `fill_between`으로 에러영역을 표시하고 그 위에 선을 추가해준다. `alpha`키워드를 이용해 에러영역의 투명도를 설정해줄 수 있다.

    x_values = range(10)
    y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
    y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
    y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]
    
    # 에러영역
    plt.fill_between(x_values, y_lower, y_upper, alpha=0.2)
    # 선
    plt.plot(x_values, y_values) 
    
    plt.show()

![](Untitled-3d041816-57e8-4184-9708-77cca675baef.png)

- `y_lower`와 `y_upper`값을 직접 계산하는건 너무 오래걸리는 작업이다. 따라서 *list comprehension*을 이용해 연산을 해주면 된다.

    y_lower = [i - 2 for i in y_values]
    y_upper = [i + 2 for i in y_values]

    from matplotlib import pyplot as plt
    
    months = range(12)
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
    
    #your work here
    plt.plot(months, revenue)
    
    ax = plt.subplot()
    ax.set_xticks(months)
    ax.set_xticklabels(month_names)
    
    y_lower = [i - i * 0.1 for i in revenue]
    y_upper = [i + i * 0.1 for i in revenue]
    
    plt.fill_between(months, y_lower, y_upper, alpha=0.2)
    
    plt.show()

![](Untitled-a14332b9-b6aa-422e-a327-bcc9fd20d4d6.png)

---

## Pie Chart

- `plt.pie` 커맨드를 이용해서 파이차트를 만들 수 있다.

    budget_data = [500, 1000, 750, 300, 100]
    
    plt.pie(budget_data)
    plt.show()

![](Untitled-c6805c69-cbc9-47e8-aae7-6ead15a7880b.png)

- 위 파이차트는 뭔가 이상하고 기울어져있다.
Matplotlit를 이용해 파이차트를 만들땐 항상 각각 축을 지정해줘야 한다.
`plt.axis('equal')`

![](Untitled-81b020a9-d840-48d6-adef-0f80753fa834.png)

    from matplotlib import pyplot as plt
    
    payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
    payment_method_freqs = [270, 77, 32, 11]
    
    plt.pie(payment_method_freqs)
    plt.axis('equal')
    
    plt.show()

![](Untitled-ac10b43a-3397-4d06-8c1a-17203faccffc.png)

---

### Pie Chart Labeling

- 파이차트 각각의 조각이 무엇을나타내는지 표시하고 싶을 때

방법 1. `legend`키워드를 이용

    budget_data = [500, 1000, 750, 300, 100]
    budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
    
    plt.pie(budget_data)
    plt.legend(budget_categories)

![](Untitled-46be6d7d-81f6-4964-a46f-9a76acaa5d23.png)

방법 2. 각각의 조각에 라벨붙이기

    budget_data = [500, 1000, 750, 300, 100]
    budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
    
    plt.pie(budget_data, labels=budget_categories)

- 또한, 각각의 조각에 퍼센티지를 붙여서 더 알아보기 쉽게 만들 수 있다.
- `autopct` 키워드를 이용, string formatting 기법을 이용해주면 된다.
    - `'%0.2f'` - 소수점 2개까지 보여주기 `4.08`
    - `'%0.2f%%'` - 소수점 2개, 퍼센티지로 보여주기 `4.08%`
    - `'%d%%'` - 반올림, 퍼센티지 `4%`

    # 소수점 1의자리, 퍼센트
    plt.pie(budget_data, labels=budget_categories, autopct='%0.1f%%')

![](Untitled-80f71ce9-34cf-4c29-ae29-1bb5314f205a.png)

    from matplotlib import pyplot as plt
    
    payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
    payment_method_freqs = [270, 77, 32, 11]
    
    plt.pie(payment_method_freqs, autopct='%0.1f%%')
    plt.axis('equal')
    
    plt.legend(payment_method_names)
    
    plt.show()

![](Untitled-c9ae44f5-91da-4358-ad52-d64ab9637c19.png)

---

## Histogram

- 히스토그램 차트 만들기
- `plt.hist` 커맨드를 이용해 만들 수 있다.
- 각각의 막대를 bin이라고 부르고, 기본값은 10이다. 또, 각각의 막대는 폭이 일정하다.

    plt.hist(dataset) 
    plt.show()

- 10개 이상의 bin을 원하면 `bins` 키워드를 사용해주면 된다.
- `range` 키워드는 x축의 최소값과 최대값을 지정해줄 수 있다.

    plt.hist(dataset, range=(66,69), bins=40)

![](Untitled-82efb1e2-76e8-40ac-9e03-2d505169463a.png)

---

### Multiple Histograms

- 두개의 서로다른 히스토그램 그래프를 비교하고 싶을 때
- 하지만, 두개의 히스토그램을 동시에 plot하면 겹치는 부분이 생긴다.

![](Untitled-d427be28-216f-4128-8e2f-1e680e2478ec.png)

- 이 문제를 해결하기 위해 `alpha` 키워드를 사용해줄 수 있다.

    plt.hist(a, range=(55, 75), bins=20, alpha=0.5)
    plt.hist(b, range=(55, 75), bins=20, alpha=0.5)

![](Untitled-b5ee7ee8-e72a-4eae-b594-c39e9afc758b.png)

- 또, `histtype` 키워드와 `'step'`이라는 인자를 이용해줄 수 있다.

    plt.hist(a, range=(55, 75), bins=20, histtype='step')
    plt.hist(b, range=(55, 75), bins=20, histtype='step')

![](Untitled-2f144e16-7eca-4114-a6d3-a4789554ac57.png)

- `linewidth` 키워드를 이용해 선의 두께를 지정해줄 수 있다.

    plt.hist(a, range=(55, 75), bins=20, histtype='step', linewidth=2)
    plt.hist(b, range=(55, 75), bins=20, histtype='step', linewidth=2)

- 또 다른 문제로 서로 다른 데이터샘플의 수를 가지고 있을 때도 있다.
(아래와 같은 경우)

    a = normal(loc=64, scale=2, size=10000)
    b = normal(loc=70, scale=2, size=100000)
    
    plt.hist(a, range=(55, 75), bins=20)
    plt.hist(b, range=(55, 75), bins=20)
    plt.show()

![](Untitled-d330071b-12da-4803-a21b-073faa1b2152.png)

- 이러한 문제를 해결하기 위해 `normed=True` 키워드를 이용해 노멀라이즈 해줄 수 있다.
- `normed=True` 키워드는 각 bin에 속하는 개수를 전체 개수로 나눈 비율을 각 bar의 높이로 사용하게 된다. (뭔말인지)

![](Untitled-107c46fe-2922-4026-8194-cead1ee82c28.png)

---

## How to Select a Meaningful Visualization

- 두가지를 고려해야 한다.
    1. 시각화를 통해 어떤 답을 주고싶은가?
    2. 어떤 형태의 데이터를 시각화하고 싶은가?

![](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-3/pickachart.svg?sanitize=true)

1. Composition Charts

    전체의 일부는 무엇인가? / 무엇으로 이루어진 데이터인가?

    - 확률, 크기, 퍼센티지와 같은 종류의 데이터를 시각화하기에 적합
    - 다양한 데이터 구성 요소와 그 비율을 전체의 일부로 보여준다.

2. Distribution Charts (분포 차트)
    - 다량의 데이터 / 다양한 특성을 가진 데이터로 적합
    - 시각화를 통해 패턴, 재발, 클러스터 시각화에 적합

        클러스터란, 주어진 데이터들의 특성을 고려해 데이터 집단을 정의하고 데이터 집단의 대표할 수 있는 대표점을 찾는 것으로 데이터 마이닝의 한 방법이다. 클러스터란 비슷한 특성을 가진 데이터들의 집단이다. 반대로 데이터의 특성이 다르면 다른 클러스터에 속해야 한다

3. Relationship Charts

    변수들이 서로 어떤 연관성이 있는가?

    - 전형적인 둘 이상의 변수 사이의 상관관계를 나타내는데에 적합
    - 한 그래프에서 여러개의 변수를 매핑시켜 상관관계를 알 수 있다.
    - 상관 관계는 변수들이 얼마나 연관되어 있는지 측정한다.
4. Comparison Charts

    변수가 서로 어떻게 비교되는가?

    - 다수의 변수가 있어야하고 이 차트를 보고 다른 항목과 함께 비교할 수 있다.
    - 예) 각자 다른 변수에 속하는 여러개의 선이 그려져있는 선그래프, 다색 막대그래프

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)