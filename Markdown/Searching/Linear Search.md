# Linear Search

## Finding Elements in Lists

첫번째 요소부터 마지막 요소까지 검색하는 방법. 원하는 요소를 찾으면 검색을 중단한다.

- Steps:
  1. 목록의 첫번째 요소를 검사한다.
  2. 만약 첫번째 요소가 검사하려는 타겟과 같다면 멈춘다.
  3. 첫번째 요소가 타겟과 같지않다면 다음 요소와 비교한다.
  4. 타겟과 같은 요소를 찾을때까지 1-3 과정을 반복한다.

![linear](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/linear-search-demo-1.gif)

## Best Case Performance

Linear search방법은 대규모 list의 경우 효율적인 검색방법이 아니다.

가장 최고의 결과는 타겟이 0번째 인덱스에 있을 경우다. 이 경우엔 알고리즘이 딱 한번만 비교하면 되고 시간복잡도는 O(1)이다.

## Worst Case Performance

두 종류의 최악의 상황이있다.

1. 타겟이 list의 맨 마지막에 있을 때
![worst1](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/worst+case.png)

2. 타겟이 list에 존재하지 않을 때
![worst2](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/worst+case+2.png)

위 두가지의 경우 알고리즘은 전체 N개의 요소를 N번 비교해야한다. 따라서 시간복잡도는 O(N)이된다.

![worst](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/vinyl_crate.svg)

## Average Case Performance

만약 이 알고리즘을 가지고 1000번을 1000개의 다른 list에 적용했다면 몇개는 best case, 몇개는 worst case 그리고 대부분은 그 중간이 될 것이다.

linear search 알고리즘이 평균적으로 list의 절반을 검색할것으로 예상된다. 따라서 평균적인 경우 linear search의 시간 복잡도는 `O(N/2)`이다. (Bio O 단순화 규칙을 기반으로 `O(N)`으로 단순화 가능)

![number of comparisons](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/comparisons.svg)

## Time Complexity

선형검색은 list의 크기가 증가함에 따라 시간도 늘어나고, Big-O 표기법에서 선형검색의 시간 복잡도는 O(N)이 된다.

O(N)의 시간 복잡도는 list의 요소개수 N에 비례한다. 요소가 두배로 늘어나면 선형검색은 검색을 수행하는데 최대 두배가 걸리게된다.

![linear](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/linear+search+graph+(1).svg)

## Examples

- Python

    ```py
    lst = [1, 3, 5, 7, 9]
    target = 7


    for i in range(len(lst)):
        if not target in lst:
            print("target is not in list")
            break
        if lst[i] == target:
            print(i)
            break
    raise ValueError(
        "{0} not in list".format(value))
    ```
