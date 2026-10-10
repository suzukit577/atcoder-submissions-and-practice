a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
intersected = (
    False if j <= a or k <= b or l <= c or d <= g or e <= h or f <= i else True
)
print("Yes" if intersected else "No")
