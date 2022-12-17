# -*- coding: utf-8 -*-
import sys
import os
from typing import List, Dict
import math

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


def solve():
    n = int(input())
    plans = []
    for _ in range(n):
        plans.append(list(map(int, input().split())))

    last_t, last_x, last_y = 0, 0, 0
    for current_t, current_x, current_y in plans:
        # 進んだ値
        diff_t = current_t - last_t
        diff_x = abs(current_x - last_x)  # 絶対値に注意
        diff_y = abs(current_y - last_y)

        # tとx+yの偶数奇数は一致
        # 1秒間に進めるのは1のみ(diff_t秒間に進めるのはdiff_t以下)
        if current_t % 2 == (current_x + current_y) % 2 and diff_t >= diff_x + diff_y:
            last_t = current_t
            last_x = current_x
            last_y = current_y
        else:
            print("No")
            return
    print("Yes")

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
