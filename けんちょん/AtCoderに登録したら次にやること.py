# -*- coding: utf-8 -*-
import sys
import os

# solveの中に記述，提出時はsolve()のコメントアウトを外して
# ここから


def solve():
    s: str = input()
    print(s.count('1'))

# solve()
# ここまで


test_path = 'test_case'
FILES = os.listdir(test_path)
print('test case => %s\n**********' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    print("\ncase : %s" % FILE)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("\n**********\nfinish")
