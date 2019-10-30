def accum(str):
    li = list(str)
    result = []
    for i in range(len(li)):
        temp_str = ""
        temp_str += li[i].upper()

        for j in range(i):
            temp_str += li[i].lower()
        result.append(temp_str)
    return '-'.join(result)


a = accum("abcd")  # : "A-Bb-Ccc-Dddd"
b = accum("RqaEzty")  # : "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
c = accum("cwAt")  # : "C-Ww-Aaa-Tttt"
