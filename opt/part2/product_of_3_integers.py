import io
import sys

#入力データ
_INPUT = """\
2 8 8
"""
sys.stdin = io.StringIO(_INPUT)
#ここから提出コード

test = 1
out = [int(i) for i in input().split(" ")]

for i in out:
    test*=i



print(test)
