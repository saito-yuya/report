from utils import *
N = 3  # 荷物の数
W = 10  # ナップサックの許容量
w = [9, 6, 4] # 荷物それぞれの重さの配列
v = [15, 10, 6] # 荷物それぞれの価値の配列


# 0-1ナップザック問題に関するしらみつぶし法
def knapsack_bit(N, W, w, v):
    start_time = time.time()
    max_value = 0

    # ビット全探索
    for i in range(2**N):
        value = 0
        weight = 0

        # 各荷物について選択するかどうかを判断する
        for j in range(N):
            if (i >> j) & 1:
                weight += w[j]
                value += v[j]

        # 許容重量以下であれば最大値を更新する
        if weight <= W:
            max_value = max(max_value, value)
            # 終了時間を記録し、実行時間を表示
        end_time = time.time()
        time_exec = end_time - start_time

    return max_value,round(time_exec,10)

print(knapsack_bit(N,W,w,v))


# 部分集和問題に関するしらみつぶし法
def subset_bit(N, W, w):
    start_time = time.time()
    max_weight = 0

    # ビット全探索
    for i in range(2**N):
        weight = 0

        # 各荷物について選択するかどうかを判断する
        for j in range(N):
            if (i >> j) & 1:
                weight += w[j]

        # 許容重量以下であれば最大値を更新する
        if weight <= W:
            max_weight = max(max_weight, weight)
            # 終了時間を記録し、実行時間を表示
    end_time = time.time()
    time_exec = end_time - start_time

    return max_weight,round(time_exec,10)

