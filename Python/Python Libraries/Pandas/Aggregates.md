# Aggregates in Pandas

Class: Analyze Data,Visualize Data
Created: Oct 16, 2019 1:02 PM
Edited: Oct 25, 2019 11:01 AM
Reviewed: No
Sub_Class: Pandas

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Aggregates in Pandas

---

## Calculating Column Statistics

- `median()`

    중간값을 찾을 때

        print(customers.age)
        >> [23, 25, 31, 35, 35, 46, 62]
        print(customers.age.median())
        >> 35

- `nunique()`

    몇가지의 종류가 있는지

        print(shipments.state)
        >> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
        print(shipments.state.nunique())
        >> 3

- `unique()`

    각각의 종류를 리턴

        print(inventory.color)
        >> ['blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'orange', 'orange', 'orange']
        print(inventory.color.unique())
        >> ['blue', 'green', 'orange']

- `mean()`
    - column의 평균 값
- `std()`
    - 표준편차
- `max()`
    - 가장 큰 값
- `min()`
    - 가장 작은 값
- `count()`
    - 갯수

---

## Calculating Aggregate Functions I

- 데이터들의 평균값, 표준편차, 중간값 등등을 얻고 싶을 때

아래와 같은 데이터가 있을 때

    student	      assignment_name	       grade
    Amy	          Assignment 1	         75
    Amy	          Assignment 2	         35
    Bob	          Assignment 1	         99
    Bob	          Assignment 2	         35

각 학생별로 평균값을 얻고 싶으면 `.groupby` 메소드를 사용하면 된다.

    grades = df.groupby('student').grade.mean()

    student	          grade
    Amy	              80
    Bob	              90
    Chris	            75

`df.groupby('column1').column2.measurement()` 이렇게 생겼다.

`column1` : 그룹으로 묶고싶은 column (`'student'`)

`column2` : 계산하고 싶은 column (`'grade'`)

`measurement` : 계산식 (`mean`)

---

## Calculating Aggregate Functions II

- `groupby` 함수를 사용하면 DataFrame이 아닌 Series를 반환한다.
- `reset_index()`를 사용하면 Series가 DataFrame으로 변한다.
- 일반적으로 `groupby`는 `reset_index`와 함께 쓰인다.

    teas_counts = teas.groupby('category').id.count().reset_index()

groupby를 해주고 column의 이름을 바꿔주는 것도 잊지말자.

    teas_counts = teas_counts.rename(columns={"id": "counts"})

---

## Calculating Aggregate Functions III

- 때때로 연산이 `mean`이나 `count`보다 훨씬 복잡할 때가 있다.
- 이런 상황에선 `apply` 메소드와 람다식을 써줄 수 있다.
- 람다식의 인풋은 항상 list라는 것을 잊지말자.

아래와 같은 DataFrame에서 각 카테고리 별 75th percentile을 구한다고 했을 때

75th percentile은 상위 25%, 하위 75%를 말한다.

    id	      name	           wage	    category
    10131	    Sarah Carney	   39	      product
    14189	    Heather Carey	   17	      design
    15004	    Gary Mercado	   33	      marketing
    11204	    Cora Copaz	     27	      design

    # np.percentile can calculate any percentile over an array of values
    high_earners = df.groupby('category').wage.apply(lambda x: np.percentile(x, 75)).reset_index()

결과는 아래와 같다.

          category	       wage
    0   	design	         23
    1	    marketing	       35
    2	    product	         48

---

## Calculating Aggregate Functions IV

- 때때로 두개 이상의 column을 group하고싶을 때 `groupby` 메소드에 리스트를 전달하면 된다.

다른 장소, 다른 요일에 대한 데이터들이 있을 때

    Location	       Date	          Day of Week	    Total Sales
    West Village	   February 1	    W	              400
    West Village	   February 2	    Th	            450
    Chelsea	         February 1	    W	              375
    Chelsea	         February 2	    Th	            390

지역별, 요일별로 나누고 싶으면

    df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()

    Location	        Day of Week	        Total Sales
    Chelsea	          M	                  402.50
    Chelsea	          Tu	                422.75
    Chelsea	          W	                  452.00
    …		
    West Village	    M	                  390
    West Village	    Tu	                400
    …

column2 자리에는 뭐가 들어가든 상관없다

---

## Pivot Tables

- 피봇테이블 정리하기

pivot command

    df.pivot(columns='ColumnToPivot',
             index='ColumnToBeRows',
             values='ColumnToBeValues')

    # First use the groupby statement:
    unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
    # Now pivot the table
    pivoted = unpivoted.pivot(
        columns='Day of Week',
        index='Location',
        values='Total Sales')

    import numpy as np
    import pandas as pd
    
    orders = pd.read_csv('orders.csv')
    
    shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
    
    print(shoe_counts.head(10))
    
    shoe_counts_pivot = shoe_counts.pivot(
        columns='shoe_color',
        index='shoe_type',
        values='id').reset_index()
    
    print(shoe_counts_pivot)

    import pandas as pd
    
    # csv파일 읽어오기
    user_visits = pd.read_csv('page_visits.csv')
    
    # utm_source를 기준으로 각각 카운트
    click_source = user_visits.groupby('utm_source').id.count().reset_index()
    
    # utm_source를 기준, 각 월마다 카운트
    click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
    
    # 피봇테이블로 변환
    click_source_by_month_pivot = click_source_by_month.pivot(columns='month', index='utm_source', values='id').reset_index()

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)