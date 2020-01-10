# [AtCoder 版！蟻本 \(初級編\)](https://qiita.com/drken/items/e77685614f3c6bf86f44)

# 参考
- [蟻本をPythonで \(初級編\)](https://qiita.com/saba/items/affc94740aff117d2ca9)

# Tips
## 実行時間上限の目安
- 1億を超えると厳しそう

![](https://i.imgur.com/vZGreXd.jpg)


# 1-6 気楽にウォーミングアップ
## 例題 1-6-1　三角形
### 本書

``` Python
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    answer = 0
    for first_i in range(n):
        for second_i in range(first_i + 1, n):
            for third_i in range(second_i + 1, n):
                # print("(" + str(first_i) + "," + str(second_i) + "," + str(third_i) + ")") # for分型の全探索
                perimeter = a[first_i] + a[second_i] + a[third_i]
                long_side_length = max(a[first_i], a[second_i], a[third_i])
                remaining_side_length = perimeter - long_side_length

                if long_side_length < remaining_side_length:  # 三角形が作れる場合
                    answer = max(answer, perimeter)
    print(str(answer))
```

### 【AtCoder 上の類題】

#### ARC 004 A 2点間距離の最大値　(全探索部分の考え方は一緒)

``` Python
def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    length_max = 0
    x_i = 0
    y_i = 1
    for first_i in range(N):
        for second_i in range(first_i + 1, N):
            x = abs(points[first_i][x_i] - points[second_i][x_i])
            y = abs(points[first_i][y_i] - points[second_i][y_i])
            length_max = max(length_max, (x**2+y**2)**0.5)

    print(length_max)
```

```sh
3
1 1
2 4
4 3
```

```sh
10
1 8
4 0
3 7
2 4
5 9
9 1
6 2
0 2
8 6
7 8
```

#### ABC 051 B Sum of Three Integers　(よい練習問題です)

``` Python
def solve():
    number_max, sum_of_numbers = list(map(int, input().split()))
    number_of_allocation = 0
    for x_i in range(number_max + 1):
        for y_i in range(number_max + 1):
            z_i = sum_of_numbers - x_i - y_i
            if 0 <= z_i and z_i <= number_max:
                number_of_allocation += 1

    print(str(number_of_allocation))
```
```sh
2 2
```


#### ABC 085 C Otoshidama　(よい練習問題です)

``` Python
def solve():
    number_of_bills, sum_of_otoshidama = list(map(int, input().split()))
    # number_of_bills, sum_of_otoshidama = [5, 10000] # for debug
    for ten_thousand_i in range(number_of_bills + 1):
        for five_thousand_i in range(number_of_bills - ten_thousand_i + 1):
            # print(str(ten_thousand_i) + "," + str(five_thousand_i))
            thousand_i = number_of_bills - ten_thousand_i - five_thousand_i
            if 10000 * ten_thousand_i + 5000 * five_thousand_i + 1000 * thousand_i == sum_of_otoshidama:
                print(ten_thousand_i, five_thousand_i, thousand_i, sep=" ")
                return
    print(-1, -1, -1, sep=" ")
```

``` Python
9 45000
```

``` Python
20 196000
```

``` Python
2000 20000000
```

## 例題 1-6-2　Ants (POJ No.1852)
### 本書

``` Python
def solve():
    length = int(input())
    number_of_ants = int(input())
    position_of_ants = list(map(int, input().split()))
    time_minimun = 0
    time_maximum = 0
    for ants_i in range(number_of_ants):
        time_minimum = min(time_maximum, position_of_ants[ants_i], abs(length - position_of_ants[ants_i]))
        time_maximum = max(time_maximum, position_of_ants[ants_i], abs(length - position_of_ants[ants_i]))

    print("minimum:" + str(time_minimum))
    print("maximum:" + str(time_maximum))
```

``` Python
10
3
2 6 7
```

### AGC 013 C Ants on a Circle
// TODO

# 2 基礎からスタート！ --- 初級編
# 2-1 すべての基本 "全探索"
## 例題 2-1-1　部分和問題
### 本書

## 例題 2-1-2　Lake Counting (POJ No.2386)

### 本書

``` Python
N, M = 10, 12
field = [['W', '.', '.',  '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
         ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']]

def dfs(x, y):
    field[x][y] = '.'

    # 移動する8方向をループ
    for dx in range(-1, 2): # -1 -> 0 -> 1
        for dy in range(-1, 2):
            # x方向にdx、y方向にdy移動した場所を(nx, ny)とする
            nx = x + dx
            ny = y ; dy

            # まず nxとnyが庭の範囲内かどうか
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                # field[nx][ny]が水たまりかどうか
                if field[nx][ny] == 'W':
                    dfs(nx, ny)

def solve():
    res = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W': # 適当なWから始める
                # W が残っているならそこから dfs を始める
                dfs(i, j) # 隣接する`W`を`.`へ塗り替える
                res += 1  # 塗り替え終わったらカウント

    print(res)
```

#### ATC 001 A 深さ優先探索　(かなり似ています)

``` Python
H, W    = 0, 0
field   = [] # 迷路
reached = [] # 到達できるかどうか

def search(x, y):
    # 迷路の外側課壁の場合は何もしない
    if x < 0 or W <= x or y < 0 or H <= y:
        return

    # 壁（#）の場合、何もしない
    if field[y][x] == '#':
        return

    # 以前に到達したことがある場合、何もしない
    if reached[y][x]:
        return

    reached[y][x] = True

    # 4方向を試す
    search(x - 1, y    )
    search(x + 1, y    )
    search(x    , y - 1)
    search(x    , y + 1)

def solve():
    global H
    global W
    global field
    field = []
    global reached
    reached = []

    H, W = list(map(int, input().split()))
    for h_i in range(H):
        field.append(list(input()))
        reached.append([False for _ in range(W)])
    print(field)

    sX, sY, gX, gY = [0, 0, 0, 0]
    for h_i in range(H):
        for w_i in range(W):
            if field[h_i][w_i] == 's': # 家から始める
                sX, sY = w_i, h_i
            if field[h_i][w_i] == 'g':
                gX, gY = w_i, h_i
    search(sX, sY)

    if (reached[gY][gX]):
        print("Yes")
    else:
        print("No")
```

## 例題 2-1-3　迷路の最短路
### 本書
TODO:

### ABC 007 C 幅優先探索　(まんまです)

``` Python
from collections import deque

# 幅優先探索
def bfs(maze, visited, sy, sx, gy, gx):
	# スタート地点の設定
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    
    while queue:
        y, x = queue.popleft() # キューでは右から左にオブジェクトを格納している
        if [y, x] == [gy, gx]: # ゴールの場合
            return visited[y][x]
        for dy, dx in ([1, 0], [-1, 0], [0, 1], [0, -1]): # 順に上・下・右・左
            new_y, new_x = y+dy, x+dx
            if maze[new_y][new_x] == "." and \
                    visited[new_y][new_x] == -1:    # 通行可能かつ未到達の場合
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])

def solve():
    R, C = list(map(int ,input().split()))   # Row, Column数
    sy, sx = list(map(int, input().split())) # Start Point
    gy, gx = list(map(int, input().split())) # Goal Point
    sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1 # 与えられた座標を、プログラム側の実装に合わせる

    maze = [input() for _ in range(R)]   # maze:迷路
    visited = [[-1]*C for _ in range(R)] # スタート地点からそのマスにいくまでの最短距離

    print(bfs(maze, visited, sy, sx, gy, gx))
```

### 例題 2-1-4　特殊な状態の列挙
#### 本書

#### [ABC 054 C One-stroke Path](https://atcoder.jp/contests/abc054/tasks/abc054_c)

``` Python
import itertools

def solve():

    from itertools import permutations

    N, M = list(map(int, input().split()))
    edges = set() # 辺を並べる全ての順番
    for _ in range(M):
        a, b = list(map(int, input().split()))
        edges.add((a, b))
        edges.add((b, a))


    number_of_one_stroke = 0 # 一筆書きができる順列の数
    for p in permutations(range(2, N + 1)):
        ordering = (1,) + p # 始点1を加える
        # orderings = (1, *p) # Python3.5から

        is_one_stroke = True # 現在の順列が1筆書きできるかどうか
        for move in zip(ordering, ordering[1:]):  # moveには隣同士のペアを表す
            is_one_stroke *= move in edges

        if is_one_stroke:
            number_of_one_stroke += 1

    print(number_of_one_stroke)
```

##### 参考

- [蟻本初級編攻略 \- 2\-1 特殊な状態の列挙](http://zehnpaard.hatenablog.com/entry/2018/06/19/211646)
	- 上記の記事を参考にした。記事内ではもっと凝縮した書き方をしている。

- [Pythonのrange関数の使い方](https://note.nkmk.me/python-range-usage/)

> 引数startの値は結果に含まれるが引数stopの値は含まれないので注意。

``` Python
print(list(range(3, 10)))
# [3, 4, 5, 6, 7, 8, 9]
```

- `itertools.permutations`の例

``` Python
for p in permutations(range(2, 7 + 1)): # e.g. (2, 3, 4, 5, 6, 7)の取り得る並び替え全てを与える
    print(p)
```

- [Python, zip関数の使い方: 複数のリストの要素をまとめて取得](https://note.nkmk.me/python-zip-usage-for/)

``` Python
names = ['Alice', 'Bob', 'Charlie']
ages = (24, 50, 18)

z = zip(names, ages)
print(z)
print(type(z))
# <zip object at 0x10b57b888>
# <class 'zip'>
```

#### JOI 2009 予選 D カード並べ

``` Python
import itertools

def solve():
    from itertools import permutations

    n = int(input()) # number of cards
    k = int(input()) # number of selected cards
    numbers = [input() for _ in range(n)]

    created_numbers = set()

    for permutation in permutations(numbers):
        part_of_permutation_= permutation[:k] # [0]から[k-1]番目までの数字を抜き出す
        number_string = "".join(part_of_permutation_)
        created_numbers.add(number_string)

    print(len(created_numbers))

#solve()
```

## 2-2 猪突猛進！ "貪欲法"
### 例題 2-2-1　硬貨の問題
#### 本書

``` Python
def solve():
    coin_values = [1, 5, 10, 50, 100, 500]
    number_of_coins_list = list(map(int, input().split())) # 1,5,10,50,100,500の順
    A = int(input()) # 合計金額

    result = [0 for _ in range(6)]
    for i in range(5, -1, -1): # 5,4,3,2,1,0
        # コイン[i]を使う枚数
        number_of_coins = min(A // coin_values[i], number_of_coins_list[i])
        A -= number_of_coins * coin_values[i]
        result[i] = number_of_coins

    print(result)
```

```sh
3 2 1 3 0 2
620
```

#### JOI 2007 予選 A おつり　

``` Python
def solve():
    coin_values = [1, 5, 10, 50, 100, 500]

    price = int(input())
    change = 1000 - price # お釣り

    coins_num = 0
    for coin_i in range(5, -1, -1):
        coin_num = change // coin_values[coin_i]
        change -= coin_values[coin_i] * coin_num
        coins_num += coin_num

    print(coins_num)
```

### 例題 2\-2\-2　区間スケジューリング問題
#### 本書

``` Python
def solve():
    n = int(input())

    tasks = []
    s, t = [list(map(int, input().split())) for i in range(2)]
    for task in zip(s, t):
        tasks.append(task)

    from operator import itemgetter
    tasks.sort(key=itemgetter(1)) # 終了時間が早い順に並び替え

    # 選べる仕事の中で、終了時間が最も早いものを選ぶことを繰り返す
    number_of_tasks = 0
    finish_time = 0 # 最後に選んだ仕事の終了時間
    for task in tasks:
        if finish_time < task[0]:
            finish_time = task[1]
            number_of_tasks += 1

    print(number_of_tasks)
```

##### 参考

- [はらへり日記 \- Pythonで二次元配列をsortする](http://sota1235.com/blog/2015/04/23/python_sort_twodime.html)

``` Python
from operator import itemgetter

my_list = [[2, 30], [4, 10], [1, 50], [3, 20]] # [[2, 30], [4, 10], [1, 50], [3, 20]]
my_list.sort(key=itemgetter(1))                # [[4, 10], [3, 20], [2, 30], [1, 50]]
```

#### KUPC 2015 A 東京都　

``` Python
def solve():
    T = int(input()) # テストケースの数
    S = [input() for _ in range(T)]

    for S_i in S:
        word_count = 0
        search_i = 0
        for _ in S_i: # 検索開始場所をインクリメントしていく
            if S_i.startswith("tokyo", search_i) or S_i.startswith("kyoto", search_i):
                search_i += 5
                word_count += 1
            else:
                search_i += 1
        print(word_count)
```

#### ABC 103 D - Islands War

- [AtCoder ABC 103 D \- Islands War \(400 点\) \- けんちょんの競プロ精進記録](http://drken1215.hatenablog.com/entry/2018/07/21/224200)
	- 串刺しの説明がしっくりくる

``` Python
def solve():
    N, M = list(map(int, input().split())) # N:島の数 M:要望の数

    requests = []

    for m_i in range(M):
        a, b = list(map(int, input().split()))
        requests.append([a-1, b-1]) # 配列のインデックスに表す
    print(requests)

    from operator import itemgetter
    requests.sort(key=itemgetter(1)) # 2番目の要素で照準ソート

    remove_count = 0 # 削除した橋の数
    last_remove_index = 0 # 最後に取り除いた島（b側）のインデックス
    for request in requests:
        if last_remove_index > request[0]: # b[i] > a[i+1]のときはカウントしない
            continue
        last_remove_index = request[1]
        remove_count += 1

    print(remove_count)
```

### 例題 2-2-3　Best Cow Line (POJ No.3617)
#### 本書

``` Python
def solve():
    N = int(input())
    s = input()
    t = ""

    # 検索用インデックス
    a = 0     # left
    b = N - 1 # right

    while a <= b: # 左右の検索インデックスが同じになるまでループする
        is_left_ascending = False # 左から見たときの方が小さくなるかどうか
        i = 0
        while a + i <= b:
            if s[a + i] < s[b - i]: # 一つ先の文字列比較
                is_left_ascending = True
                break
            elif s[a + i] > s[b - i]:
                is_left_ascending = False
                break
            i += 1 # s[a+i] == s[b-i]のとき、次の文字の比較を行う

        if is_left_ascending:
            t += s[a]
            a += 1 # increment left index
        else:
            t += s[b]
            b -= 1 # increment right index

    print(t)
```

#### ABC 076 C Dubious Document 2

- 正規表現を使ったやり方もある
	- [C \- Dubious Document 2](https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2017/1028_abc076)

``` Python
import re

def solve2(s, t):
    s = s.replace('?', '.')
    ls, lt = len(s), len(t)
    if ls < lt:
        return 'UNRESTORABLE'
    ans = []
    for i in range(ls - lt + 1): # iは「ls-lt」までを取る
        m = re.match(s[i:i + lt], t)
        if m is None:
            continue
        ans.append((s[:i] + t + s[i + lt:]).replace('.', 'a')) # 正規表現で見つかったらt以外の「.」はaとする

    if not ans: # 見つからない場合
        return 'UNRESTORABLE'
    return min(ans) # 見つかったもののうち一番小さいものを採用する

def solve():
    s = input().strip() # ?tc????
    t = input().strip() # coder

    print(solve2(s, t))
```

### [例題 2\-2\-4　Saruman's Army \(POJ No\.3069\)](https://qiita.com/drken/items/e77685614f3c6bf86f44#%E4%BE%8B%E9%A1%8C-2-2-4sarumans-army-poj-no3069)

``` Python
def solve():
    number_of_points = int(input())  # 点の数
    distance         = int(input())  # 各点が離れられる最大距離R
    points           = list(map(int, input().split()))  # 各点の情報

    i   = 0
    ans = 0  # 印をつけた数

    while i < number_of_points:
        # sはカバーされていない一番左の点の位置
        s = points[i]
        i += 1
        # sから距離Rを超える点まで進む!
        while i < number_of_points and points[i] <= s + distance:
            i += 1  # 条件内なので次の点を検索

        # pは新しく印をつける点の位置
        p = points[i - 1] # 条件外の点の一つ前の点に印を付ける

        # pから距離Rを超える点まで（iの値を）進める（次に探索を始める点まで進む）
        while i < number_of_points and points[i] <= p + distance:
            i += 1
            
        ans += 1
    print(str(ans))
```

#### ABC 083 C Multiple Gift