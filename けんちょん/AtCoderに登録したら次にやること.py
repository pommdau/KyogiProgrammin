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
from itertools import combinations


def solve():
    number_of_rows, number_of_columns = list(map(int, input().split()))
    field = []
    for _ in range(number_of_rows):
        line = []
        for char in input():
            line.append(char)
        field.append(line)
    t = input()
    length_of_t = len(t)

    count = 0
    for row_i in range(number_of_rows):
        for column_i in range(number_of_columns):
            created_word = field[row_i][column_i]

            # 右に移動可能な場合
            if column_i < number_of_columns - 1:
                created_word += field[row_i][column_i + 1]
                # 下に移動可能な場合
                if row_i < number_of_rows - 1:
                    created_word += field[row_i + 1][column_i + 1]
            else:
                # 下に移動可能な場合
                if row_i < number_of_rows - 1:
                    created_word += field[row_i + 1][column_i]

            if created_word == t:
                count += 1
    
    print(count)


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
