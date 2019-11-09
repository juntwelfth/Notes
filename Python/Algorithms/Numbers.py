# Numbers


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
