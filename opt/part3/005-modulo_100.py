import io
import sys

#入力データ
_INPUT = """\
3
30 50 70
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input()) - 1
a_s = [int(i) for i in input().split(" ")]

out = 0
while N >= 0:
    out+=a_s[N]
    N -= 1

print(out % 100)