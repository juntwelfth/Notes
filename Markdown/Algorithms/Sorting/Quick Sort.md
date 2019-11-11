# Quick Sort

Quicksort는 배열 또는 list를 정렬하기 위한 효율적인 recursive algorithm이다. 이 알고리즘은 비교정렬이며, 여기서 값은 `>`, `<`와 같은 비교연산으로 정렬된다.

Quicksort 또한 *divide and conquer* 전략을 사용하며, 해답이 명확해져서 더이상 해결할 것이 없을 때 까지 문제들을 작은 문제들로 쪼개는 방식이다.

문제: 배열의 값들이 정렬되어있지 않다.

해결: 배열을 하나의 요소만 가질때까지 쪼개준다.

list에서 *pivot*요소 하나를 선택한다. 다른 모든 요소들은 이 pivot요소와 비교할 것이고 다른 모든 요소는 세 그룹으로 나뉘어진다.

1. pivot보다 **더 작은** 요소들을 담은 sub-array
2. pivot
3. pivot보다 **더 큰** 요소들을 담은 sub-array

이 과정은 각각의 sub-array들의 요소가 1개 혹은 0개가 될 때까지 반복한다. 더 작은 요소들을 모아놓은 sub-array는 **결코** 더 큰 요소들을 모아놓은 sub-array와 비교되지 않는다.

```py
[6,5,2,1,9,3,8,7]

6 # The pivot
[5, 2, 1, 3] # lesser than 6
[9, 8, 7] # greater than 6


[5, 2, 1, 3]
# 이 두 list들은 서로 비교되지 않는다. 절대로.
[9, 8, 7]
```

![quick](https://s3.amazonaws.com/codecademy-content/programs/cs-path/quicksort-conceptual/quicksort.svg)

## Quicksort Runtime

Quicksort의 런타임 효율성의 핵심은 배열을 나누는것이다. 배열은 우리가 선택한 pivot 요소에 따라 나뉘는데 어떤 pivot을 선택해야 sub-array들을 비슷한 길이로 나눌 수 있을까?

대부분의 경우 항상 첫번재 요소를 pivot으로 사용한다. best case는 배열이 정렬되어있을 경우고 worst case는 정렬된 배열에서 첫번째 요소를 선택하는데 계속 가장 큰 요소 혹은 가장 작은 요소가 선택될때이다.

유명한 전략중 하나는 각각의 나누는 과정에서 pivot을 랜덤으로 설정하는 것이다.

또 다른 유명한 전략으로는 배열의 첫번째, 중간, 마지막 요소를 가져와서 중간값 요소를 pivot으로 선택하는것이다.

worst case에서 시간복잡도는 `O(N²)`이지만 평균 시간복잡도는 `O(N * logN)`이다.

보통 알고리즘의 런타임(시간복잡도)에 대해 이야기할 때 worst case만 이야기하지만 Quicksort는 평균을 가지고 얘기한다.

## 순서

1. pivot 고르기

    ```py
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]

    # 교체하기
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    ```

2. 파티션 나누기

    ```py
    [5, 6, 2, 3, 1, 4]
    # 랜덤으로 3을 뽑았고 마지막 요소 4와 자리를 바꿔준다.
    [5, 6, 2, 4, 1, 3]

    # We'll use () to mark our "lesser than" pointer
    # We'll use {} to mark our progress through the list
    # () : "lesser than" 포인터
    # {} : 진행상황

    [{(5)}, 6, 2, 4, 1, 3]
    # {5} 는 3보다 작지 않으므로 "lesser than" 포인터는 그대로

    [(5), {6}, 2, 4, 1, 3]
    # {6} 은 3보다 작지 않으므로 "lesser than" 포인터는 그대로

    [(5), 6, {2}, 4, 1, 3]
    # {2} 는 3보다 작으므로 5와 값을 바꿔준다.
    [(2), 6, {5}, 4, 1, 3]
    # 그런 다음 "lesser than" 포인터를 증가시켜준다.
    [2, (6), {5}, 4, 1, 3]

    [2, (6), 5, {4}, 1, 3]
    # {4} 는 3보다 작지 않으므로 "lesser than" 포인터는 그대로

    [2, (6), 5, 4, {1}, 3]
    # {1} 은 3보다 작으므로 교체해준다.
    [2, (1), 5, 4, {6}, 3]
    # "lesser than" 포인터를 증가시켜준다.
    [2, 1, (5), 4, {6}, 3]

    # pivot을 제외한 요소중 마지막에 도달했다.
    [2, 1, (5), 4, 6, {3}]
    # "lesser than" 포인터와 pivot을 교체해준다.
    [2, 1, (3), 4, 6, {5}]
    ```

3. Recurse, Rinse and Repeat

    ```py
    # pivot 3
    whole_list = [2, 1, (3), 4, 6, 5]

    less_than_pointer = 2
    start = 0
    end = len(whole_list) - 1

    # "lesser than" 그룹을 위한 포인터들
    left_sub_list_start = start
    left_sub_list_end = less_than_pointer - 1

    # "lesser than" 그룹
    lesser_than_sub_list =
        whole_list[left_sub_list_start : left_sub_list_end]
    # [2, 1]

    # "greater than" 그룹을 위한 포인터들
    right_sub_list_start = less_than_pointer + 1
    right_sub_list_end = end

    # "greater than" 그룹
    greater_than_sub_list =
        whole_list[right_sub_list_start : right_sub_list_end]
    # [4, 6, 5]
    ```
