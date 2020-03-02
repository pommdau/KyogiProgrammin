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

``` Python
def solve():
    input_string = input()
    part_string = input()

    for i in range(len(input_string) - len(part_string), -1, -1):
        possible_part_string = input_string[i:i+len(part_string)]  # part_stringの可能性のある文字列
        for j in range(len(part_string) + 1):  # 1つ多くループしているのは最後の処理のため
            if j == len(part_string):
                result = input_string[:i] + part_string + input_string[i + len(part_string):]
                result = result.replace("?", "a")
                print(result)
                return  # 今回のテストケースの終了
            if possible_part_string[j] == "?" or possible_part_string[j] == part_string[j]:
                continue
            else:  # 再度ずらして探索する
                break

    print("UNRESTORABLE")
```

- 正規表現を使ったやり方もあります
	- [C \- Dubious Document 2](https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2017/1028_abc076)

``` Python
import re


def solve():
    input_string = input()
    part_string = input()

    input_string = input_string.replace('?', '.')
    length_of_input_string, length_of_part_string = len(input_string), len(part_string)
    if length_of_input_string < length_of_part_string:
        print("UNRESTORABLE")

    ans = []
    for i in range(length_of_input_string - length_of_part_string + 1):  #
        m = re.match(input_string[i:i+length_of_part_string], part_string)
        if m is None:
            continue
        # 正規表現で見つかったらt以外の「.」はaとする
        ans.append((input_string[:i] + part_string + input_string[i + length_of_part_string:]).replace('.', 'a'))

    if not ans:  # 見つからなかった場合
        print("UNRESTORABLE")
    else:
        print(min(ans))  # 見つかったもののうち一番小さいものを採用する
```

### [ABC 007 B 辞書式順序　(そもそも辞書次式順序とはなにか)](https://atcoder.jp/contests/abc007/tasks/abc007_2)

``` Python
def solve():
    input_string = input()
    if input_string == "a":
        print("-1")
    else:
        print("a")
```

### [ABC 009 C 辞書式順序ふたたび　(かなり難しいです)](https://atcoder.jp/contests/abc009/tasks/abc009_3)

