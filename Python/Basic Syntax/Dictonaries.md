# Dictionaries

Class: Basic Syntax
Created: Sep 22, 2019 6:23 PM
Edited: Oct 01, 2019 6:04 PM
Reviewed: No

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Dictionary

---

## Dictionary

- Dictionary는 curly braces `{}` 로 감싸져있음
- 상수 key와 변수 value로 이루어져있음
- 순서가 없음 (index가 없음)
- value는 어떤것이든 올 수 있음 (number, string, list, dictionary 등)
- key값엔 list, dictionary가 올 수 없음
- 빈 dictionary를 만들 수 있음
- key 중복 가능, 하지만 마지막에 추가된게 우선순위 높음

    menu = {'a': 3, 'b': 2, 'c': 5}
    
    menu['d'] = 4

Javascript의 객체처럼 `menu['d'] = 4` 로 새로운 요소를 추가할 수 있다.

---

## Update Dictionary

- Dictionary에 새로운 요소 추가하기

    menu = {'a': 3, 'b': 2, 'c': 5}
    
    menu.update({'d': 4, 'e': 6, 'f': 1})
    
    print(menu)
    # prints {'a': 3, 'b': 2, 'c': 5, 'd': 4, 'e': 6, 'f': 1}

다수의 요소를 추가할 때 유용하다.

---

## List Comprehensions

- 리스트 반복문처럼 dictionary도 반복문을 이용해 만들 수 있다.

    names = ['Jenny', 'Alexus', 'Sam', 'Grace']
    heights = [61, 70, 67, 64]
    
    students = {key:value for key, value in zip(names, heights)}
    
    print(students)
    # prints {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

    # 배열안에 있는 Ceballos의 갯수를 세는 법
    total = sum([1 for i in array if i == 'Ceballos'])

---

## Invalid Key

- 존재하지 않는 Key값을 불러올 때 발생하는 예외

    building = {"63 building": 828, "Lotte Tower": 1320, "One World Trade": 541.3}
    
    print(building["Landmark 81"])
    # prints KeyError: 'Landmark 81'
    
    key_to_check = "Landmark 81"
    
    if key_to_check in building:
    	  print(building["Landmark 81"])

Error를 피하기 위해 `if`문 이용

---

## Try / Except to Get a Key

- 예외처리

    key_to_check = "Landmark 81"
    
    try:
    	  print(building_heights[key_to_check])
    except KeyError:
    	  print("That key doesn't exist!")

---

## Get Attribute

- `get()`키워드를 이용해 Value값을 얻어올 수 있다.

    building = {"63 building": 828, "Lotte Tower": 1320, "One World Trade": 541.3}
    
    print(building.get("63 building"))
    # prints 828
    print(building.get("Landmark 81"))
    # prints None
    print(building.get("Landmark 81", 10))
    # prints 10

`get()` 키워드는 예외가 발생하지 않아 안전하다.

default 값을 지정해줄 수 있다.

---

## Pop

- `pop()` 키워드는 `get()` 키워드와 비슷하지만 원래 dictionary에서 삭제한다.

    building = {"63 building": 828, "Lotte Tower": 1320, "One World Trade": 541.3}
    
    a = building.pop("63 building")
    print(a)
    # prints 828
    
    b = building,pop("Landmark 81")
    # KeyError
    
    c = building,pop("Landmark 81", 10)
    print(c)
    # prints 10
    
    print(building)
    # prints {"Lotte Tower": 1320, "One World Trade": 541.3}

---

## List and Keys

- `list()` : dictionary의 모든 key를 반환한다.
- `keys()` : dict_keys 객체를 반환한다. dict_keys 객체는 읽기전용이라 수정이 불가능하다.
하지만 dictionary의 key를 불러올 때 자주 사용한다.

    test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], 
    	  "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], 
    	  "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
    
    print(list(test_scores))
    # prints ['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Dina']
    
    for student in test_scores.keys():
    	  print(student)
    
    """
    'Grace'
    'Jeffrey'
    'Sylvia'
    'Pedro'
    'Martin'
    'Dina'
    """

---

## Get Values from Dictionaries

- `values()` : dict_values 라는 객체를 반환한다.
- value 값을 리스트로 반환하는 메소드는 따로 없지만 정 원한다면 `list(test_scores.values())`를 이용해서 얻을 수 있음 (권장하지 않음)

    test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], 
    	  "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], 
    	  "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
    
    for score in test_scores.values():
    	  print(score)
    
    """
    [80, 72, 90]
    [88, 68, 81]
    [80, 82, 84]
    [98, 96, 95]
    [78, 80, 78]
    [64, 60, 75]
    """

---

## Get Keys and Values

- `items()` : `keys()`, `values()`와 같이 `dict_list object`를 튜플로 반환한다. (key, value)

    biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, 
    	  "Coca-Cola": 69.7, "Amazon": 64.8}
    
    for company, value in biggest_brands.items():
    	  print(company + " has a value of " + str(value) + " billion dollars.")
    
    """
    Apple has a value of 184 billion dollars.
    Google has a value of 141.7 billion dollars.
    Microsoft has a value of 80 billion dollars.
    Coca-Cola has a value of 69.7 billion dollars.
    Amazon has a value of 64.8 billion dollars.
    """

각 함수에 예외를 raise(던지는) 조건문을 넣어줬다.
냉장고에서 음식을 꺼낼 때 KitchenException 예외가 발생하면 음식을 주문한다.

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)