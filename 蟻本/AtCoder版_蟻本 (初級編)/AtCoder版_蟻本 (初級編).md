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

