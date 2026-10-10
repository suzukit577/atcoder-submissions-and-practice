a, b = map(int, input().split())
ans = 0
while a != b:
    n = 0
    if a % b == 0:
        n = a // b - 1
        a -= n * b
    elif b % a == 0:
        n = b // a - 1
        b -= n * a
    elif a > b and a != 1 and b != 1:
        n = a // b
        a -= n * b
    elif a < b and a != 1 and b != 1:
        n = b // a
        b -= n * a
    elif a == 1:
        n = b - 1
        b = 1
    elif b == 1:
        n = a - 1
        a = 1
    ans += n
print(ans)
