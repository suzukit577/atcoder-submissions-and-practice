from collections import defaultdict

N = int(input())
cnt_dict = defaultdict(int)
for _ in range(N):
    cnt_dict[input()] += 1
M = int(input())
for _ in range(M):
    cnt_dict[input()] -= 1
max_value = max(cnt_dict.values())
print(max_value if max_value >= 0 else 0)
