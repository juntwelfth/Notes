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
