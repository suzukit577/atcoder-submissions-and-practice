a, b = map(int, input().split())
negative_cnt = 0
if a * b < 0:
    print("Zero")
    exit()
for i in range(a, b + 1):
    if i < 0:
        negative_cnt += 1
print("Positive" if negative_cnt % 2 == 0 else "Negative")
