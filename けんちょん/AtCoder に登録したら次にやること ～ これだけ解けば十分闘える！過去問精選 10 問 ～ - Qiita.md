# [AtCoder に登録したら次にやること ～ これだけ解けば十分闘える！過去問精選 10 問 ～ \- Qiita](https://qiita.com/drken/items/fd4e5e3630d0f5859067#%E7%AC%AC-10-%E5%95%8F--abc-086-c---traveling-300-%E7%82%B9)

# 参考

- [AtCoder に登録したら解くべき精選過去問 10 問 をPythonで解いてみた \- やるだけPython競プロ日誌](http://delta114514.hatenablog.jp/entry/2018/03/15/014555)
- [AtCoder に登録したら解くべき精選過去問 10 問をPython3で解いてみた](https://qiita.com/edad811/items/f72acb09f06e5fb35e4e)

## 0問目 PracticeA - はじめてのあっとこーだー（Welcome to AtCoder）

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    a = int(input())
    b, c = list(map(int, input().split()))
    s = input()
    print(a+b+c, s)
# solve()
##### ここまで


# テストケース実行部分
test_path = 'test_case'
FILES = os.listdir(test_path)
print('test case => %s\n/Users/ikeuchihiroki/PycharmProjects/Kyopro/test_case' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    print("\ncase : %s" % FILE)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("\n**********\nfinish")
```

- 提出するときはこれだけ抜き出す。

``` Python
def solve():
    a = int(input())
    b, c = list(map(int, input().split()))
    s = input()
    print(a+b+c, s)
solve()
```

## 1問目 ABC086A - Product

``` Python
def solve():
    number1, number2 = list(map(int, input().split()))
    odd = number1 * number2
    if odd % 2 == 0:
        print("Even")
    else:
        print("Odd")
# solve()
```

## 2問目 ABC081A - Placing Marbles

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    s = input()
    print(s.count('1'))
# solve()
##### ここまで
```

```python
def solve():
    s: str = input()
    count: int = 0
    for number_str in s:
        if int(number_str) == 1:
            count += 1

    print(count)

# solve()
```

## 3問目 ABC081B - Shift only

- [Pythonの組み込み関数all\(\), any\(\)の使い方 \| note\.nkmk\.me](https://note.nkmk.me/python-all-any-usage/)

> すべての要素がTrueか判定: all()
> all()は引数に指定したイテラブルオブジェクトの要素がすべてTrueと判定されるとTrueを返す。一つでもFalseがあればFalse。
> ``` Python
> print(all([True, True, True]))
> # True
> print(all([True, False, True]))
> # False
> ```

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while all(a%2==0 for a in A):
        A = [a/2 for a in A]
        cnt += 1
    print(cnt)

# solve()
##### ここまで


# テストケース実行部分
test_path = 'test_case'
FILES = os.listdir(test_path)
print('test case => %s\n/Users/ikeuchihiroki/PycharmProjects/Kyopro/test_case' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    print("\ncase : %s" % FILE)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("\n**********\nfinish")
```

## 4問目 ABC087B - Coins

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    A, B, C, X = [int(input()) for _ in range(4)]
    ans = 0
    for a_i in range(A+1):
        for b_i in range(B+1):
            for c_i in range(C+1):
                sum = 500 * a_i + 100 * b_i + 50 * c_i
                if (sum == X):
                    ans += 1
    print(ans)

# solve()
##### ここまで


# テストケース実行部分
test_path = 'test_case'
FILES = os.listdir(test_path)
print('test case => %s\n/Users/ikeuchihiroki/PycharmProjects/Kyopro/test_case' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    print("\ncase : %s" % FILE)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("\n**********\nfinish")
```

## 5問目 ABC083B - Some Sums

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    N, A, B = list(map(int, input().split()))

    res = 0
    for i in range(N+1):
        if A <= sum([int(s) for s in str(i)]) <= B:
            res += i

    print(res)

# solve()
##### ここまで


# テストケース実行部分
test_path = 'test_case'
FILES = os.listdir(test_path)
print('test case => %s\n/Users/ikeuchihiroki/PycharmProjects/Kyopro/test_case' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    print("\ncase : %s" % FILE)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("\n**********\nfinish")
```

## 第6問 ABC 088 B - Card Game for Two

- [Pythonでリストをソートするsortとsortedの違い \| note\.nkmk\.me](https://note.nkmk.me/python-list-sort-sorted/)
    - `sort()`はもとの配列自体をソートする。
- [【Python】スライス操作についてまとめ](https://qiita.com/tanuk1647/items/276d2be36f5abb8ea52e)

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### ここから
def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)    #  降順で整列

    score_of_Alice = sum(a[0::2])
    score_of_Bob = sum(a[1::2])

    print(score_of_Alice - score_of_Bob)
```

## 第7問 ABC 085 B - Kagami Mochi

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    N = int(input())
    d = [int(input()) for _ in range(N)]
    s = set(d)

    print(len(s))

# solve()
##### ここまで
```

## 第8問 ABC 085 C - Otoshidama

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    N, Y = list(map(int, input().split()))
    for i in range(N + 1):
        for j in range(N + 1 - i):
            if i * 10000 + j * 5000 + (N - i - j) * 1000 == Y:
                print(i, j, N - i - j)
                exit()
    print("-1, -1, -1")

# solve()
##### ここまで
```

## 9問目 ABC049C - 白昼夢 / Daydream

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    S = input()
    S = S.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
    if S:
        print("NO")
    else:
        print("YES")

# solve()
##### ここまで
```

``` Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    S = input()
    given = ["dreamer", "dream", "eraser", "erase"]
    while len(S) > 0:
        judge = [S.endswith(i) for i in given]
        if any(judge):
            target = given[judge.index(True)]
            S = S[:-len(target)]
            if len(S) == 0:
                print("YES")
                break
        else:
            print("NO")
            break

# solve()
##### ここまで
```

## 10問目 ABC086C - Traveling