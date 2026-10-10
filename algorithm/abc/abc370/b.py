N = int(input())
A = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
current = 0
for i in range(N):
    if current >= i:
        current = A[current][i]
    else:
        current = A[i][current]
print(current + 1)
