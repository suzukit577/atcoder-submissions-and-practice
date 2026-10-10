H = int(input())
ans = 0
for i in range(10**6):
    ans += 2**i
    H //= 2
    if H <= 0:
        break
print(ans)
