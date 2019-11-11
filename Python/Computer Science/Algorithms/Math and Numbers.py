# Math and Numbers


def decimal_format():  # | 소수점 2번째자리까지 나오게 format
    '{0:.2f}'.format(1)
    #: 1.00


def Binary_and_decimal():  # | 2진수 10진수
    # 2진수에서 10진수로
    print(int('1001', 2))
    #: 9

    # 10진수에서 2진수로 (앞에 0b가 붙음)
    print(bin(25))
    #: 0b11001


def complex():  # | Complex형 숫자 실수로 바꾸기
    x = complex(2, 3)
    #: (2+3j)

    y = abs(x)
    print(y)
    #: 3.6055


def is_square():  # | Squared 숫자인지 판별
    # 아무 숫자 입력
    n = 4  # ? sqrt(n) ========== n ** 0.5

    # n ** 0.5를 1로 나눴을 때 나머지가 0이면 square
    n ** 0.5 % 1 == 0
    #: True : Square Number


def is_prime():  # | 소수인지 판별
    num = 11

    if num > 1:
        # 2 ~ num // 2까지 확인
        for i in range(2, num//2):
            # 만약 2 ~ num // 2 까지의 숫자 중 num의 약수가 나오면 소수가 아님
            if (num % i) == 0:
                return True

        return False

    return False  # ? 음수는 소수가 아니다.


def how_many_primes():  # | 범위 내 소수 개수
    # 2 ~ N 범위 내 소수 개수
    N = 10

    # 2는 소수니깐. 1부터 시작
    count = 1

    # 3부터 N까지 반복문
    for num in range(3, N + 1):
        for i in range(2, num):
            # 약수가 있으면 탈락
            if num % i == 0:
                break

        # 약수가 없으면 카운트 +1
        else:
            count += 1


#! 재귀함수
def factorial(n):  # | 팩토리얼
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial(n):  # | 내가만든 팩토리얼
    sum = 1

    while n > 1:
        sum *= n
        n -= 1

    return sum


#! 재귀함수
def sum_to_one(n):  # | n부터 1까지의 합
    # n이 1이면 재귀종료
    if n == 1:
        return n
    return n + sum_to_one(n - 1)


#! 재귀함수
def fibonacci(n):  # | 피보나치 수열
    # base cases
    if n == 1:
        return n
    if n == 0:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    # * 참고로 피보나치 수열의 시간복잡도는 2^N


def fibonacci(n):  # | 피보나치 구현
    if n == 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    n_1 = 0
    n_2 = 1
    sum = 0
    for i in range(n-1):
        sum = n_1 + n_2
        n_1 = n_2
        n_2 = sum
    return sum


#! 재귀함수
def sum_digits(n):  # | 모든 자리수의 합
    if n < 10:
        return n
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)


def sum_digits(n):  # | 모든 자리수 합 non recursive
    sum = 0
    for i in str(n):
        sum += int(i)

    return sum


def sum_digits(n):  # | 반복문 없이 모든 자리수 합
    # 먼저 자리수마다 스트링화 시켜서 list에 넣고
    a = list(str(n))
    # 다시 int로 바꾸기
    b = list(map(int, a))
    return sum(b)


#! 재귀함수
def multiplication(n1, n2, n3=0):  # | 곱셈 구현
    if n2 < 1:
        return n3
    return multiplication(n1, n2-1, n3+n1)
