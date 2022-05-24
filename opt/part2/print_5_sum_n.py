import io
import sys

#入力データ
_INPUT = """\
8
"""
sys.stdin = io.StringIO(_INPUT)


#ここからコーディング
print(int(input()) + 5)