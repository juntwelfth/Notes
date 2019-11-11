# Strings


def replace_words():  # | 특정 문자열 다른걸로 바꾸기
    'aaabbbddd'.replace('d', 'c')
    #: 모든 d들이 c로 바뀜

    'aaabbbddd'.translate(str.maketrans("d", "c"))
    #: 모든 d들이 c로 바뀜


def reverse_string():  # | 스트링 뒤집기
    a = 'abc'
    a[::-1]
    #: 'cba'


def unicode_or_ascii():  # | 아스키코드, 유니코드
    print(ord('a'))
    #: 97
    print(ord('A'))
    #: 65


#! 재귀함수
def is_palindrome(string):  # | palindrome인지 체크
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


def is_palindrome(string):  # | palindrome인지 체크
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        string = string[1:-1]
    return True
