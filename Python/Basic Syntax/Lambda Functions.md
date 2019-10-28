# Lambda Functions

Class: Basic Syntax
Created: Sep 23, 2019 9:23 PM
Edited: Oct 14, 2019 4:21 PM
Reviewed: No

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)

---

---

# Lambda Functions

---

## Lambda Functions

- 함수를 간단하게 정리할 수 있는 기법

    add_two = lambda my_input: my_input + 2

이 코드는:

    print(add_two(3))    # 5
    print(add_two(100))  # 102
    print(add_two(-2))   # 0

1. `add_two`라는 변수에 함수를 저장했다.

2. `lambda`라는 키워드를 이용해 `lambda functiond`을 명시했다. (`def` 와 비슷하다.)

3. `my_input` : 매개변수를 뜻한다.

4. 인자로 전달받은 `my_input`에 2를 더해 반환한다. (`return` 생략)

    is_substring = lambda my_string: my_string in "This is the master string"

    print(is_substring('I'))       # False
    print(is_substring('am'))      # False
    print(is_substring('the'))     # True
    print(is_substring('master'))  # True

`if`문을 사용한 람다식은 아래와 같다.

    <WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>

    check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

특이하게도 `if` 문의 조건식이 `if` 앞에 나온다.

람다함수는 한줄로만 작동한다.

한번만 사용하고 말 함수들을 작성할 때 좋다.

함수를 정의하는것이 아니기때문에 람다함수는 재사용이 불가능하다.

---

## 예제

    double_or_zero = lambda num : num * 2 if num > 10 else 0
    
    print double_or_zero(15)
    # prints 30
    print double_or_zero(5)
    # prints 0

`num`이 짝수면 `"even"`을, 홀수면 `"odd"`를 반환한다.

    even_or_odd = lambda num : "even" if num % 2 == 0 else "odd"
    
    print even_or_odd(10)
    print even_or_odd(5)

`num`이 `3`으로 나누어 떨어지는지 확인하는 람다식

    multiple_of_three = lambda num : "multiple of three" if num % 3 == 0 else "not a multiple"
    
    print multiple_of_three(9)
    print multiple_of_three(10)

`num`을 일의자리 숫자로 반환하는 식

    ones_place = lambda num : num % 10
    
    print ones_place(123)
    print ones_place(4)

`num`의 제곱을 2 곱해서 반환

    double_square = lambda num : num ** 2 * 2 # or num * num * 2
    
    print double_square(5)
    print double_square(3)

`num`에 1부터 10까지의 난수를 더하는 식

    import random
    add_random = lambda num : num + random.randint(1, 10)
    
    print add_random(5)
    print add_random(100)

---

[Python](./Python-e30b406c-0174-45c4-87ee-c876cf4525b5.csv)