
# KDE Plots

## KDE Plots, Part I

- KDE stand for *Kernel Density Estimator*
- KDE는 변화량을 곡선그래프로 보여준다.
- 다른 2차원 혹은 이변량 데이터셋과는 다르게 1차원, 일변량그래프만 가능하다.
- KDE는 히스토그램보다 더 선호되는데, 히스토그램은 데이터를 bin으로 그룹하는 방식과 bin의 너비에 따라 데이터의 모양을 매우 다양한 결과가 나오기 때문이다.
- KDE 플롯은 이러한 문제들을 완화시킬 수 있다. 스무스한 데이터셋이 데이터의 형태를 일반화시키고 특정 데이터 포인트에 영향을받지 않기 때문이다.

## KDE Plots, Part II

- `sns.kdeplot()` 메소드를 이용해 plot할 수 있다.
  - `data` : 시각화 될 수 있는 univariate 데이터셋 (파이썬 리스트, numpy array, dataframe)
  - `shade` : shade화 시킬것인지 아닌지 boolean

    sns.kdeplot(dataset1, shade=True)
    sns.kdeplot(dataset2, shade=True)
    sns.kdeplot(dataset3, shade=True)
    plt.legend()
    plt.show()

![](Untitled-126bc04d-2332-4de0-8487-5149aaf2ef4e.png)

KDE plot 할 때에는 데이터가 합쳐진 dataframe과 다르게 각각 서로 다른 데이터셋을 이용해야 한다.

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    import seaborn as sns

    # CSV파일을 numpy array로
    set_one = np.genfromtxt("dataset1.csv", delimiter=",")
    set_two = np.genfromtxt("dataset2.csv", delimiter=",")
    set_three = np.genfromtxt("dataset3.csv", delimiter=",")
    set_four = np.genfromtxt("dataset4.csv", delimiter=",")

    # KDE plot으로 사용할 수 없다.
    n=500
    df = pd.DataFrame({
        "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
        "value": np.concatenate([set_one, set_two, set_three, set_four])
    })

    # 더 이쁘게
    sns.set_style("darkgrid")
    sns.set_palette("pastel")

    sns.kdeplot(data=set_one, shade=True)
    sns.kdeplot(data=set_two, shade=True)
    sns.kdeplot(data=set_three, shade=True)
    sns.kdeplot(data=set_four, shade=True)
    plt.show()

# Box Plots

## Box Plots, Part I

- 데이터의 모양을 보여주는 KDE는 한번에 여러개의 KDE를 비교하기 어렵다. 또한 여러가지 통계적 정보들을 제공해주지 않는다. (outliers 같은 값들)
- Box Plot (aka box-and-whisker plot)은 KDE와 비슷하게 데이터가 얼마나 분포되어있는지 보여준다.
- 하지만 Box Plot은 데이터셋의 범위를 보여주고, 데이터의 상당부분이 어디에 있는지, 특이치(outlier)가 있는지 여부에 대한 아이디어를 제공해준다.

- Box Plot 설명
    1. 박스는 IQR (Interquartile Range)을 나타낸다.
    2. 박스 중간에 존재하는 선은 median (중간값)을 나타낸다.
    3. 끝나는 선 두개는 각각 1st quartile, 3rd quartile이다.
    4. 다이아몬드는 outliers들을 보여준다.

    ![](https://s3.amazonaws.com/codecademy-content/programs/dataviz-python/unit-5/intro-to-seaborn/seaborn_distributions/box-plot-white.svg)

## Box Plots, Part II

- KDE plot 대신 Box plot을 사용하는 이점은 여러개의 데이터를 plot하는게 쉽고 분포도를 비교하기 쉽다.

        sns.boxplot(data=df, x='label', y='value')
        plt.show()

    ![](Untitled-53e1a8a4-694d-4cad-8d8b-85fe976ddc56.png)

  - Box plot은 차이를 확실하게 볼 수 있다. 하지만 dataset3이 bimodal인건 보여주지 않는다.

- `sns.boxplot()` 메소드를 이용해 plot한다.
  - `data` : DataFrame, List, Array 등
  - `x` : 1차원 데이터, Series, List, Array 등등
  - `y` : 또다른 1차원 데이터셋
- `x`와 `y`에 Pandas Series를 사용하면 각각 축에대한 라벨을 자동으로 설정해준다.

# Violin Plots

## Violin Plots, Part I

- 다수의 히스토그램을 그릴 순 있지만 분포를 비교하기엔 좋은 방법이 아니다.
- Seaborn은 Violin plot이라는 분포를 비교하기 적절한 옵션을 제공한다.
- Violin plot은 Box plot보다 더 많은 정보를 제공한다. 각 데이터 포인트를 매핑시키는게 아닌 KDE에 의한 면적을 얻기 때문이다. 뭔솔?

- Violin plot
  - 중심선을 기준으로 두개의 KDE plot이 있다.
  - 중앙에 하얀점은 median을 의미한다.
  - violin 중간에 있는 굵은 검정색 선은 IQR을 의미한다.
  - 중간 확장된 부분은 신뢰구간이다. 95%

## Violin Plots, Part II

- `sns.violinplot()`
  - `data` : List, DataFrame, Array
  - `x`, `y`, `hue` : 1차원 데이터집합 Series, List, Array
  - `sns.boxplot()`의 매개변수는 전부 가능

    sns.violinplot(data=df, x="label", y="value")
    plt.show()

![](Untitled-ff3e9693-1ea9-48fa-aa88-750c4c0e362c.png)

- Violin plot은 분포를 시각적으로 보고 비교할 수 있다. 위 예시를 보고 dataset1은 skewed left, dataset3은 bimodal이라는 것을 알 수 있다.

## Review

- KDE plot : Kernel density estimator; 스무스한 데이터셋을 보여준다
- Box plot : median, IQR, outliers를 보여주는 plot
- Violin plot : KDE와 Box plot을 합친 plot. 여러개의 분포를 한눈에 보는데 적합하다.

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)
