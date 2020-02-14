## 例題 2-2-3　Best Cow Line (POJ No.3617)

### 本書

``` Python
def solve():
    number_of_characters = int(input())
    input_string = input()
    output_string = ""

    # 検索用インデックス
    left_index = 0
    right_index = number_of_characters - 1

    while left_index <= right_index:  # 左右の検索インデックスが同じになるまでループする
        is_left_younger = False  # 左から見たときの方が小さくなるかどうか
        search_count = 0
        while left_index + search_count <= right_index:
            if input_string[left_index + search_count] < input_string[right_index - search_count]:
                is_left_younger = True
                break
            elif input_string[left_index + search_count] > input_string[right_index - search_count]:
                is_left_younger = False
                break
            search_count += 1  # s[a+i] == s[b-i]のとき、次の文字同士の比較を行う

        if is_left_younger:
            output_string += input_string[left_index]
            left_index += 1  # increment left index
        else:
            output_string += input_string[right_index]
            right_index -= 1  # increment right index

    print(output_string)
```

### [ABC 076 C Dubious Document 2　(辞書順最小 Greedy の練習です)](https://atcoder.jp/contests/abc076/tasks/abc076_c)



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