# -*- coding: utf-8 -*-
import sys
import os

# solveの中に記述，提出時はsolve()のコメントアウトを外して
# ここから

# https://teru0rc4.hatenablog.com/entry/2017/05/15/003532
# # 数値
# s = input().split()
# a, b, c = input().split()

# 入力が1行で複数ある場合
# n = list(map(int, input().split()))  # 整数
# n = list(map(float, input().split()))  # 浮動小数点数
# n1, n2, n3 = list(map(int, input().split()))  # 整数
# n1, n2, n3 = list(map(float, input().split()))  # 浮動小数点数

from typing import List, Dict
import math
from itertools import product  # bit全探索


def solve():
    number_of_rods = int(input())
    rods = list(map(int, input().split()))
    rods_dict = {i: 0 for i in range(51)}

    for rod in rods:
        rods_dict[rod] += 1

    can_create_rectangle = False
    for rods_count in rods_dict.values():
        if rods_count >= 4:
            can_create_rectangle = True

    if can_create_rectangle:
        print("YES")
    else:
        print("NO")

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
