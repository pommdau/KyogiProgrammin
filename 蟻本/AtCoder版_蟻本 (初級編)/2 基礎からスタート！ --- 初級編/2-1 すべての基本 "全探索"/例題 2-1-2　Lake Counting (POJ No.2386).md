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

