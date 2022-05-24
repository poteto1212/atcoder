import io
import sys

#入力データ
_INPUT = """\
1 2 3 5
"""

sys.stdin = io.StringIO(_INPUT)
number = [int(i) for i in input().split(" ")]
length = len(number)
i = 0
sum = 1
while i < length//2:
    sum = sum*number[i]*number[length-i - 1]
    i += 1
#奇数の時は中央値を加算する
is_odd = length%2 
if is_odd == 1:
    sum = sum*number[i]

print(sum)