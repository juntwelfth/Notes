# Line Graphs in Matplotlib

- Matplotlib는 차트와 그래프를 만드는 파이썬 라이브러리이다.

```py
from matplotlib import pyplot as plt
```

## Basic Line Plot

- `plot()` 메소드로 선을 그리고 `show()` 메소드로 프린트할 수 있다.

```py
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]

plt.plot(x_values, y_values)
plt.show()
```

![line](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/parabola.png)

## Basic Line Plot II

- matplotlib는 두개이상의 선을 그릴 수 있고, 자동으로 선의 색깔을 다르게 보여준다.

```py
days = [0, 1, 2, 3, 4, 5, 6]

money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]

plt.plot(days, money_spent)
plt.plot(days, money_spent_2)

plt.show()
```

![line 2](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/money_spent_2.png)

> A vs B는 x값에 B를, y값에 A를 넣으라는 뜻이다. `plot(B, A)`

## Linestyles

- `color` 키워드를 이용해 선의 색을 지정해줄 수 있다.

```py
plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')  # 회색
```

HTML color name, HEX code를 이용해줄 수 있다.

- `linestyle` 키워드를 이용해 선의 형태를 지정해줄 수 있다.

```py
# 점선과 실선 중간
plt.plot(x_values, y_values, linestyle='--')
# 점선
plt.plot(x_values, y_values, linestyle=':')
# 안보임
plt.plot(x_values, y_values, linestyle='')
```

- `marker` 키워드는 마커를 추가해준다.

```py
# 원 마커
plt.plot(x_values, y_values, marker='o')
# 사각형
plt.plot(x_values, y_values, marker='s')
# 별표
plt.plot(x_values, y_values, marker='*')
```

## Axis and Labels

- `plt.axis()` 메소드를 이용해 줌을 해줄수도 있다.
  - 총 4개의 요소를 지닌 list를 인자로 전달한다.
    1. x의 최소값
    2. x의 최대값
    3. y의 최소값
    4. y의 최대값

x값을 0부터 3까지, y값을 2부터 5까지 보고싶다면

```py
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]
    plt.plot(x, y)
    plt.axis([0, 3, 2, 5])
    plt.show()
```

![zoom](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/axis_zoom.png)

## Labeling the Axes

- `plt.xlabel()` : x축에 라벨 붙여주기
- `plt.ylabel()` : y축에 라벨 붙여주기
- `plt.title()`   : 제목 정해주기
- 항상 string 값으로 전달해줘야 한다.

```py
hours = [9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3,
    9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]
plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/axis_labels.png)

## Subplots Part I

- 다수의 그래프가 한 그림안에 있을때 각각 그래프를 *subplot*이라고 부른다.
- 이러한 subplot을 담고있는 사진이나 오브젝트를 *figure*라고 부른다.

>아래 figure는 2개의 row와 3개의 column을 가지고 있다.

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/six_subplots.svg)

- `subplot()` 메소드를 이용해 subplot을 생성할 수 있다.
  - 3개의 인자가 필요하다.
    1. row 크기
    2. column 크기
    3. index 만들고 싶은 subplot의 index

```py
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

plt.show()
```

![a](https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/two_subplots.svg)

> subplot먼저 plot은 나중에

## Subplots Part II

- 가끔 subplot이 서로 오버랩될 때가 있다.

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/overlapping_subplots.png)

- subplot들 사이를 커스터마이즈할 수 있다.
- `plt.subplots_adjust()`
  - `left`    : 왼쪽 마진, default = 0.125, y축 라벨을 위해 늘려줄 수 있음
  - `right`  : 오른쪽 마진, default = 0.9, 전체적인 크기 조절 가능
  - `bottom` : 아래 마진, default = 0.1, x축 라벨을 위해 늘려줄 수 있음
  - `top`      : 위 마진, default = 0.9
  - `wspace` : subplot의 수평 공간, default = 0.2
  - `hspace` : subplot의 수직 공간, default = 0.2
- `plt.subplots_adjust(top=0.95, hspace=0.25)` 이런식으로 수정해줄 수 있다.

1. 위 subplot은 2 rows, 1 column, 1번째

2. 아래 왼쪽 : 2 rows, 2 columns, 2번째

3. 아래 오른쪽: 2 rows, 2 columns, 4번째

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/subplot_adjust_ckpt.png)

## Legends

- 여러개의 선이 있을 때 `plt.lenend()` 메소드를 이용해서 각각의 선에 이름을 붙여줄 수 있다.
- `legend` 메소드는 list로 인자를 받는다.

```py
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
plt.legend(['parabola', 'cubic'])
plt.show()
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/legend.png)

- `loc` 키워드를 인자로 받으면 포지션을 정해줄 수 있다. (0 ~ 10)

![a](https://i.imgur.com/9MPe0JE.png)

```py
plt.legend(['parabola', 'cubic'], loc=6)
plt.show()
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/legend_loc.png)

- 굳이 legend에 인자로 전달 할 필요없이 각 plot에서 이름을 정해줄 수 있다.

```py
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16],
    label="parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64],
    label="cubic")
plt.legend() # Still need this command!
plt.show()
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/legend.png)

>이 경우에도 `plt.legend()`는 필수

## Modify Ticks

- 그래프에 tick을 지정해주고 싶을때

```py
ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/tick_marks.png)

- `ax.set_yticks()`를 이용해 y축 tick도 수정이 가능하다.
- 특별한 라벨(string)을 원할 땐 `ax.set_xticklabels()`을 이용해주자.

>y축의 tick을 0.1, 0.6, 0.8로 설정하고 10% 60% 80%로 보이게 하고 싶다면

```py
ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])
```

![a](https://s3.amazonaws.com/codecademy-content/courses/matplotlib/y_ticks.png)

## Figures

- 여러개의 plot을 만들 때 plot은 되었지만 display되지 않은 경우가 종종있다. 이러한 plot들은 그 다음 plot에서 나오게된다.
- `plt.close('all')` 메소드를 이용해 모든 plot을 지워주고 다음 plot을 만드는게 좋다.

- 두개 이상의 figure를 만들 때 `plt.figure()` 메소드를 이용해 만들어 줄 수 있다.
  - `figsize=(width, height)` 키워드를 추가해 사이즈 조절도 가능하다.
  - `plt.figure(figsize=(4, 10))`

- 이렇게 만든 figure들은 `plt.savefig()` 메소드를 이용해 저장할 수도 있다.
  - png, svg, pdf로 확장자를 설정해줄 수 있다.
  - `plt.savefig('my_file.png')`
