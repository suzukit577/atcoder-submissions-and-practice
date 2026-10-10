N, D = map(int, input().split())
S = list(input())
cnt = 0
for i in range(N - 1, -1, -1):
    if cnt < D and S[i] == "@":
        S[i] = "."
        cnt += 1
print("".join(S))
