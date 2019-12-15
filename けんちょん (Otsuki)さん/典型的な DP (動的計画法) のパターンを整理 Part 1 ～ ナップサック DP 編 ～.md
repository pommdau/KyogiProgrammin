# [典型的な DP \(動的計画法\) のパターンを整理 Part 1 ～ ナップサック DP 編 ～](https://qiita.com/drken/items/a5e6fe22863b7992efdb)

## 1 ナップサック DP とは

- dp[0]が独自に定義されているので、添字の感覚が1つずれることに注意。
- e.g. `d[3]:= (a[0],...,a[2]の総和の最大値)`

![-w675](https://i.imgur.com/QtPMeIy.jpg)

``` Python
def solve():
    # input
    n = int(input())
    a = list(map(int, input().split()))

    # calc
    dp = []
    dp.append(0) # dp[0]:何も選ばない状態、の総和の最大値は0
    for i in range(n):
        dp.append(max(dp[i], dp[i] + a[i])) # e.g. (i=2)dp[3] = max(dp[2], dp[2]+a[2])

    print(dp[n])
```

inputの例

``` Python
3
7 -6 9
```
``` Python
2
-9 -16
```

## 2 ナップサック問題

![-w561](https://i.imgur.com/Wx7AYOB.jpg)


``` Python
def solve():

    # input
    n = int(input()) # 品物の数がN個
    weight = [0 for _ in range(110)]
    value  = [0 for _ in range(110)]
    for i in range(n):
        weight[i], value[i] = list(map(int, input().split()))
    W = int(input())

    # calc
    ## DP初期条件：dp[0][w] = 0
    dp = [[0 for i in range(110)] for j in range(10010)]

    # DP loop
    # dp[i+1][w] := a[0]~a[i]の総和の最大値
    for i in range(n):
        for w in range(W+1):    # 重さの最大値も対象に含めることに注意
            # dp[n+1][w] :=
            # (a[0],...,a[n]までの品物の中から大きさがwを超えない組み合わせの最大値)
            if (w >= weight[i]):
                dp[i+1][w] = max(dp[i][w-weight[i]] + value[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

    print(dp[n][W]) # dp[n][W] := (a[0],...,a[n-1]の総和の最大値)
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
8
```

# 問題 3:　部分和問題　

- `dp[i][j]`:=`(a[0],...,a[i-1])`の中から選んで総和を`j`とすることができるか。
    - e.g. `dp[3][10]` := `(a[0],a[1],a[2])`の中から選んで総和を`10`とすることができるか。


![-w827](https://i.imgur.com/MRrlALj.jpg)

``` Python
def solve():

    N = int(input())    # N個の整数の配列a[N]
    A = int(input())    # 目的の総和
    a = list(map(int, input().split()))

    # DP Table
    # dp[i][A] := (a[0],...,a[i-1])の中から選んで総和をjとすることが可能か
    dp = [[False for _ in range(110)] for _ in range(10010)]
    dp[0][0] = True # 何も選ばない場合に総和は0となる

    for n in range(N):
        for A_i in range(A+1):
            # dp[n][A_i]
            # := n個の配列(a[0],...,a[n-1])を使って総和を「A_i」とすることができるか
            dp[n+1][A_i] |= dp[n][A_i] # a[n]を選ばない場合
            if A_i >= a[n]:
                # a[n]を選ぶ場合
                # n+1個の配列(a[0],...,a[n]  )を使って総和をA_i       とすることができるか は
                # n個の配列  (a[0],...,a[n-1])を使って総和をA_i - a[n]とすることができるか と等しい
                dp[n+1][A_i] |= dp[n][A_i - a[n]]

    if dp[N][A]:
        print("YES")
    else:
        print("NO")

# solve()
```

# 問題 4:　部分和数え上げ問題　

``` Python
def solve():

    MOD = 1000000009

    N = int(input())    # N個の整数の配列a[N]
    A = int(input())    # 目的の総和
    a = list(map(int, input().split()))

    # DP Table
    # dp[i][A] := (a[0],...,a[i-1])の中から選んで総和をjとすることが可能か
    dp = [[0 for _ in range(110)] for _ in range(10010)]
    dp[0][0] = 1 # 何も選ばない場合は1通りのみである

    for n in range(N):
        for A_i in range(A+1):
            # dp[n][A_i]
            # := n個の配列(a[0],...,a[n-1])を使って総和を「A_i」とすることができる場合
            dp[n+1][A_i] += dp[n][A_i] # a[n]を選ばない場合
            dp[n+1][A_i] %= MOD
            if A_i >= a[n]:
                # a[n]を選ぶ場合
                # n+1個の配列(a[0],...,a[n]  )を使って総和をA_i       とすることができるか は
                # n個の配列  (a[0],...,a[n-1])を使って総和をA_i - a[n]とすることができるか と等しい
                dp[n+1][A_i] += dp[n][A_i - a[n]]
                dp[n + 1][A_i] %= MOD

    print(dp[N][A])

# solve()
```

input

``` Python
5
12
7 5 3 1 8
```

``` Python
4
5
4 1 1 1
```

# 問題 5:　最小個数部分和問題　

![-w801](https://i.imgur.com/VkIBoc1.jpg)

``` Python
def solve():

    INF = 1<<29 # 十分に大きい値にする

    N = int(input())    # N個の整数の配列a[N]
    A = int(input())    # 目的の総和
    a = list(map(int, input().split()))

    # DP Table
    # dp[i][A] := (a[0],...,a[i-1])の中から選んで総和をAとするとき、選ぶ整数の個数の最小値
    dp = [[INF for _ in range(110)] for _ in range(10010)]
    dp[0][0] = 0 # 何も選ばない場合は、つまり選ぶ整数の個数は0個である

    for n in range(N):
        for A_i in range(A+1):
            # dp[n][A_i]
            # := n個の配列(a[0],...,a[n-1])を使って総和を「A_i」とすることができる場合
            dp[n+1][A_i] = min(dp[n+1][A_i], dp[n][A_i]) # a[n]を選ばない場合

            if A_i >= a[n]:
                # a[n]を選ぶ場合
                # n+1個の配列(a[0],...,a[n]  )を使って総和をA_i       とすることができるか は
                # n個の配列  (a[0],...,a[n-1])を使って総和をA_i - a[n]とすることができるか と等しい
                dp[n+1][A_i] = min(dp[n+1][A_i], dp[n][A_i - a[n]] + 1)

    if dp[N][A] < INF:
        print(dp[N][A])
    else:
        print(-1)

# solve()
```

input

``` Python
5
12
7 5 3 1 8
```

``` Python
2
6
7 5
```

# 問題 6:　K個以内部分和問題

# 問題 8:　最長共通部分列 (LCS) 問題

- いまいち理解できていない所。

``` Python
def solve():
    S = input()
    T = input()

    # dp[s_i + 1][t_i + 1] := Sのs_i文字目までと、Tのt_i文字目までのLCSの長さ
    dp = [[0 for _ in range(1010)] for _ in range(1010)]

    for s_i in range(len(S)):
        for t_i in range(len(T)):
            # print("(S[" + str(s_i) + "], T[" + str(t_i) + "]) = " + "(" + S[s_i] + ", " + T[t_i] + ")")
            if S[s_i] == T[t_i]: # ここで初めてS[s_i], T[t_i]同士を比較する
                dp[s_i + 1][t_i + 1] = max(dp[s_i + 1][t_i + 1], dp[s_i][t_i] + 1)
                # print("インクリメントされました")
            dp[s_i + 1][t_i + 1] = max(dp[s_i + 1][t_i + 1], dp[s_i + 1][t_i])
            dp[s_i + 1][t_i + 1] = max(dp[s_i + 1][t_i + 1], dp[s_i][t_i + 1])

    print(dp[len(S)][len(T)])

# solve()
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

- 探索イメージ

``` Python
case : test_1
(S[0], T[0]) = (a, a)
(S[0], T[1]) = (a, c)
(S[0], T[2]) = (a, b)
(S[0], T[3]) = (a, e)
(S[0], T[4]) = (a, f)
(S[1], T[0]) = (b, a)
(S[1], T[1]) = (b, c)
(S[1], T[2]) = (b, b)
(S[1], T[3]) = (b, e)
(S[1], T[4]) = (b, f)
(S[2], T[0]) = (c, a)
(S[2], T[1]) = (c, c)
(S[2], T[2]) = (c, b)
(S[2], T[3]) = (c, e)
(S[2], T[4]) = (c, f)
(S[3], T[0]) = (d, a)
(S[3], T[1]) = (d, c)
(S[3], T[2]) = (d, b)
(S[3], T[3]) = (d, e)
(S[3], T[4]) = (d, f)
(S[4], T[0]) = (e, a)
(S[4], T[1]) = (e, c)
(S[4], T[2]) = (e, b)
(S[4], T[3]) = (e, e)
(S[4], T[4]) = (e, f)
```