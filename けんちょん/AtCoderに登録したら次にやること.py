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
    number_of_rows, number_of_columns = list(map(int, input().split()))
    field: List[str] = []
    for _ in range(number_of_rows):
        field.append(list(input()))

    for row_i in range(number_of_rows):
        for column_i in range(number_of_columns):
            if field[row_i][column_i] == "#":
                continue
            
            # 上下左右8マスの確認
            number_of_bombs = 0
            diff_list = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            for diff in diff_list:
                target_row = row_i + diff[1]
                target_column = column_i + diff[0]
                if target_row < 0 or target_row > number_of_rows - 1:
                    continue
                if target_column < 0 or target_column > number_of_columns - 1:
                    continue
                if field[target_row][target_column] == "#":
                    number_of_bombs += 1
            field[row_i][column_i] = number_of_bombs

    for row_i in range(number_of_rows):
        for column_i in range(number_of_columns):
            print(field[row_i][column_i], end="")
        print("")

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
