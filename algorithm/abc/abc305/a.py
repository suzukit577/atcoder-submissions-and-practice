N = int(input())
if N >= 98:
    print(100)
elif N % 5 <= 2:
    print(5 * (N // 5))
elif N % 5 >= 3:
    print(5 * (N // 5 + 1))
