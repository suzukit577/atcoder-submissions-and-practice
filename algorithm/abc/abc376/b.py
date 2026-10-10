N, Q = map(int, input().split())
l, r = 1, 2
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == "L":
        if l < r < T or T < r < l:
            ans += N - abs(T - l)
        else:
            ans += abs(T - l)
        l = T
    else:
        if r < l < T or T < l < r:
            ans += N - abs(T - r)
        else:
            ans += abs(T - r)
        r = T
print(ans)
