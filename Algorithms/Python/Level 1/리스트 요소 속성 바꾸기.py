li = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

#: li를 split해서 리스트로 만든 후 요소들을 int로 바꾸기
li_int = list(map(int, li.split(' ')))
print(li_int)

#: li_int의 내용물을 string으로 바꾸기
li_str = list(map(str, li_int))
print(li_str)
