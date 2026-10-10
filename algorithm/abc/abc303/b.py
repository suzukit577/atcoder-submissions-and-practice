from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
comb = set(combinations(A[0], 2))
for i in range(M):
    for j in range(N - 1):
        comb.discard((A[i][j], A[i][j + 1]))
        comb.discard((A[i][j + 1], A[i][j]))
print(len(comb))
