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
