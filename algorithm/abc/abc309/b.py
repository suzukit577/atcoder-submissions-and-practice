N = int(input())
A = [list(input()) for _ in range(N)]
a = A[0][: N - 1]
b = [A[i][N - 1] for i in range(N - 1)]
c = A[N - 1][1:]
d = [A[i][0] for i in range(1, N)]
A[0][1:] = a
for i in range(N - 1):
    A[i + 1][N - 1] = b[i]
A[N - 1][: N - 1] = c
for i in range(N - 1):
    A[i][0] = d[i]
for i in range(N):
    print("".join(A[i]))
