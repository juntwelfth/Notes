# Creating, Loading, and Selecting Data with Pandas

Class: Analyze Data,Visualize Data
Created: Oct 13, 2019 12:54 PM
Edited: Oct 25, 2019 11:01 AM
Reviewed: No
Sub_Class: Pandas

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Creating, Loading, and Selecting Data with Pandas

---

## Importing the Pandas Module

- Pandas는 파이썬에서 테이블 형식의 데이터를 다루기 위해 존재하는 모듈이다. (테이블 형식의 데이터란, 행과 열이 존재하는 데이터를 말한다.)
- 먼저 Pandas 모듈을 설치하고, 파이썬파일에 import를 해주어야 한다.

    import pandas as pd

---

## Create a DataFrame I

- DataFrame은 행과 열로 구분된 데이터를 저장한 객체다.
- Spreadsheet, SQL 테이블이라고 생각하면 된다.
- 직접 DataFrame을 만들 수도 있고, CSV나 엑셀 spreadsheet, SQL 쿼리에서 가져올 수도 있다.

- DataFrame에는 row와 column이 있다.
- 각각의 column은 이름이 있고, 그 이름은 string이다.
- 각각의 row는 index값을 가지고, 숫자로 되어있다.
- DataFrame은 다양한 종류의 데이터를 포함한다. 스트링, 정수, 실수, 튜플 등등

- 이러한 데이터들을 `pd.DataFrame()`을 이용해 dictionary로 전달할 수 있다.

value값들의 길이는 항상 같아야한다. 그렇지 않으면 에러발생

    df1 = pd.DataFrame({
        'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
        'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
        'age': [34, 28, 51]
    })

위 명령은 `df1`이라는 DataFrame을 만들어내고 아래와 같이 생겼다.

    address                 age         name
    123 Main St.            34          John Smith
    456 Maple Ave.          27          Adam Doe
    789 Broadway            51          Joe Schmo

각각의 column들은 가나다순으로 정렬된다. dictionary에는 순서가 없기때문

    import pandas as pd
    
    df1 = pd.DataFrame({
      'Product ID': [1, 2, 3, 4],
      'Color': ['blue', 'green', 'red', 'black'],
      'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt']
    })
    
    print(df1)

![](Untitled-f1d550aa-caaa-4bda-9311-22da7d60a0db.png)

---

## Create a DataFrame II

- dictionary를 이용하지 않고 list를 이용해 DataFrame을 만들수 있다.
- columns 키워드를 이용해 column의 이름을 설정해줄 수 있다.

    df2 = pd.DataFrame([
        ['John Smith', '123 Main St.', 34],
        ['Jane Doe', '456 Maple Ave.', 28],
        ['Joe Schmo', '789 Broadway', 51]
        ],
        columns=['name', 'address', 'age'])

위 명령은 `df2`라는 DataFrame을 만들어내고 아래와 같이 생겼다.

    name              address              age
    John Smith        123 Main St.         34
    Adam Doe          456 Maple Ave.       27
    Joe Schmo         789 Broadway         51

list를 이용한 DataFrame은 우리가 작성한 순서대로 column의 이름들이 생성된다. list에는 순서가 있으니깐.

    import pandas as pd
    
    df2 = pd.DataFrame([
      [1, 'San Diego', 100],
      [2, 'Los Angeles', 120],
      [3, 'San Francisco', 90],
      [4, 'Sacramento', 115]
    ],
      columns=[
        'Store ID', 'Location', 'Number of Employees'
      ])
    
    print(df2)

![](Untitled-2b2d794e-b008-4b21-ba0c-e72b9d5bf4f5.png)

---

## Loading and Saving CSVs

- CSV데이터 파일이 있을 때, `read_csv()`를 이용해 DataFrame으로 만들 수 있다.

    pd.read_csv('my-csv-file.csv')

my-csv-file이라는 csv파일을 불러오는 방법

    df.to_csv('new-csv-file.csv')

new-csv-file이라는 이름의 csv파일을 만드는 방법

---

## Inspect a DataFrame

- DataFrame을 만들고 확인을 할 때, small DataFrame의 경우 단순히 print를 해주면 된다.
- large DataFrame의 경우 전체를 보기보다 부분 부분만 보면된다.
- `head(n)` 메소드는 처음부터 n번째 줄 까지 보여준다. (default값 = 5)
- `info()` 메소드는 각각의 column의 상태를 보여준다.

    import pandas as pd
    
    df = pd.read_csv('imdb.csv')
    
    print(df.head())
    '''
    id                                       name   genre  year  imdb_rating
    0   1                                     Avatar  action  2009          7.9
    1   2                             Jurassic World  action  2015          7.3
    2   3                               The Avengers  action  2012          8.1
    3   4                            The Dark Knight  action  2008          9.0
    4   5  Star Wars: Episode I - The Phantom Menace  action  1999          6.6
    '''
    print(df.info())
    '''
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 220 entries, 0 to 219
    Data columns (total 5 columns):
    id             220 non-null int64
    name           220 non-null object
    genre          220 non-null object
    year           220 non-null int64
    imdb_rating    220 non-null float64
    dtypes: float64(1), int64(2), object(2)
    memory usage: 8.7+ KB
    None
    '''

---

## Select Columns

