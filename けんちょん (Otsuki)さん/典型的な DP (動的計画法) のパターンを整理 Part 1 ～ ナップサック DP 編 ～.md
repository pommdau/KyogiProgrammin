# [典型的な DP \(動的計画法\) のパターンを整理 Part 1 ～ ナップサック DP 編 ～](https://qiita.com/drken/items/a5e6fe22863b7992efdb)

# TODO:dpの宣言のところで配列のサイズ逆になっている。適宜修正すること。

# 1 ナップサック DP とは
## 問題 1:　最大和問題
- dp[0]が独自に定義されているので、添字の感覚が1つずれることに注意。
- e.g. `d[3]:= (a[0],...,a[2]の総和の最大値)`

![-w675](https://i.imgur.com/QtPMeIy.jpg)

``` Python
def solve():
    number_of_input = int(input())
    numbers = list(map(int, input().split()))

    dp = []  # dp[i] := numbers[0],numbers[1],...,numbers[i-1]の総和の最大値
    dp.append(0)  # dp[0]:何も選ばない状態、の総和の最大値は0

    for i in range(number_of_input):
        dp.append(max(dp[i], dp[i] + numbers[i]))

    print(dp[number_of_input])
```

- `input`

``` Python
3
7 -6 9
```
``` Python
2
-9 -16
```

# 2 ナップサック問題
## 問題 2:　ナップサック問題

![-w561](https://i.imgur.com/Wx7AYOB.jpg)

``` Python
WEIGHT_INDEX = 0
VALUE_INDEX = 1

def solve():
    number_of_input = int(input())
    items = [list(map(int, input().split())) for _ in range(number_of_input)]
    limit_weight = int(input())

    # DP初期条件: dp[0][w] = 0
    # dp[i][w] := items[0]~items[i-1]から品物を選んで、重さが[w]を超えない場合の価値の最大値
    dp = [[0 for _ in range(10010)] for _ in range(110)]

    for item_i, item in enumerate(items):
        for each_limit_weight in range(limit_weight + 1):
            if item[WEIGHT_INDEX] <= each_limit_weight:  # itemが追加できる重量の場合
                # 「item」を追加できる場合、価値が大きくなる方を採用する
                # dp[item_i][each_limit_weight - item[WEIGHT_INDEX]] := 過去の情報を用いるイメージ
                dp[item_i + 1][each_limit_weight] = \
                    max(dp[item_i][each_limit_weight - item[WEIGHT_INDEX]] + item[VALUE_INDEX],
                        dp[item_i][each_limit_weight]
                        )
            else:
                dp[item_i + 1][each_limit_weight] = dp[item_i][each_limit_weight]

    print(dp[number_of_input][limit_weight])
```

- `input`は以下

```
6
2 3
1 2
3 6
2 1
1 3
5 85
9
```

# 3 部分和問題とその応用たち
## 問題 3:　部分和問題　

- `dp[i][j]`:=`(a[0],...,a[i-1])`の中から選んで総和を`j`とすることができるか。
    - e.g. `dp[3][10]` := `(a[0],a[1],a[2])`の中から選んで総和を`10`とすることができるか。


![-w827](https://i.imgur.com/MRrlALj.jpg)

``` Python
def solve():
    number_of_items = int(input())    # N個の整数の配列a[N]
    items = list(map(int, input().split()))  # itemの内容は重さ
    sum_of_result = int(input())    # 目的の総和

    # dp[item_i][sum] := items[0]~items[item_i-1]の中から選んで総和を[sum]とすることができるか
    # +1は処理の兼ね合いでの下駄履かせ
    dp = [[False for _ in range(number_of_items+1)] for _ in range(sum_of_result+1)]
    dp[0][0] = True  # 何も選ばない場合の総和は0とする

    for item_i, item in enumerate(items):
        for each_sum in range(sum_of_result + 1):
            dp[item_i+1][each_sum] |= dp[item_i][each_sum]  # itemを選ばない場合
            if item <= each_sum:  # itemを選ぶ場合
                dp[item_i+1][each_sum] |= dp[item_i][each_sum-item]

    if dp[number_of_items][sum_of_result]:
        print("YES")
    else:
        print("NO")
```

```sh
3
7 5 3
10
```

```sh
2
9 7
6
```

## 問題 4:　部分和数え上げ問題　

- `MOD`はオーバーフローを懸念して、最後ではなくそれぞれの処理内で呼んでいる？

``` Python
NUMBER_FOR_MOD = 1000000009


def solve():
    number_of_items = int(input())
    items = list(map(int, input().split()))
    sum_of_result = int(input())

    # dp[i][sum] := item[0]~item[i-1]の中から商品を選んで、総和をsumとできる組み合わせの数
    dp = [[0 for _ in range(110)] for _ in range(10010)]
    dp[0][0] = 1  # 総和が0となるのは、何も選ばない場合である

    for item_i, item in enumerate(items):
        for each_sum in range(sum_of_result+1):
            dp[item_i + 1][each_sum] += dp[item_i][each_sum]  # itemを選ばない場合
            dp[item_i + 1][each_sum] %= NUMBER_FOR_MOD
            if item <= each_sum:  # itemを選ぶ場合、条件にあっていれば…
                dp[item_i + 1][each_sum] += dp[item_i][each_sum - item]
                dp[item_i + 1][each_sum] %= NUMBER_FOR_MOD

    print(dp[number_of_items][sum_of_result])
```

- `input`

``` Python
5
7 5 3 1 8
12
```

``` Python
4
4 1 1 1
5
```

## 問題 5:　最小個数部分和問題　

``` Python
INF = 1 << 29  # 十分大きい値にする, INT_MAX にしないのはオーバーフロー対策


def solve():
    number_of_items = int(input())
    items = list(map(int, input().split()))
    sum_of_result = int(input())

    # dp[i][sum] := item[0]~item[i-1]の中から商品を選んで、操作がsumとなるときの、選ぶ商品の個数の最小値
    dp = [[INF for _ in range(110)] for _ in range(10010)]
    dp[0][0] = 0  # 総和が0となるのは、何も選ばない場合である

    for item_i, item in enumerate(items):
        for each_sum in range(sum_of_result+1):
            # itemを選ばない場合
            dp[item_i + 1][each_sum] = min(dp[item_i + 1][each_sum],
                                           dp[item_i][each_sum])

            if item <= each_sum:  # itemを選ぶ場合、条件にあっていれば…
                dp[item_i + 1][each_sum] = min(dp[item_i + 1][each_sum],
                                               dp[item_i][each_sum - item] + 1)

    if dp[number_of_items][sum_of_result] < INF:
        print(dp[number_of_items][sum_of_result])
    else:
        print(-1)
```

- `input`

``` Python
5
7 5 3 1 8
12
```

``` Python
2
7 5
6
```

## 問題 6:　K個以内部分和問題

``` Python
INF = 1 << 29


def solve():
    number_of_items = int(input())
    limit_number_of_selection = int(input())  # K個以内の整数を選ぶ
    items = list(map(int, input().split()))
    result_sum = int(input())

    # dp[i][sum] := items[0]~items[i-1]から品物を選び、総和がsumとなる場合の、選んだ品物の個数の最小値
    dp = [[INF for _ in range(110)] for _ in range(10010)]
    dp[0][0] = 0  # 総和が0となるのは何も選ばない場合

    for item_i, item in enumerate(items):
        for each_sum in range(result_sum + 1):
            # itemを選ばない場合
            dp[item_i + 1][each_sum] = min(dp[item_i + 1][each_sum],
                                           dp[item_i][each_sum])
            # itemを選ぶ場合
            if item <= each_sum:
                dp[item_i + 1][each_sum] = min(dp[item_i + 1][each_sum],
                                               dp[item_i][each_sum - item] + 1)

    if dp[number_of_items][result_sum] <= limit_number_of_selection:
        print("YES")
    else:
        print("NO")
```

``` Python
3
2
7 5 3
10
```

``` Python
3
1
7 5 3
10
```

## 問題 7:　個数制限付き部分和問題

``` Python
def solve():
    number_of_balls = int(input())
    items = list(map(int, input().split()))
    each_number_of_item = list(map(int, input().split()))
    result_sum = int(input())

    # dp[i + 1][j] := item[0]~item[i]の中から選んで、総和jが作れるか
    dp = [[False] * (result_sum + 1) for i in range(number_of_balls + 1)]
    dp[0][0] = True

    for item_i, item in enumerate(items):
        for each_sum in range(result_sum + 1):
            each_item_i = 0
            while each_item_i <= each_number_of_item[item_i] and \
                    each_item_i * items[item_i] <= each_sum:
                # 各ボール(=items[item_i])をeach_item_i個使ったときの情報を記録する
                dp[item_i + 1][each_sum] |= dp[item_i][each_sum - each_item_i * items[item_i]]
                each_item_i += 1

    if dp[number_of_balls][result_sum]:
        print("Yes")
    else:
        print("No")
```

## 問題 8:　最長共通部分列 (LCS) 問題

- [アルゴリズム1000本ノック \#3\. Longest common subsequence](https://qiita.com/_rdtr/items/c49aa20f8d48fbea8bd2)
    - この記事が視覚的に分かりやすい。

> 次は `Table[1][2]` で, `S1[1] == S2[2]` となっています! したがってLCSの長さを1伸ばすことができます. ここで私たちは同時に,  **Table[0][1] の状態から斜めにしかこのセルに到達できない** ことに気づきます. `Table[0][2]` と `Table[1][1]` においては, `S1[1]` あるいは `S2[2]` (= `"2"`) が既に考慮済のためです.

- ここがまだ腑に落ちないけど、一緒のタイミングで末尾が同じじゃないとカウントできない、みたいな認識であってるのかな。

``` Python
def solve():
    first_sentense = input()
    second_sentense = input()

    # dp[s_i + 1][t_i + 1] := Sのs_i文字目までと、Tのt_i文字目までのLCSの長さ
    dp = [[0 for _ in range(1010)] for _ in range(1010)]

    for first_i in range(len(first_sentense)):
        for second_i in range(len(second_sentense)):
            print("(S[" + str(first_i) + "], T[" + str(second_i) + "]) = " + "(" + first_sentense[first_i] + ", " + second_sentense[second_i] + ")")
            if first_sentense[first_i] == second_sentense[second_i]:  # LCSが長くなる場合
                dp[first_i + 1][second_i + 1] = max(dp[first_i + 1][second_i + 1],
                                                    dp[first_i][second_i] + 1)

            # LCSの長さが変わらない場合
            dp[first_i + 1][second_i + 1] = max(dp[first_i + 1][second_i + 1], dp[first_i + 1][second_i])
            dp[first_i + 1][second_i + 1] = max(dp[first_i + 1][second_i + 1], dp[first_i][second_i + 1])
    print(dp[len(first_sentense)][len(second_sentense)])
```

- input

``` Python
abcde
acbef
```

``` Python
pirikapirirara
poporinapeperuto
```

## [問題 9:　最小コスト弾性マッチング問題](https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-9%E6%9C%80%E5%B0%8F%E3%82%B3%E3%82%B9%E3%83%88%E5%BC%BE%E6%80%A7%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C)

