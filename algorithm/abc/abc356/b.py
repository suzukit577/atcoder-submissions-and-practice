N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
get = [0] * M
for i in range(N):
    for j in range(M):
        get[j] += X[i][j]
for i in range(M):
    if get[i] < A[i]:
        print("No")
        break
else:
    print("Yes")
