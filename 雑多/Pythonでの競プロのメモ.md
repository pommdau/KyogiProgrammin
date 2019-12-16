# Pythonで競プロ

## 2次元配列の宣言

[Pythonで2次元配列の静的確保と動的確保](http://sonickun.hatenablog.com/category/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0?page=1402667101)

> 2次元配列の静的確保
>``` Python
>>>> arr = [[0 for i in range(3)] for j in range(5)]
>>>> arr
>[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>```

## 二次元配列を要素の2番目の値でソートする

- [はらへり日記 \- Pythonで二次元配列をsortする](http://sota1235.com/blog/2015/04/23/python_sort_twodime.html)

``` Python
from operator import itemgetter

my_list = [[2, 30], [4, 10], [1, 50], [3, 20]] # [[2, 30], [4, 10], [1, 50], [3, 20]]
my_list.sort(key=itemgetter(1))                # [[4, 10], [3, 20], [2, 30], [1, 50]]

## 複数行複数列の入力の読み込み
```

```Python
3
1 1
2 4
4 3
```

### 1案

``` Python
N = int(input())
X = [0]*N
Y = [0]*N
for i in range(N):
    x, y = list(map(int, input().split()))
    X[i], Y[i] = x, y
```

### 2案

- 扱いにくい？

``` Python
N = int(input())
points = [list(map(int, (input().split()))) for _ in range(N)]
```

## 平方根の求め方
- 下記の通りべき乗で表現できる

``` Python
print(5**0.5)
```

- `math`を使う必要もない

``` Python
import math
print(math.sqrt(5))
```

## 参考

- [Python3での競技プログラミング用標準入力個人的まとめ](http://teru0rc4.hatenablog.com/entry/2017/05/15/003532)
- [pythonの内包表記を少し詳しく](https://qiita.com/y__sama/items/a2c458de97c4aa5a98e7)
- [Python 競技プログラミング高速化tips \(PythonでAtcoderをやる際に個人的に気を付けてること\) \- じゅっぴーダイアリー](https://juppy.hatenablog.com/entry/2019/06/14/Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E9%AB%98%E9%80%9F%E5%8C%96tips_%28Python%E3%81%A7Atcoder%E3%82%92%E3%82%84%E3%82%8B%E9%9A%9B%E3%81%AB%E5%80%8B#%E3%81%BF%E3%82%93%E3%81%AA%E4%B8%80%E5%BA%A6%E3%81%AF%E9%80%9A%E3%82%8B%E9%81%93)
- [PythonでAtCoder青になるまで \-Pythonで競プロやるときに気をつけること\- \- Qiita](https://qiita.com/Kentaro_okumura/items/a6917572756a2e3c0da9)
- [Pythonで使う競技プログラミング用チートシート](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)
- [Pythonで競プロやるときによく書くコードをまとめてみた \- Qiita](https://qiita.com/y-tsutsu/items/aa7e8e809d6ac167d6a1)
- [Python3基礎文法](https://qiita.com/Fendo181/items/a934e4f94021115efb2e)

![-w917](https://i.imgur.com/5YVBQof.jpg)

```Python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に記述，提出時はsolve()のコメントアウトを外して
##### ここから
def solve():
    a, b, c = list(map(int, input().split()))
    if a <= c and c <= b :
        print("Yes")
    else:
        print("No")
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
