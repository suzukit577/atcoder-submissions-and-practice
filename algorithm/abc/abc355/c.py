def check_bingo(r, c, diag1, diag2, N):
    if r == N:
        return True
    if c == N:
        return True
    if diag1 == N or diag2 == N:
        return True
    return False


N, T = map(int, input().split())
A = list(map(int, input().split()))
row, col = [0] * N, [0] * N
diag1, diag2 = 0, 0

for i in range(T):
    r = (A[i] - 1) // N
    c = (A[i] - 1) % N
    row[r] += 1
    col[c] += 1
    if r == c:
        diag1 += 1
    if r + c == N - 1:
        diag2 += 1
    if check_bingo(row[r], col[c], diag1, diag2, N):
        print(i + 1)
        break
else:
    print(-1)
