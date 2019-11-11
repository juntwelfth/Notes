# What is Bubble Sort

버블정렬은 인접한 항목끼리 반복적으로 비교를하여 정렬하는 기법이다.

![bubble](https://s3.amazonaws.com/codecademy-content/courses/sorting/BubbleSort.gif)

첫번째 요소가 두번째 요소보다 크기가 크면 두 요소의 위치를 바꾸는식이고, 이렇게 바뀌게되면 list가 정렬되어있지 않다는것을 의미하므로 전체 반복문이 한번 더 반복된다.

## Bubble Sort

이 알고리즘이 어떻게 두 요소를 교체하는 것일까? `index_1`과 `index_2`라는 값을 가지고 있다고 가정해보자.

```py
list[index_1] = list[index_2]
list[index_2] = list[index_1]
```

이런식으로 이루어지게 되는데, 이 경우엔 `index_`의 값을 잃어버리게된다. 따라서 임시 변수를 하나 만들고 값을 바꿔주면 된다.

```py
temp = list[index_1]
list[index_1] = list[index_2]
list[index_2] = temp
```

![gif](https://s3.amazonaws.com/codecademy-content/courses/sorting/swap.gif)

또다른 방법으로는 아래와같은 방법이 가능하다.

```py
a = 1
b = 5

a, b = b, a
```

## Algorithm Analysis

정렬되지않은 데이터셋이 주어지면, 버블정렬은 정렬된 list를 만들기까지 여러번의 반복을 행해야한다.

Inner loop로 `n-1`번 비교를한다. 그 다음 list의 요소들이 제대로 정렬되었는지 확인하기 위해 전체 list를 `n`번 살펴봐야한다.

Worst case에선 inner loop이 list 각각의 요소 `n`에 대해 `n-`번 비교한다. 따라서 알고리즘의 효율은 아래와같다.

$$O(n(n-1))=O(n(n))=O(n^2)$$

알고리즘의 run-time 효율을 계산할 때 `-1`은 제거하고 단순히 `n`만 남긴다. 따라서 `O(n²)`가 된다.

![bubble](https://s3.amazonaws.com/codecademy-content/courses/sorting/Sorting+Course+Efficiency+Diagram+1.svg)

> 버블정렬은 기존 list 혹은 배열을 수정시킨다.

버블정렬을 한번 수행하고나면 목록의 마지막값이 올바른 위치에 있다는 것을 알고 있다. 따라서 더이상 고려하지 않아도된다. 두번째 단계에선 `n-2`번만 비교하면 된다.

더 많은 요소를 정렬을하면 더 적은 반복을 하게된다. 이러한 정렬은 더이상 `n²-n`번을 비교하지 않고 `(n-1) + (n-2) + ... + 2 + 1`번을 비교하게 된다. 간단히 말하면 `(n²-n) / 2`이다.

`n²-n`번을 비교하게 되므로 더 적은 숫자이지만 시간복잡도는 여전히 `O(N²)`가된다.

## 순서

1. 먼저 스왑해주는 함수를 작성해준다.

    ```py
    # 스왑해주는 함수
    def swap(arr, index_1, index_2):
        temp = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = temp
    ```

2. 스왑이 필요한지 확인하는 루프를 설정해준다.
   먼저 list 요소 전체를 iterate하는 반복문을 설정하고, 각각의 요소들끼리 비교를하는 내부반복문을 하나 더 만들어준다.

    ```py
    def bubble_sort(arr):
        for el in arr:
            for index in range(len(arr)-1):
                if arr[index] > arr[index + 1]:
                    swap(arr, index, index+1)
    ```

## Examples

### Python

```py
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))
# PRE SORT: [9, 8, 7, 6, 5, 4, 3, 2, 1]


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    # 총 반복횟수 72번 (n² - n)번
    iteration_count = 0
    for el in arr:
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)


def bubble_sort(arr):
    # 총 반복횟수 36번 (n² - n) / 2번
    iteration_count = 0
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                swap(arr, idx, idx + 1)
```
