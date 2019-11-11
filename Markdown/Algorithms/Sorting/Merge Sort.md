# Merge Sort란

1945년 John von Neumann이 만든 정렬 알고리즘이다. 병합정렬의 "killer app"은 *divide-and-conquer* 알고리즘이라고도 불리우는 정렬할 list를 더 작은 부분으로 나누는 전략이다.

divide-and-conquer 알고리즘에서 데이터는 정렬이 간단해질때까지 계속해서 작은 부분으로 나눠진다.

![merge](https://s3.amazonaws.com/codecademy-content/courses/merge-sort/merge_ex_3.svg)

## How To Merge Sort

- 병합정렬엔 두 단계가 있다.
  1. 데이터를 "실행"또는 더 작은 구성 요소로 분할한다.
  2. 이렇게 분할된 데이터를 다시 정렬된 목록으로 결합한다. (merge)

데이터를 나눌 때 입력을 반으로 나눈다. 그런 다음 각각 재귀를 이용하여 또 반으로 나눈다. 이 과정은 모든 list들이 한개의 요소만 가지고있을 때 까지 반복한다. 그런 후 병합을 시작한다.

요소를 하나만 가지고있는 두개의 list를 병합할 때 첫번째 요소가 더 작은지 큰지 확인한다. 그 다음 작은요소 다음에 큰 요소가 오는 두개의 요소를 가진 list를 반환한다.

![merge](https://s3.amazonaws.com/codecademy-content/courses/merge-sort/merge_ex_1.svg)

## Merge Sort Performance

병합정렬은 best, worst, average 시간 복잡도가 전부 `Θ(N*log(N))`로 같다. 이는 거의 완벽하게 정렬된 list나 완전히 정렬이 되지않은 list나 동일한시간이 걸린다는 것을 의미한다.

병합정렬은 공간이 필요하다. 각각의 list가 각각의 임시저장 배열이 필요하기 때문에 병합 정렬에는 전체 입력을 두번째로 저장할만큼 충분한 공간이 필요하다.

## 순서

1. 정렬하려는 list의 길이가 1 혹은 그 이하일 때 그 list를 그대로 반환 (정렬할 필요가 없으니깐)

    ```py
    if len(lst) <= 1:
        return lst
    ```

2. list를 절반으로 나누기

    ```py
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    ```

3. merge해주는 함수 작성하기

    ```py
    def merge(left, right):
        result = []

        # left, right 둘 다 빈 list가 아닐 때
        while (left and right):
            if left[0] < right[0]:
                # 둘중에 더 큰 수를 result에 추가
                result.append(left[0])
                # 방금 추가시킨 요소를 삭제
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        # 만약 left가 빈 list가 아니라면 result에 이어붙이기
        if left:
            result += left
        if right:
            result += right

        return result
    ```

4. sort하기

    ```py
    def merge_sort(items):
        if len(items) <= 1:
            return items

        middle_index = len(items) // 2
        # 양쪽으로 반띵해서 나누기
        left_split = items[:middle_index]
        right_split = items[middle_index:]

        # 반띵해서 나눈것을 재귀함수를 이용해서 각각 한개만 가질 때 까지 계속 반띵하기
        left_sorted = merge_sort(left_split)
        right_sorted = merge_sort(right_split)

        # 서로 한개씩 가지게되면 merge함수 호출하기
        return merge(left_sorted, right_sorted)


    def merge(left, right):
        result = []

        while (left and right):
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        if left:
            result += left
        if right:
            result += right

        return result
    ```
