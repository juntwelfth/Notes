# Modifying DataFrames

## Adding a Column

- DataFrame에 새로운 column을 추가하고 싶을 때
- dictionary에 요소를 추가하는 방식과 비슷하게 접근할 수 있다.

    ```py
    df['Quantity'] = [100, 150, 50, 35]
    ```

- 전부 같은 값을 추가하고 싶을 땐 아래와 같이 하면 된다.

    ```py
    df['In Stock?'] = True
    ```

- 이미 존재하는 column에 더하기, 곱셈 등 수식을 이용하여 추가할 수도 있다.

    ```py
    df['Sales Tax'] = df.Price * 0.075
    ```

## Performing Column Operations

- DataFrame의 값들을 일괄수정하는 방법
- `apply()` 함수를 이용하면 된다.

df의 이름들을 전부 대문자로 고치고 싶을 때

```py
from string import upper

df['Name'] = df.Name.apply(upper)
```

```py
from string import lower
import pandas as pd

df = pd.DataFrame([
    ['JOHN SMITH', 'john.smith@gmail.com'],
    ['Jane Doe', 'jdoe@yahoo.com'],
    ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df.Name.apply(lower)
```

## Applying a Lambda to a Row

- 두개 이상의 column을 한번에 수정해줄 수 있다.
- `apply`키워드를 특정 column 없이 사용하고 `axis=1`이라는 인자를 전달해주면 된다.

아래와 같은 데이터가 있을 때

```py
Item           Price     Is taxed?
Apple          1.00      No
Milk           4.20      No
Paper Towels   5.00      Yes
Light Bulbs    3.75      Yes
```

- 세금이 붙은 가격이 아닌 가격엔 7.5%의 세금을 더해주고 새로운 column을 만들고 싶으면

```py
df['Price with Tax'] = df.apply(lambda row:
    row['Price'] * 1.075
    if row['Is taxed?'] == 'Yes'
    else row['Price'],
    axis=1
)
```

## Renaming Columns I

- `.columns` 속성을 통해 column의 이름을 바꿔줄 수 있다.
- 순서를 지켜줘야 한다.

```py
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']
```

## Renaming Columns II

- `rename()` 메소드를 이용해 이름을 바꿔줄 수도 있다.
- `rename`과 `columns`을 사용하면 새로운 DataFrame을 만들어낸다. 그래서 `inplace=True`를 인자로 전달해 기존 DataFrame을 수정시켜 줄 수 있다.
- `.columns`보다 `.rename`을 더 선호하는 이유
  - 특정 column만 이름을 바꿔줄 수 있다.
  - 시각적으로 보기 더 편하고 어떤걸 바꿔주는지 볼 수 있다.

`{'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}`

```py
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)

df.rename(columns={
    'name': 'movie_title'
}, inplace=True)
```

- 기존 column 이름의 스펠링이 틀리면 아무변화도 일어나지 않는다.
