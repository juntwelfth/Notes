# Seaborn Introduction

## Introduction to Seaborn

- Seaborn은 통계분석을 위한 막대그래프를 만드는데 사용된다.
- Seaborn은 통계적 탐구와 통찰을 위한 고급진 시각화를 할 수 있게 해준다.
- Matplotlib에 기반한 라이브러리이지만 좀 더 업그레이드 되었다.
    1. 시각적으로 더 매력적인 plot 스타일과 간결한 문법
    2. Pandas의 DataFrame을 읽어들일 수 있어서 CSV파일을 직접 plot하기 쉽다.
    3. 여러개의 행이 있는 DataFrame을 쉽게 요약해 집계된 차트로 보여줄 수 있다.

> import 방법

```py
import seaborn as sns
```

## Plotting Bars with Seaborn

- matplotlib 막대그래프와 같이 seaborn도 막대그래프 plot이 가능하다.
- `sns.barplot()` 3개의 인자
    1. `data` : DataFrame
    2. `x` : x축에 올 DataFrame의 column
    3. `y` : y축에 올 DataFrame의 column

```py
import pandas as pd
import seaborn as sns

df = pd.read_csv('results.csv')

sns.barplot(data=df, x='Gender', y='Mean Satisfaction')
plt.show()
```

- matplotlib로 구현하면 아래와 같다... 그래도 색깔은 구현 못했음

```py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

ax = plt.subplot()
plt.bar(range(len(df)), df['Mean Satisfaction'])
ax.set_xticks(range(len(df)))
ax.set_xticklabels(['Male', 'Female', 'Non-binary'])
plt.xlabel('Gender')
plt.ylabel('Mean Satisfaction')
plt.show()
```

## Understanding Aggregates

- Aggregate란, 데이터집합을 숫자로 표현한 것이다. (평균값 등)

```py
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# csv 파일을 불러오고
gradebook = pd.read_csv("gradebook.csv")

# Assignment 1만 따로 불러온 다음
assignment1 = gradebook[
    gradebook.assignment_name == 'Assignment 1']

# 중간값을 계산
asn1_median = np.median(assignment1.grade)
```

- seaborn으로 구현하면 아래와 같다. 평균을 알아서 구해서 막대그래프를 그려준다.

```py
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook,
    x="assignment_name", y="grade")
plt.show()
```

## Modifying Error Bars

- `barplot()`을 하면 기본 설정으로 Seaborn은 error bar를 보여준다. 오차범위
  - 아래 그림에서 오차막대는 평균 학생들이 어떤 점수를 받을지 보여준다.

![error bars](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/intro-to-seaborn/seabornCi1.png)

- seaborn의 default 설정은 bootstrapped confidence interval이다.
- 간단히말해서 이 범위는 데이터에 기반, 비슷한 상황의 95%가 이 범위에 속할것이다 라는 뜻.
- 위 예시에서 the confidence interval (신뢰구간)은 "매우 많은 학생들에게 이 과제를 주었을 때 과제의 평균 점수가 이 범위내에 있을것이다."

- `ci="sd"` 키워드를 통해 오차막대를 표준편차 막대로 바꿀 수 있다.

```py
sns.barplot(data=gradebook,
    x="name", y="grade", ci="sd")
```

## Calculating Different Aggregates

- seaborn의 `barplot()`이 평균값이 아닌 다른값을 표현하게 해주고 싶다면 `estimator` 키워드를 이용하면 된다.
- `estimator` 키워드는 아무거나 다 받을 수 있다. (`np.mean`, `len` 등등)

```py
sns.barplot(data=df, x="x-values",
            y="y-values", estimator=np.median)

sns.barplot(data=df, x="Patient ID",
            y="Response", estimator=len)
```

## Aggregating by Multiple Columns

- 막대그래프에서 카테고리를 더 나눠서 표현하고 싶을 때
- `hue` 키워드를 사용하면 된다.

```py
sns.barplot(data=df, x="Gender",
            y="Response", hue="Age Range")
```

![multiple bar plots](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/intro-to-seaborn/seabornHue.svg)

> X축 라벨은 그대로 유지하고, 두개의 막대를 세분화 시켰다.

