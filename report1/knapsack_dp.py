from utils import *
import argparse

# 0-1ナップザック問題に関するDP
def knapsack_dp(N,W,w,v):
    start_time = time.time()
    # 次使用する配列に今回の結果を残すので+1している
    dp = [[0]*(W+1) for i in range(N+1)] # DPの配列作成

    for i in range(N):
        for j in range(W+1):
            if j < w[i]: # この時点では許容量を超えていないので選択しない
                dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
    end_time = time.time()
    time_exec = end_time - start_time
    return dp[N][W],round(time_exec,10)

# 部分集和問題に関するDP
def subset_dp(N,W,w):
    start_time = time.time()
    # 次使用する配列に今回の結果を残すので+1している
    dp = [[0]*(W+1) for i in range(N+1)] # DPの配列作成

    for i in range(N):
        for j in range(W+1):
            if j < w[i]: # この時点では許容量を超えていないので選択しない
                dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+w[i])

    end_time = time.time()
    time_exec = end_time - start_time
    return dp[N][W],round(time_exec,10)



