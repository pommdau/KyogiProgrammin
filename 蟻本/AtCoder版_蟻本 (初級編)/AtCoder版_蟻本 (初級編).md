# [AtCoder 版！蟻本 \(初級編\)](https://qiita.com/drken/items/e77685614f3c6bf86f44)

# 参考
- [蟻本をPythonで \(初級編\)](https://qiita.com/saba/items/affc94740aff117d2ca9)

# Tips
## 実行時間上限の目安
- 1億を超えると厳しそう

![](https://i.imgur.com/vZGreXd.jpg)


### ？？？

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


### 例題 2-2-3　Best Cow Line (POJ No.3617)
#### 本書


#### ABC 076 C Dubious Document 2



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