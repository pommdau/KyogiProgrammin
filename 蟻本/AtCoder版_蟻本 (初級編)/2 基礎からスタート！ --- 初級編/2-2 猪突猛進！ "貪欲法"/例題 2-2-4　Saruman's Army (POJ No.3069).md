## [例題 2\-2\-4　Saruman's Army \(POJ No\.3069\)](https://qiita.com/drken/items/e77685614f3c6bf86f44#%E4%BE%8B%E9%A1%8C-2-2-4sarumans-army-poj-no3069)
### 本書

``` Python
def solve():
    number_of_points = int(input())
    distance = int(input())
    position_of_points = list(map(int, input().split()))

    point_i = 0
    answer = 0

    while point_i < number_of_points:
        left_position = position_of_points[point_i]

        while point_i < number_of_points and position_of_points[point_i] <= left_position + distance:
            point_i += 1

        middle_position = position_of_points[point_i - 1]

        # 右の点
        while point_i < number_of_points and position_of_points[point_i] <= middle_position + distance:
            point_i += 1

        # right_position = position_of_points[point_i - 1]  # 次の点の探索はright_positionの右の点から始まる

        answer += 1
```

```sh
6
10
1 7 15 20 30 50
```

### [ABC 083 C Multiple Gift　(例題はなるべく遠い方を選ぶ Greedy でしたが、これは近い方を選ぶ Greedy です)](https://atcoder.jp/contests/abc083/tasks/arc088_a)

``` Python
def solve():
    min_number, max_number = list(map(int, input().split()))

    current_number = min_number
    answer = 0

    while current_number <= max_number:
        answer += 1
        current_number = current_number * 2

    print(answer)
```

### [ARC 006 C 積み重ね　(典型問題です)](https://atcoder.jp/contests/arc006/tasks/arc006_3)

- 順序によっては例とできる山が違うことがあるが、結果は同じなので山の数には影響しない

``` Python
TOP_INDEX = 0  # 山の一番上を示すインデックス


def solve():
    number_of_boxes = int(input())
    boxes = [int(input()) for _ in range(number_of_boxes)]  # 各箱の重さリスト

    pile_of_boxes_list = []  # 全てのダンボールの山

    for box in boxes:

        position = -1  # 箱を置く場所

        for pile_i, pile_of_boxes in enumerate(pile_of_boxes_list):
            if box <= pile_of_boxes[TOP_INDEX]:  # 既存の山の上に置ける場合
                if position == -1:  # 初回に見つかった場合は条件無しで採用
                    position = pile_i
                elif pile_of_boxes_list[pile_i][TOP_INDEX] < pile_of_boxes_list[position][TOP_INDEX]:  # 可能な限り軽い箱の上に置く
                    position = pile_i

        if position == -1:  # 置ける箱がなかった場合は新たに山を作る
            pile_of_boxes_list.append([box])
        else:  # 箱を先頭に配置する
            pile_of_boxes_list[position].insert(TOP_INDEX, box)

    # print(pile_of_boxes_list)  # for debug
    print(len(pile_of_boxes))
```

### [ABC 005 C おいしいたこ焼きの売り方　(少し難しくなった Greedy です、Greedy に解けるマッチングの例です)](https://atcoder.jp/contests/abc005/tasks/abc005_3)

``` Python
# 方針：可能な限り古いたこ焼きを提供する。但しT秒以内のもの
def solve():
    limit_wating_time = int(input())  # 指定秒数以内にたこ焼きを売る
    number_of_lot = int(input())  # たこ焼きができる回数
    takoyakis_time = list(map(int, input().split()))  # たこ焼きの完成時間
    number_of_users = int(input())
    users_time = list(map(int, input().split()))  # お客さんが来る時間

    for user_time in users_time:
        can_sell = False  # 現在のお客さんにたこ焼きを売れたかどうかのフラグ
        for takoyaki_i, takoyaki_time in enumerate(takoyakis_time):
            duration = user_time - takoyaki_time   # たこ焼きが焼き上がってからお客が来るまでの経過時間
            if 0 <= duration <= limit_wating_time:  # たこ焼きを売れる場合
                del takoyakis_time[takoyaki_i]
                can_sell = True
                break

        if not can_sell:  # たこ焼きが売れなかった場合
            print('no')
            return

    print('yes')
```

### [ABC 091 C 2D Plane 2N Points　(二次元量同士を比較する最大二部マッチング、Greedy に解けるマッチング例です)](https://atcoder.jp/contests/abc091/tasks/arc092_a)
- 解説を参照
    - https://img.atcoder.jp/arc092/editorial.pdf

``` Python
X_INDEX = 0
Y_INDEX = 1


def solve():
    number_of_balls = int(input())
    red_points = [list(map(int, input().split())) for _ in range(number_of_balls)]
    blue_points = [list(map(int, input().split())) for _ in range(number_of_balls)]

    from operator import itemgetter
    blue_points.sort(key=itemgetter(X_INDEX))  # 青玉をx座標の昇順でソート
    red_points.sort(key=itemgetter(Y_INDEX), reverse=True)  # 赤玉をy座標の降順でソート

    # 青玉：x座標の小さいものからペアを作っていく
    # 赤玉：青玉のx座標よりも小さいものの中で、y座標が最大のものをペアとする
    number_of_pairs = 0  # 仲良しペアの数
    used_red_points = [False for _ in range(number_of_balls)]  # 使用済み赤玉情報
    # used_blue_points = [False for _ in range(number_of_balls)]  # 使用済み青玉情報
    for blue_i, blue_point in enumerate(blue_points):
        for red_i, red_point in enumerate(red_points):
            if red_point[X_INDEX] < blue_point[X_INDEX] and \
                    red_point[Y_INDEX] < blue_point[Y_INDEX] and \
                    not used_red_points[red_i]:
                number_of_pairs += 1
                used_red_points[red_i] = True
                break

    print(number_of_pairs)
```

## 例題 2-2-5　Fence Repair (POJ No.3253)
### 本書

``` Python
def solve():
    number_of_boards = int(input())
    board_length_list = list(map(int, input().split()))
    total_cost = 0

    # 分割予定の板を小さい順に結合していく
    # 板が1本になるまで適用
    while len(board_length_list) > 1:
        board_length_list.sort()

        # それらを併合
        new_board_length = board_length_list[0] + board_length_list[1]
        total_cost += new_board_length

        del board_length_list[0:2]
        board_length_list.insert(0, new_board_length)

    print(total_cost)
```

- `input`

```sh
3
8 5 8
```

```sh
5
3 4 5 1 2
```
