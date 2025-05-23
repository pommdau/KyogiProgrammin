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
- [B \- Shift only 解説](https://atcoder.jp/contests/abc081/tasks/abc081_b)
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
```

```python
def solve():
    n: int = int(input())
    a_list: List[int] = list(map(int, input().split()))
    counter: int = 0
    while True:
        can_deviding = True
        for a_n in a_list:
            if a_n % 2 != 0:
                can_deviding = False
                break
        if not can_deviding:
            break

        counter += 1
        a_list = [a_n / 2 for a_n in a_list]

    print(counter)
```

## 4問目 ABC087B - Coins
[B \- Coins 解説](https://atcoder.jp/contests/abc087/tasks/abc087_b)

``` Python
def solve():
    a, b, c, x = [int(input()) for i in range(4)]
    count = 0
    for a_i in range(a + 1):
        for b_i in range(b + 1):
            for c_i in range(c + 1):
                sum = a_i * 500 + b_i * 100 + c_i * 50
                if sum == x:
                    count += 1
    print(count)

# solve()
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
```

```python
def get_sum_of_digit(number: int) -> int:
    sum = 0
    while(number > 0):
        sum += number % 10
        number = int(number / 10)  # キャストをしないとFloatがでてきてしまうので注意. math.floor()を使ってもいいか

    return sum


def solve():
    n, a, b = list(map(int, input().split()))
    count = 0
    for n_i in range(n + 1):
        if n_i == 0:
            continue
        
        # if a <= sum([int(char) for char in str(n_i)]) <= b:
        if a <= get_sum_of_digit(n_i) <= b:
            count += n_i

    print(count)
# solve()
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

```python
def solve():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    alice_points = 0
    bob_points = 0
    for card_i in range(n):
        if card_i % 2 == 0:
            alice_points += a_list[card_i]
        else:
            bob_points += a_list[card_i]

    print(alice_points - bob_points)
# solve()
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

```python
def solve():
    n = int(input())
    d_list = [int(input()) for d_i in range(n)]
    d_dict: Dict[int, int] = {i: 0 for i in range(110)}
    
    for d_n in d_list:
        d_dict[d_n] += 1

    count = 0
    for number in range(101):
        if d_dict[number] > 0:
            count += 1

    print(count)
```

## 第8問 ABC 085 C - Otoshidama

``` Python
def solve():
    number_of_bills, sum_of_bills = list(map(int, input().split()))
    for x in range(number_of_bills + 1):
        for y in range(number_of_bills + 1 - x):
            z = number_of_bills - x - y
            sum = 10000 * x + 5000 * y + 1000 * z
            if sum == sum_of_bills:
                print(x, y, z)
                return
    
    print(-1, -1, -1)
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
- [C \- Traveling ](https://atcoder.jp/contests/abc086/tasks/arc089_a)

```python
def solve():
    n = int(input())
    plans = []
    for _ in range(n):
        plans.append(list(map(int, input().split())))

    last_t = last_x = last_y = 0
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
```

## ここまで解いたら
### グリッドに関する処理
#### [B \- Minesweeper 解説](https://atcoder.jp/contests/abc075/tasks/abc075_b)
- [ABC075\-B \- Minesweeper を解く](https://kenkoro.hatenablog.com/entry/2019/05/26/000000)

```python
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
```

#### [C \- Grid Repainting 2 解説](https://atcoder.jp/contests/abc096/tasks/abc096_c)

```python
def solve():
    h, w = list(map(int, input().split()))
    field: List[str] = []
    for _ in range(h):
        field.append(list(input()))

    for row_i in range(h):
        for column_i in range(w):
            if field[row_i][column_i] == ".":
                continue
            
            # 上下左右が"#"かどうかを確認
            can_fill_in_close_cell = (row_i > 0 and field[row_i - 1][column_i] == "#") or \
                (row_i < h - 1 and field[row_i + 1][column_i] == "#") or \
                (column_i > 0 and field[row_i][column_i - 1] == "#") or \
                (column_i < w - 1 and field[row_i][column_i + 1] == "#")

            if can_fill_in_close_cell:
                continue
            else:
                print("No")
                return

    print("Yes")
```

### 区間の重なりを求める処理
#### [B \- Two Switches](https://atcoder.jp/contests/abc070/tasks/abc070_b)

```python
def solve():
    a, b, c, d = list(map(int, input().split()))
    time = 0
    for t in range(110):
        if (a <= t < b) and (c <= t < d):
            time += 1
    
    print(time)
```

- 公式の解説の通り

```python
def solve():
    a, b, c, d = list(map(int, input().split()))
    time = min(b, d) - max(a, c)
    if time < 0:
        time = 0
    print(time)
```

### 答えを 1000000007 (など) で割った余りで求める
#### [B \- Training Camp ](https://atcoder.jp/contests/abc055/tasks/abc055_b)

```python
def solve():
    n = int(input())
    power = 1
    for n_i in range(n + 1):
        if n_i == 0:
            continue
        power *= n_i
        power = power % (pow(10, 9) + 7)
    print(power)
```

### 数学的問題
#### [B \- AtCoDeerくんとボール色塗り](https://atcoder.jp/contests/abc046/tasks/abc046_b)

```python
def solve():
    number_of_balls, number_of_colors = list(map(int, input().split()))
    # k * (k - 1)^(n-1)
    result = number_of_colors
    result = result * pow(number_of_colors - 1, number_of_balls - 1)
    print(result)

```

#### [B \- Between a and b](https://atcoder.jp/contests/abc048/tasks/abc048_b)

- [AtCoder Regular Contest 064/ Beginner Contest 048 解説放送](https://www.youtube.com/watch?v=btAAdZqTCok)
    - 16:00~

```python

def solve():
    left, r, x = list(map(int, input().split()))
    # [0, R] - [0, L - 1]
    first = r // x + 1
    second = (left - 1) // x + 1
    if left == 0:
        print(first)
    else:
        print(first - second)
```

### 状態がループするシミュレーション処理
#### [B \- Choose Integers](https://atcoder.jp/contests/abc060/tasks/abc060_b)

- [ABC060: B \- Choice Integers（整数を扱う基本的な問題）](https://pyteyon.hatenablog.com/entry/2018/11/26/203000)
- [ABC060\-B 備忘録 p\.8](https://note.com/artechum/n/ne0bc05dd928e)

### [B \- Trained?](https://atcoder.jp/contests/abc065/tasks/abc065_b)

```python
def solve():
    number_of_buttons = int(input())
    buttons = []
    current_button_index = 0
    for _ in range(number_of_buttons):
        buttons.append(int(input()))

    max_operation = number_of_buttons
    for operation_i in range(max_operation):
        current_button_index = buttons[current_button_index] - 1
        if current_button_index == 1:
            print(operation_i + 1)
            return
    
    print(-1)
```

### 累積和
#### [C \- Candies](https://atcoder.jp/contests/abc087/tasks/arc090_a)
- [pythonでsumの計算ができない。](https://teratail.com/questions/341585)
- [AtCoder Regular Contest 090/ Beginner Contest 087 解説放送](https://www.youtube.com/watch?v=br3ze-KC6WA)

```python
def solve():
    number_of_candy = int(input())
    field: List[List[int]] = []
    for _ in range(2):
        field.append(list(map(int, input().split())))

    max_sum = 0
    # どのcolumnで下に移動したか
    for down_column_i in range(number_of_candy):
        sum_ = 0
        sum_ += sum(field[0][:down_column_i + 1])
        sum_ += sum(field[1][down_column_i:])
        max_sum = max(max_sum, sum_)

    print(max_sum)
```


### bit 全探索
#### [C \- Train Ticket](https://atcoder.jp/contests/abc079/tasks/abc079_c)
- [こわくないbit全探索2 基本編1: 簡単な例題でbit全探索をやってみよう！【競プロ解説】](https://qiita.com/u2dayo/items/8c1601a61841540b4947#%E9%81%B8%E3%81%B3%E6%96%B9%E3%81%8C%E3%82%8F%E3%81%8B%E3%82%8C%E3%81%B0%E5%90%88%E8%A8%88%E3%82%92%E6%B1%82%E3%82%81%E3%81%A6%E5%88%A4%E5%AE%9A%E3%81%99%E3%82%8B%E3%81%AE%E3%81%AF%E7%B0%A1%E5%8D%98)

```python
from itertools import product  # bit全探索

def solve():
    abcd = input()
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])
    
    for pro in product((0, 1), repeat=3):
        result = a
        result_str = f'{a}'

        if pro[0] == 0:
            result += b
            result_str += f'+{b}'
        else:
            result -= b
            result_str += f'-{b}'
        
        if pro[1] == 0:
            result += c
            result_str += f'+{c}'
        else:
            result -= c
            result_str += f'-{c}'

        if pro[2] == 0:
            result += d
            result_str += f'+{d}'
        else:
            result -= d
            result_str += f'-{d}'

        if result == 7:
            result_str += "=7"
            print(result_str)
            return
```

## もう一度
- 第7問 ABC 085 B - Kagami Mochi
- 10問目 ABC086C - Traveling