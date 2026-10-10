# 別解 - 問題文に記述されている操作の実装
N, K = map(int, input().split())
K -= 1  # 0-indexed にする
S = input()
l = [i for i in range(N) if S[i] == "1" and (i == 0 or S[i - 1] == "0")]
r = [i for i in range(N) if S[i] == "1" and (i == N - 1 or S[i + 1] == "0")]
T = list(S)
for i in range(r[K - 1] + 1, r[K - 1] + (r[K] - l[K]) + 2):
    T[i] = "1"
for i in range(r[K - 1] + (r[K] - l[K]) + 2, r[K] + 1):
    T[i] = "0"
print("".join(T))
