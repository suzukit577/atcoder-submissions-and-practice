# 別解
N, K = map(int, input().split())
S = input()
ans, i = 0, 0
while i < N:
    if S[i] == "O":
        for j in range(i, i + K):
            if j == N or S[j] == "X":
                i = j
                break
        else:
            ans += 1
            i += K
    else:
        i += 1
print(ans)