- 특정 column을 선택할 땐 dictionary value값을 불러올 때와 같이 `customers['age']` 이런식으로 불러오거나 `customers.age` 이런식으로 불러오면 된다.

    import pandas as pd
    
    df = pd.DataFrame([
      ['January', 100, 100, 23, 100],
      ['February', 51, 45, 145, 45],
      ['March', 81, 96, 65, 96],
      ['April', 80, 80, 54, 180],
      ['May', 51, 54, 54, 154],
      ['June', 112, 109, 79, 129]],
      columns=['month', 'clinic_east',
               'clinic_north', 'clinic_south',
               'clinic_west']
    )
    
    clinic_north = df.clinic_north
    
    print(type(clinic_north))
    # <class 'pandas.core.series.Series'>
    
    print(type(df))
    # <class 'pandas.core.frame.DataFrame'>

---

### Selecting Multiple Columns

- 두개 이상의 column을 불러올 땐 list를 사용한다.
- `new_df = orders[['last_name', 'email']]`
- 대괄호를 두개 붙이는것에 유의

    import pandas as pd
    
    df = pd.DataFrame([
      ['January', 100, 100, 23, 100],
      ['February', 51, 45, 145, 45],
      ['March', 81, 96, 65, 96],
      ['April', 80, 80, 54, 180],
      ['May', 51, 54, 54, 154],
      ['June', 112, 109, 79, 129]],
      columns=['month', 'clinic_east',
               'clinic_north', 'clinic_south',
               'clinic_west']
    )
    
    clinic_north_south = df[['clinic_north', 'clinic_south']]
    
    print(type(clinic_north_south))
    # <class 'pandas.core.frame.DataFrame'>

하나의 column을 불러왔을 땐 series의 타입이었는데 여러개를 불러오면 DataFrame 타입이다.

---

## Select Rows

- row 전체를 불러오고 싶을 땐 list에 접근하는 방식으로 접근하면 된다.
- DataFrame은 zero-indexed이다. (index가 0부터 시작함)
- `iloc`을 이용해야 한다.

    import pandas as pd
    
    df = pd.DataFrame([
      ['January', 100, 100, 23, 100],
      ['February', 51, 45, 145, 45],
      ['March', 81, 96, 65, 96],
      ['April', 80, 80, 54, 180],
      ['May', 51, 54, 54, 154],
      ['June', 112, 109, 79, 129]],
      columns=['month', 'clinic_east',
               'clinic_north', 'clinic_south',
               'clinic_west'])
    
    march = df.iloc[2]

row를 불러올 땐 series로 불러온다.

---

### Selecting Multiple Rows

- 두개 이상의 row를 불러올 땐 다중 list를 불러올때와 같이 하면된다.
- `iloc[2:5]` (뒤 숫자는 포함하지 않음)

    import pandas as pd
    
    df = pd.DataFrame([
      ['January', 100, 100, 23, 100],
      ['February', 51, 45, 145, 45],
      ['March', 81, 96, 65, 96],
      ['April', 80, 80, 54, 180],
      ['May', 51, 54, 54, 154],
      ['June', 112, 109, 79, 129]],
      columns=['month', 'clinic_east',
               'clinic_north', 'clinic_south',
               'clinic_west']
    )
    
    april_may_june = df.iloc[-3:]    # 뒤에서 3번째부터 끝까지
    print(april_may_june)

---

## Select Rows with Logic

- 논리연산자를 이용해서 특정 조건을 통과하는 row만 선택할 수 있다.
- `df[df.MyColumnName == desired_column_value]`

    import pandas as pd
    
    df = pd.DataFrame([
      ['January', 100, 100, 23, 100],
      ['February', 51, 45, 145, 45],
      ['March', 81, 96, 65, 96],
      ['April', 80, 80, 54, 180],
      ['May', 51, 54, 54, 154],
      ['June', 112, 109, 79, 129]],
      columns=['month', 'clinic_east',
               'clinic_north', 'clinic_south',
               'clinic_west'])
    
    # month가 January인 row
    january = df[df.month == 'January']
    
    # month가 March이거나 April인 row
    march_april = df[(df.month == 'March') | (df.month == 'April')]
    
    # month가 January, February, March인 경우
    january_february_march = df[df.month.isin(['January', 'February', 'March'])]
    test = df[df.month == 'January' | df.month == 'February' | df.month == 'March']

- `isin()` 명령어를 통해 리스트에 존재하는지 확인할 수 있다.
- `isin()`의 인자로는 리스트가 온다.

    df[df.name.isin(['Martha Jones',
         'Rose Tyler',
         'Amy Pond'])]

---

## Setting indices

- 논리연산자를 통해 데이터를 선택할 때 연속적이지 않은 index 때문에 곤란할 때가 있다.

              First Name         Last Name
        0     John               Smith
        4     Jane               Doe
        7     Joe                Schmo

- `reset_index()` 메소드를 통해 인덱스를 초기화 시켜줄 수 있다.
    - `df.reset_index()` 명령어를 사용하면 아래와 같은 새로운 DataFrame을 반환한다.

          index          First Name         Last Name
    0     0              John               Smith
    1     4              Jane               Doe
    2     7              Joe                Schmo

새로운 index라는 column이 생성되었는데 특수한 상황이 아니면 쓸 일이 없다.

`drop=True`라는 키워드를 사용하면 이런 불필요한 column을 생성하는것을 방지할 수 있다.

`df.reset_index(drop=True)`

아래는 새로운 DataFrame이다.

          First Name         Last Name
    0     John               Smith
    1     Jane               Doe
    2     Joe                Schmo

`reset_index()` 메소드는 새로운 DataFrame을 반환한다.

기존의 DataFrame을 수정하고 싶을 땐 `inplace=True` 키워드를 사용하면 된다.

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)