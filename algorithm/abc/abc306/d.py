N = int(input())
# dp[i][j]:
# 料理 i までの料理を食べるか下げてもらうか選択した時に，高橋くんの状態が j (0...高橋くんがお腹を壊していない，1...高橋くんがお腹を壊している) である時の，食べた料理の美味しさの総和の最大値
dp = [[-float("inf"), -float("inf")] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    X, Y = map(int, input().split())
    dp[i + 1][0] = dp[i][0]  # 食べない時
    dp[i + 1][1] = dp[i][1]  # 食べない時
    if X == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + Y, dp[i][1] + Y)
    else:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + Y)
print(max(dp[-1]))
