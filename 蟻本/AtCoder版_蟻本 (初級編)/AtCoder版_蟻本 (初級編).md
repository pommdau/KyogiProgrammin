# [AtCoder 版！蟻本 \(初級編\)](https://qiita.com/drken/items/e77685614f3c6bf86f44)

# 参考
- [蟻本をPythonで \(初級編\)](https://qiita.com/saba/items/affc94740aff117d2ca9)

# Tips
## 実行時間上限の目安
- 1億を超えると厳しそう

![](https://i.imgur.com/vZGreXd.jpg)

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