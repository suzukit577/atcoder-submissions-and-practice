def ceil_to_10_multiplier(n: int) -> int:
    if n % 10 == 0:
        return n
    else:
        return (n // 10 + 1) * 10


food = list()
for _ in range(5):
    food.append(int(input()))
rem = list(map(lambda x: x % 10, food))
min_rem = 10
for r in rem:
    if r != 0 and r < min_rem:
        min_rem = r
if min_rem == 10:
    min_rem = 0
id = rem.index(min_rem)

ans = 0
for i in range(5):
    if i == id:
        ans += food[i]
    else:
        ans += ceil_to_10_multiplier(food[i])
print(ans)