## Review

1. CSV 파일 불러오기

    ```py
    df = pd.read_csv('file_name.csv')
    ```

2. `sns.barplot()`과 `x`, `y`, `data`를 설정해준다.

    ```py
    sns.barplot(data=df, x='X-Values', y='Y-Values')
    ```

3. `estimator`와 `hue`를 설정해준다.

    ```py
    sns.barplot(data=df, x='X-Values', y='Y-Values',
                estimator=len, hue='Value')
    ```

4. `plt.show()`

## Built-in Themes

- `sns.set_style()`

    ```py
    sns.set_style()
    sns.stripplot(x="day", y="total_bill", data=tips)
    ```

1. `darkgrid` - default
![darkgrid](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image1.png)

2. `dark`
![dark](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image2.png)

3. `ticks`
    - 흰색 바탕 덕에 plot들을 더 잘 볼 수 있다.
![ticks](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image3.png)

4. `white`
    - 마찬가지로 흰색바탕
![white](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image5.png)

5. `whitegrid`
    - 그리드 덕에 수치를 더 잘 확인할 수 있다.
![white grid](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image4.png)

> Fun Fact : 다크블루 위 하얀색 글씨가 검은색 바탕 위 흰색 글씨보다 더 읽기 쉽다.

## Despine

- 원래 네 면에 모두 테두리가 그려지는데 `sns.despine()` 메소드로 간결화 시킬 수 있다.

    ```py
    sns.set_style("white")
    sns.stripplot(x="day", y="total_bill", data=tips)
    sns.despine()
    ```

![a](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image6.png)

- 네 면 전부다 없앨 수도 있다.

    ```py
    sns.set_style("whitegrid")
    sns.stripplot(x="day", y="total_bill", data=tips)
    sns.despine(left=True, bottom=True)
    ```

![a](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image7.png)

## Scaling Figure Styles for Different Mediums

- Matplotlib를 사용하면 시각적으로 보기 불편한 부분이 있을 수 있다.
- Seaborn은 연구논문, 컨퍼런스 포스터 등 적절한 상황에 맞게 디자인할 수 있다.

`sns.set_context()`

1. plot의 스케일 조절가능
    - `paper`

        ```py
        sns.set_style("ticks")

        # Smallest context:
        sns.set_context("paper")
        sns.stripplot(x="day", y="total_bill",
                    data=tips)
        ```

    ![notebook](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image8.png)

    - `notebook` - default
    - `talk`
    - `poster`

        ```py
        sns.set_style("ticks")

        # Largest Context:
        sns.set_context("poster")
        sns.stripplot(x="day", y="total_bill",
                      data=tips)
        ```

        ![poster](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image9.png)

2. font size 조절가능
    - `font_scale`
    - line width도 함께 조절해서 잘 어울리게 만들어 줄 수 있다.

        ```py
        # Set font scale and reduce grid line
        # width to match
        sns.set_context("poster",
            font_scale = .5,
            rc={"grid.linewidth": 0.6})

        sns.stripplot(x="day",
            y="total_bill", data=tips)
        ```

        ![font scale](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image10.png)

        ```py
        # Set font scale and increase grid line
        # width to match
        sns.set_context("poster",
            font_scale = 1,
            rc={"grid.linewidth": 5})

        sns.stripplot(x="day",
            y="total_bill", data=tips)
        ```

        ![.](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-1/article1_image11.png)

3. `rc`
    - `sns.set_context`를 했을 때 생성되는 dictionary에서 직접 수정할 수 있다.
    - 제공되는 속성값들

        ```py
        sns.set_style("ticks")
        sns.set_context("poster")
        sns.stripplot(x="day", y="total_bill",
                      data=tips)
        sns.plotting_context()

        {'axes.labelsize': 17.6,
            'axes.titlesize': 19.200000000000003,
            'font.size': 19.200000000000003,
            'grid.linewidth': 1.6,
            'legend.fontsize': 16.0,
            'lines.linewidth': 2.8000000000000003,
            'lines.markeredgewidth': 0.0,
            'lines.markersize': 11.200000000000001,
            'patch.linewidth': 0.48,
            'xtick.labelsize': 16.0,
            'xtick.major.pad': 11.200000000000001,
            'xtick.major.width': 1.6,
            'xtick.minor.width': 0.8,
            'ytick.labelsize': 16.0,
            'ytick.major.pad': 11.200000000000001,
            'ytick.major.width': 1.6,
            'ytick.minor.width': 0.8}

        sns.set_context("poster",
            font_scale = 1, rc={"grid.linewidth": 5})
        ```

