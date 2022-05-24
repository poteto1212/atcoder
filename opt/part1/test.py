import io
import sys

#入力データ
_INPUT = """\
100,5,12,3,9,13,11,10,8,7,2100
"""
sys.stdin = io.StringIO(_INPUT)

test_array = [int(i) for i in input().split(",") ]
test_list=[None]*len(test_array)
i = 0
while i < len(test_array):
    j = i + 1
    min = i
    while j < len(test_array):
        if test_array[min] > test_array[j]:
            min = j
        j += 1

    tmp = test_array[i]
    test_array[i] = test_array[min]
    test_array[min] = tmp
    i += 1
print(test_array)