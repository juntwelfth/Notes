def binary_search_recursively(lst, target):
    # 먼저 lst 정렬
    lst.sort()

    if not lst:  #: lst가 빈 list라면
        return "value not found"

    # 중간값과 중간 idx
    mid_idx = int(len(lst)/2)
    mid_val = lst[mid_idx]

    if target == mid_val:
        return mid_idx

    elif target < mid_val:
        left_half = lst[:mid_idx]
        return binary_search(left_half, target)

    elif target > mid_val:
        right_half = lst[mid_idx + 1:]
        result = binary_search(right_half, target)

        if result == "value not found":
            return result

        return result + mid_idx + 1
        # ? result + mid_idx + 1 하는 이유는?
        # ? 원래 오리지널 list에서의 index값을 반환해야하니깐


print(binary_search_recursively([], 1))


def binary_search_iteratively(lst, target):
    lst.sort()

    left_pointer = 0
    right_pointer = len(lst)

    while left_pointer < right_pointer:
        mid_idx = (left_pointer + right_pointer) // 2
        mid_val = lst[mid_idx]

        if target == mid_val:
            return mid_idx

        elif target < mid_val:
            right_pointer = mid_idx

        elif target > mid_val:
            left_pointer = mid_idx + 1

    return "Value not in list"


print(binary_search_iteratively([2, 7, 8, 5, 3], 5))
