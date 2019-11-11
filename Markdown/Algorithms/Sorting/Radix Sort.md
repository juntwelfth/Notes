# Radix Sort

Radix Sort(기수 정렬)는 대단히 빠른 정렬중 하나다. 자리수를 비교해서 정렬하는 방식이며 단점으로는 자리수가 없는 숫자들은 정렬할 수 없다. 예를들면 부동소수점같은 경우

하지만 문자열과 정수는 거의 다 정렬할 수 있다.

핵심 아이디어는 자리수를 이용하여 다른 위치에서 사용될 때 다른값을 나타낸다는 점을 이용하는 것이다. 26에서 숫자 6은 6을 나타내지만 86452에선 6000을 나타내는 것과 같이 말이다.

![n](https://s3.amazonaws.com/codecademy-content/courses/radix-sort/radix1.svg)

## Base Numbering Systems

다른 자리수에 있는 같은 숫자는 10의 배수로 차이가난다. 이 말은 오른쪽 끝에 있는 숫자 '8'은 8의 값과 같다는 말이고 한칸 왼쪽으로 가게되면 `10 * 8` (80)이 된다는 말이다. 한번 더 왼쪽으로 옮기면 `10 * 10 * 8`이 된다.

지수를 통일하는것이 아주 유용할 것이다. $10^0$은 1과 같다는 것은 아주 중요하다.

![2](https://s3.amazonaws.com/codecademy-content/courses/radix-sort/radix2.svg)

## Sorting By Radix

Radix Sort에는 두가지 방법이있다. 첫번째로는 MSD(최상위 유효 자릿수), 그리고 다른 하나는 LSD(최하위 유효 자릿수)가 있다.

두 방법 모두 입력받은 list를 열개의 "buckets"로 구성한다. 숫자는 MSD(가장 왼쪽 숫자) 혹은 LSD(가장 오른쪽 숫자)를 기준으로 바구니에 배치된다. 예를들어 숫자 2367은 MSD의 경우 bucket "2", LSD의 경우 "7"에 배치된다.

이러한 과정은 가장 긴 숫자의 모든 숫자가 고려될때까지 반복된다. 각 반복마다 버킷 내 순서가 유지된다. 예를들어 숫자 23, 25, 126은 초기 LSD bucketing으로 "3", "5", "6"에 배치된다. 알고리즘의 두번째 반복에서 이들은 모두 "2" 버킷에 배치되어 있지만 순서는 `23, 25, 126`으로 보존된다.

![3](https://s3.amazonaws.com/codecademy-content/courses/radix-sort/radix3.svg)

## Performance

Radix Sort의 가장 놀라운 기능은 비교를 하지않고 정수로 이루어진 list를 정렬할 수 있다는 것이다. (non-comparison sort라고 불리운다.)

이로인해 대부분의 다른 비교 기반 정렬과 비교하기가 어려워진다. 길이 *n*의 list를 생각해보자. 알고리즘을 반복 할 때마다 n개의 항목을 배치 할 버킷을 결정한다.

각 숫자를 검사할 때까지 계속 반복한다는 점을 통해 얼마나 많은 자릿수를 반복해서 하는지 알 수 있다. 이러한 평균 자리수를 word-size 혹은 w라고한다.

이것은 Radix Sort의 복잡성이 O(wn)임을 의미한다. list의 길이가 자리수보다 훨씬 크다고 가정하면 w를 상수 인자로 간주 할 수 있으며 이를 O(n)으로 줄일 수 있다.

쉽게말해 가장 큰 자리수만큼 반복한다.

![3](https://s3.amazonaws.com/codecademy-content/courses/radix-sort/radix4.svg)

## 순서

1. 가장 큰 숫자를 찾는다.

    ```py
    # 가장 큰 숫자
    maximum_value = max(to_be_sorted)

    # 가장 큰 숫자의 자리수(길이)
    max_exponent = len(str(maximum_value))
    ```

2. 주어진 list의 복사본을 만들고 bucket을 만들어준다.

    ```py
    being_sorted = to_be_sorted[:]
    digits = [[] for digit in range(10)]
    ```

3. Bucketing, 각 숫자의 각 자리수에 대한 바구니를 만들고 채워준다.

    ```py
    # 복사한 list에 모든 숫자에 접근
    for number in being_sorted:
        # 그 숫자들을 string화 시키고
        number_as_a_string = str(number)
        # 해당 숫자의 마지막 자리수를 digit에 저장 (string)
        digit = number_as_a_string[-1]
        # int화
        digit = int(digit)
        # 해당 bucket에 숫자 추가
        digits[digit].append(number)
    ```

4. Rendering, 복사한 배열에 있는 모든 숫자는 `digits`에 들어갔으니 비워준다. 그리고 다시 숫자들로 채워준다.

    ```py
    being_sorted = []

    for numeral in digits:
        being_sorted.extend(numeral)

    return being_sorted
    ```

5. Iterating, 나머지 자리수에 있는 숫자들도 정렬을 해준다.

    ```py
    def radix_sort(to_be_sorted):
        maximum_value = max(to_be_sorted)
        max_exponent = len(str(maximum_value))
        being_sorted = to_be_sorted[:]

        # 모든 자리수를 도는 반복문 생성
        for exponent in range(max_exponent):
            digits = [[] for i in range(10)]

            # 몇번째 자리수를 확인하고 있는지
            position = exponent + 1
            # 뒤에서부터 거꾸로 세야하니깐 음수로 변환
            index = -position

            for number in being_sorted:
                number_as_a_string = str(number)
                # position이 1이라면 -1, 2라면 -2, 3이라면 -3
                # position이 1이라면 1의자리, 2라면 10의자리 ...
                digit = number_as_a_string[index]
                digit = int(digit)

                digits[digit].append(number)

            being_sorted = []

            for numeral in digits:
                being_sorted.extend(numeral)

        return being_sorted
    ```

6. Bug Fix, 지금 상태로는 IndexError가 발생한다. 몇몇 숫자가 다른 숫자들보다 길이가 짧아 나타나는 현상이다. try/except 키워드를 이용해서 수정해주자.

    ```py
    try:
        digit = number_as_a_string[index]
        digit = int(digit)
    except IndexError:
        digit = 0
    ```
