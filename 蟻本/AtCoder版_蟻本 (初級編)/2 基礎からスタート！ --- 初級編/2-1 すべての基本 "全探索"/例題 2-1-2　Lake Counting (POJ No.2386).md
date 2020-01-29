# 例題 2-1-2　Lake Counting (POJ No.2386)

## 本書

``` Python
height, width = 10, 12  # 10*12の庭。W:=水たまり
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


# 2次元座標のとり方がx,yが逆になってしまうが他にやりようはあるか…？
def dfs(x, y):
    field[y][x] = '.'
    #  8方向に移動を試みる
    for dy in range(-1, 2):   # -1, 0, 1
        for dx in range(-1, 2):
            ny = y + dy  # ny:= new_y
            nx = x + dx
            #  移動先が範囲内かどうか
            if 0 <= ny <= height - 1 and 0 <= nx <= width - 1:
                if field[ny][nx] == 'W':
                    dfs(nx, ny)


def solve():
    number_of_puddles = 0

    for height_i in range(height):
        for width_i in range(width):
            if field[height_i][width_i] == 'W':  # すべてのマスを走査する
                dfs(width_i, height_i)  # 隣接する'W'を'.'に置換する
                number_of_puddles += 1  # 置換し終わったらカウントする
    print(number_of_puddles)
```

## 【AtCoder 上の類題】
### ATC 001 A 深さ優先探索　(かなり似ています)

``` Python
height = 0
width = 0
field = []  # 迷路
reached = []  # その地点に到達できたかどうか


# DFS
def search(x, y):
    if x < 0 or width - 1 < x or y < 0 or height - 1 < y:
        return

    # 塀(#)の場合は何もしない
    if field[y][x] == '#':
        return

    # すでに探索済みの場合
    if reached[y][x]:
        return

    reached[y][x] = True

    search(x - 1, y)
    search(x + 1, y)
    search(x, y - 1)
    search(x, y + 1)

def solve():
    global height
    global width
    global field
    field = []
    global reached
    reached = []

    height, width = list(map(int, input().split()))
    for height_i in range(height):
        field.append(list(input()))
        reached.append([False for _ in range(width)])

    start_x, start_y, goal_x, goal_y = 0, 0, 0, 0
    for height_i in range(height):
        for width_i in range(width):
            if field[height_i][width_i] == 's':
                start_x, start_y = width_i, height_i
            if field[height_i][width_i] == 'g':
                goal_x, goal_y = width_i, height_i

        # スタート地点から探索開始
        search(start_x, start_y)

    if (reached[goal_y][goal_x]):
        print("Yes")
    else:
        print("No")
```

### [ARC 031 B 埋め立て　(比較的似ています)](https://atcoder.jp/contests/arc031/tasks/arc031_2)

``` Python
import copy

def dfs(x, y, field_for_search):
    if x < 0 or 10 <= x or y < 0 or 10 <= y:
        return

    if field_for_search[y][x] == 'o':
        field_for_search[y][x] = "x"
        dfs(x-1, y, field_for_search)
        dfs(x+1, y, field_for_search)
        dfs(x, y-1, field_for_search)
        dfs(x, y+1, field_for_search)

def solve():
    field = []

    for height_i in range(10):
        field.append(list(input()))

    # 全マスに対して埋め立てを行ってみる
    for height_i in range(10):
        for width_i in range(10):

            if field[height_i][width_i] == 'x':  # 海の場合埋め立てを行う
                field[height_i][width_i] = 'o'

                # 島の数を検索
                field_for_search = copy.deepcopy(field)  # 検索用にテーブルの別オブジェクトを作成する
                number_of_islands = 0  # 島の数
                for height_j in range(10):
                    for width_j in range(10):
                        if field_for_search[height_j][width_j] == 'o':
                            dfs(width_j, height_j, field_for_search)  # Pythonでmutableなオブジェクトは参照渡しとなる
                            number_of_islands += 1

                # print("There are " + str(number_of_islands) + " islands!")

                field[height_i][width_i] = 'x'  # 埋め立てた場所をもとに戻す

                if number_of_islands == 1:
                    print('YES')
                    return
    print('NO')
```

#### 参考：Pythonのリストは参照渡し

- [\[Python\] リストの複製、浅いコピーと深いコピー](https://webbibouroku.com/Blog/Article/post-1558#outline__3)

``` Python
import copy

def append_triangle(list):
    list.append("△")

def solve():
    my_list = ["o", "x"]
    append_triangle(my_list)  # Mutableオブジェクトは参照渡しなので、my_listが変更される
    print(my_list)  # ['o', 'x', '△']

    new_my_list = copy.deepcopy(my_list)
    append_triangle(new_my_list)

    print(my_list)  # ['o', 'x', '△']
    print(new_my_list)  # ['o', 'x', '△', '△']
```

### [ARC 037 B バウムテスト　(見た目は違いますが実装するアルゴリズムは似ています)](https://atcoder.jp/contests/arc037/tasks/arc037_b)


// TODO

#### 参考

https://qiita.com/saba/items/affc94740aff117d2ca9#%E4%BE%8B%E9%A1%8C-2-1-3%E8%BF%B7%E8%B7%AF%E3%81%AE%E6%9C%80%E7%9F%AD%E8%B7%AF