S = input()
N = len(S)
last, now, ans = "", "", 0
for s in S:
    now += s
    if now == last:
        continue
    last, now = now, ""
    ans += 1
print(ans)