## Palettes

- `sns.color_palette()` 메소드를 이용해 색을 설정해줄 수 있다.
    > RGB, Hex Color Codes, HTML Color Names 사용 가능

- palette가 어떻게 생겼는지 궁금하면 `sns.palplot()`를 이용해 확인할 수 있다.

```py
# Save a palette to a variable:
palette = sns.color_palette("bright")

# Use palplot and pass in the variable:
sns.palplot(palette)
```

![bright](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image1.png)

- Seaborn에서 palette를 선택하려면 `sns.set_palette()` 이름을 인자로 전달해주면 된다.

```py
# Set the palette using the name of a palette:
sns.set_palette("Paired")

# Plot a chart:
sns.stripplot(x="day", y="total_bill", data=tips)
```

![paired](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image2.png)

- palette설정을 하지 않으면 기본값을 사용한다. (사람들이 Seaborn을 사용하는 이유이기도 함)
  - Matplotlib Defaults
![mat](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image3.png)

  - Seaborn Defaults
![sea](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image4.png)

- 심지어 Seaborn은 Matplotlib에만 존재하는 plot의 형태도 커스터마이즈할 수 있게 해준다. (히스토그램 등등)

```py
    # Call the sns.set() function
    sns.set()
    for col in 'xy':
      plt.hist(data[col], normed=True, alpha=0.5)
```

![hist](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image5.png)

- Seaborn Default Color Palette
  - `deep`, `muted`, `pastel`, `bright`, `dark`, `colorblind`

![seaborn](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image6.png)

```py
# Set the palette to the "pastel" default palette:
sns.set_palette("pastel")

# plot using the "pastel" palette
sns.stripplot(x="day", y="total_bill", data=tips)
```

![pastel](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image7.png)

## Color Brewer Palettes

- 기본 내장 팔레트 말고 Color Brewer Palette라는 Cindy Brewer가 만든 pallete를 이용할 수 있다. colorblind도 볼 수 있는 좋은 pallete 지원해준다.

```py
custom_palette = sns.color_palette("Paired", 9)
sns.palplot(custom_palette)
```

![colors](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image8.png)

![colors2](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image9.png)

## **Qualitative Palettes for Categorical Datasets**

- 확실히 구별은 되지만 순서가 없는 카테고리같은 경우 이 팔레트를 사용하면 좋다.
- Qualitative Palettes는 뚜렷한 색깔로 구별하기 쉽게 해준다. 특정 순서나 의미를 집어넣진 말아야한다.
- 예를들면 보더콜리와 푸들은 명확히 구분되지만 서로간의 고유한 순서가 없다.

```py
qualitative_colors = sns.color_palette("Set3", 10)
sns.palplot(qualitative_colors)
```

![set3](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image10.png)

## **Sequential Palettes**

- 이름과 같이 그라데이션처럼 서로 연관되는 색깔의 집합이다.
- 예를들면 학점, 연봉등과 같이 그룹핑될 수 있는 집합
- 가장 어두운 색상이 가장 많은 관심을 끌기 때문에 단지 더 높은 값을 강조하고 싶다면 이 색상팔레트를 사용하는 것이 좋다.

```py
sequential_colors = sns.color_palette("RdPu", 10)
sns.palplot(sequential_colors)
```

![rdpu](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image11.png)

## **Diverging Palettes**

- 이 팔레트는 고온 및 저온과 같이 낮은값과 높은 값이 모두 동일한 우선순위에 있는 데이터셋에 가장 적합하다.

```py
    diverging_colors = sns.color_palette("RdBu", 10)
    sns.palplot(diverging_colors)
```

![rdbu](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image12.png)

![rdbu](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/seaborn-design-2/article2_image13.png)
