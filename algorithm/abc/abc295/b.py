import copy

r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
ans = copy.deepcopy(b)
bomb = set([f"{i}" for i in range(10)])
for i in range(r):
    for j in range(c):
        if b[i][j] in bomb:
            bi = int(b[i][j])
            for k in range(bi + 1):
                for l in range(bi - k + 1):
                    if i - k >= 0 and j - l >= 0:
                        ans[i - k][j - l] = "."
                    if i - k >= 0 and j + l <= c - 1:
                        ans[i - k][j + l] = "."
                    if i + k <= r - 1 and j - l >= 0:
                        ans[i + k][j - l] = "."
                    if i + k <= r - 1 and j + l <= c - 1:
                        ans[i + k][j + l] = "."
for i in range(r):
    for j in range(c):
        print(ans[i][j], end="")
    print()
