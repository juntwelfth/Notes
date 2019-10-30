# Lists


def copy_list():  # | List 복사
    original = [1, 2, 3, 4, 5]

    # 1
    copy_1 = list(original)
    copy_1.pop()

    print(original)  # * 안변했음
    #: [1, 2, 3, 4, 5]

    # 2
    copy_2 = original[:]
    copy_2.pop()

    print(original)  # * 안변했음
    #: [1, 2, 3, 4, 5]


def change_elements_from_list():  # | List Element 속성 바꾸기
    li = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

    # li를 split해서 리스트로 만든 후 요소들을 int로 바꾸기
    li_int = list(map(int, li.split(' ')))

    # li_int의 내용물을 string으로 바꾸기
    li_str = list(map(str, li_int))


def delete_element_from_list():  # | List Element 제거하기
    li = [1, 2, 3, 4, 5]

    li.pop(2)     # * delete by index
    del(li[0])    # * delete by index

    li.remove(4)  # * delete by value


def int_list_join(arr):  # | int형 List join 메소드
    ''.join(map(str, arr))
