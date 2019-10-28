# Numerical Python aka NumPy

Class: Analyze Data
Created: Sep 29, 2019 4:57 PM
Edited: Oct 01, 2019 5:54 PM
Reviewed: No
Sub_Class: NumPy

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Numerical Python

---

## Importing NumPy

- `NumPy` 라이브러리를 추가시키는 방법

    import numpy as np

항상 코드는 간결하게! (간단한 코드 = 더 적은 에러)

---

## NumPy Arrays

- `NumPy` 내장 특수 배열

    my_array = np.array([1, 2, 3, 4, 5, 6])

평범한 배열을 NumPy 배열로 바꾸는 방법또한 존재한다.

    my_list = [1, 2, 3, 4, 5, 6]
    my_array = np.array(my_list)

---

## Creating an Array from a CSV

- `NumPy`에선 배열에 직접 값을 입력하는 경우가 별로없다.
- 다른 데이터를 배열에 전달하는 경우가 많다.
- 대표적인 예로, CSV파일을 `genfromtxt()`을 이용해 가져올 수 있다.
- 이런식으로 가져온 데이터는 자동적으로 numpy array로 변환된다.

`sample.csv`

    34,9,12,11,7

    csv_array = np.genfromtxt('sample.csv', delimiter=',')

때때로 `csv`파일이 `,`가 아닌 다른 문자로 되어있을 때가 있다. `delimiter`를 잘 설정하자.

    >>> csv_array
    array([34, 9, 12, 11, 7])

---

## Operations with NumPy Arrays

- NumPy 배열은 파이썬 `list`보다 월등히 좋은 성능을 보여준다.

    # With a list
    l = [1, 2, 3, 4, 5]
    l_plus_3 = []
    for i in range(len(l)):
        l_plus_3.append(l[i] + 3)
    
    # With an array
    a = np.array(l)
    a_plus_3 = a + 3

파이썬에선 반복문을 사용하거나 List Comprehension을 사용해야 한다.

NumPy 배열은 단순히 3을 더하면 된다. 뺄셈, 곱셈, 나눗셈 전부 다 해당된다.

    >>> a ** 2    # 여기서 a는 이미 NumPy 배열임
    array([ 1,  4,  9, 16, 25, 36])
    
    >>> np.sqrt(a)
    array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])

---

## Operations with NumPy Arrays II

- NumPy 배열끼리의 연산도 가능하다.

    >>> a = np.array([1, 2, 3, 4, 5])
    >>> b = np.array([6, 7, 8, 9, 10])
    >>> a + b
    array([7,  9, 11, 13, 15])

    import numpy as np
    
    test_1 = np.array([92, 94, 88, 91, 87])
    test_2 = np.array([79, 100, 86, 93, 91])
    test_3 = np.array([87, 85, 72, 90, 92])
    test_3_fixed = test_3 + 2
    
    total_grade = test_1 + test_2 + test_3_fixed
    
    final_grade = total_grade / 3
    
    print(final_grade)
    # prints [86 93 82 92 90]

세 배열의 평균값을 구하는 방법

---

## Two-Dimensional Arrays

- 모든 일차원 배열의 크기가 같다면, 이차원배열로 만들 수 있다.

    # 일차원 배열
    test_1 = np.array([92, 94, 88, 91, 87])
    test_2 = np.array([79, 100, 86, 93, 91])
    test_3 = np.array([87, 85, 72, 90, 92])
    
    # 이차원 배열
    np.array([[92, 94, 88, 91, 87], 
              [79, 100, 86, 93, 91],
              [87, 85, 72, 90, 92]])

    np.array([[29, 49,  6], 
              [77,  1]])

위 코드는 실행은 되지만 이차원배열을 만들지 않는다.

    np.array([68, 16, 73],
             [61, 79, 30])

위 코드는 실행이 되지 않는다. 바깥 `[]`이 없기 때문

---

## Selecting Elements from a 2-D Array

- 2차원 배열에서 특정 요소를 선택할 때 `a[row,column]` 형식으로 선택할 수 있다.

![](Untitled-e9699e02-d41d-43fd-b78e-1b331840684f.png)

    a = np.array([[32, 15, 6, 9, 14], 
                  [12, 10, 5, 23, 1],
                  [2, 16, 13, 40, 37]])
    
    >>> a[2,1]
    16
    
    # selects the first column
    >>> a[ : , 0]
    array([32, 12,  2])
    
    # selects the second row
    >>> a[1, : ]
    array([12, 10,  5, 23,  1])
    
    # selects the first three elements of the first row
    >>> a[0, 0 : 3]
    array([32, 15,  6])

row 선택할 때       : `[x, : ]`         x번째 row 전부 선택
column 선택할 때 : `[ : , y]`        y번째 column 전부 선택
특정 요소 선택      : `[x, 0:3]`      x 번째 row, 0부터 2까지의 요소 

    temp = [[ 46.6  48.1  61.8  56. ]
            [ 50.   47.5  61.3  55.6]
    			  [ 49.7  47.2  60.9  55.2]
    				[ 49.5  47.1  60.6  54.9]
    				[ 49.2  46.9  60.2  54.5]]
    
    temp[0,:]
    # [ 46.6  48.1  61.8  56. ]
    
    temp[3:, 1]
    # [ 47.1  46.9]

![](Untitled-1ef14dd7-85b5-4b58-8683-e201a4771ca1.png)

---

## Logical Operations with Arrays

- 파이썬 `list comprehension`, 자바스크립트의 `filter`처럼 특정 조건을 주고 결과를 알 수 있다.

    >>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
    >>> a > 5
    array([True, False, False, False, False, False, True, True, True, True], dtype=bool)

    >>> a[a > 5]
    array([10, 9, 8, 9, 7])

    >>> a[(a > 5) | (a < 2)]
    array([10, 9, 8, 9, 7])

`&` (and) and `|` (or) 연산자를 사용해서 조건문을 만들 수 있다.

    porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
    
    # less than 60
    cold = porridge[porridge < 60]
    
    # greater than 80
    hot = porridge[porridge > 80]
    
    # between 60 and 80
    just_right = porridge[(60 < porridge) & (porridge < 80)]

조건문을 쓸 땐 항상 괄호안에 넣어주기

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)