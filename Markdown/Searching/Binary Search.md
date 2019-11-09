# Binary Search

정렬된 데이터셋을 사용하면 더 효율적인 방법으로 검색을 할 수 있다.

사전에서 "Telescope"라는 단어를 찾고있다고 해보자. "A"부터 "B"까지 한장한장 넘기면서 찾지않고 "T"가 나올 때 까지 넘길것이다.

책을 확 펼쳤는데 "R"이 나왔고 다시 뒤로 확 넘겼는데 "V"가 나왔다면 다시 앞으로 조금 넘겨서 "T"를 찾을것이다.

위 과정에서 binary search를 수행한 것이다.

- Steps:
    1. 데이터셋에서 가운데값을 확인한다.
       - 만약 타겟과 일치하면 그대로 반환한다.
    2. 가운데값이 타겟보다 더 작다면
       - 오른쪽 나머지 list에 대해 1번을 수행한다.
    3. 가운데값이 타겟보다 더 크다면
       - 왼쪽 나머지 list에 대해 1번을 수행한다.

![binary](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/binarySearch.gif)

## Time Complexity

각 반복에서 list를 반으로 나눈다. 시간복잡도는 `O(log N)`이다.

정렬된 64개 요소를 포함한 list는 최대 `log` `2` `(64) = 6` 비교를 수행한다.

- Worst case:
    1. `64`개의 요소중 가운데 값을 찾는다.
    2. 타겟과 일치하지 않는다면 `32`개의 요소중에서 찾는다.
    3. 일치하지 않는다면 `16`개의 요소중에서 찾는다.
    4. ...`8`개...
    5. ...`4`개...
    6. ...`2`개...

`64` 사이즈 list에선 `6`번의 비교를 수행한다.

![binary2](https://s3.amazonaws.com/codecademy-content/courses/search-course/visualizations/binaryComplexity.png)

> Binary Search는 항상 꼭 정렬된 list에서만 가능!
> > Binary Search를 수행할 땐 Recursion(재귀)를 이용하자.
> > > 오른쪽 slice에서 찾아내서 index를 반환할 땐 꼭 왼쪽 잘려나간 slice + 1을 더해주기.

```py
sorted_list = [7, 8, 9, 10, 11]
binary_search(sorted_list, 11)
mid_idx = 2
# 9 < 11, 오른쪽 slice를 비교할차례
# right_half = [10, 11]
# mid_idx = 1
# 오른쪽 slice에서 1번째 인덱스가 정답.
# 하지만 원래 오리지널 list에선 1번째 인덱스가 아니고
# mid_idx + 1 + 오른쪽slice에서의 인덱스
(result + mid_idx + 1) == 4
```

## Examples

- Python

   ```py
   lst = [2, 4, 6, 8, 10]
   target = 8

   left_pointer = 0
   right_pointer = len(lst)

   while left_pointer < right_pointer:
      mid_idx = (left_pointer + right_pointer) // 2
      mid_val = lst[mid_idx]

      if not target in lst:
         print("Value not in list)

      if target == mid_val:
         print(mid_idx)
         break

      elif target < mid_val:
         right_pointer = mid_idx

      elif target > mid_val:
         left_pointer = mid_idx + 1
   ```
