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
from itertools import permutations

def solve():
    number_of_words = int(input())
    words = []
    for _ in range(number_of_words):
        words.append(input())
    
    coined_words = []
    for first_word, second_word in permutations(words, 2):
        first_word_suffix = first_word[-2:]
        second_word_suffix = second_word[:2]
        if first_word_suffix == second_word_suffix:
            coined_word = first_word + second_word[2:]
            coined_words.append(coined_word)
    if len(coined_words) == 0:
        print(-1)
    else:
        print(max([len(coined_word) for coined_word in coined_words]))

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
