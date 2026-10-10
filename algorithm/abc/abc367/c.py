from itertools import product

N, K = map(int, input().split())
R = list(map(int, input().split()))
perm_list = list(product(*[range(1, r + 1) for r in R]))
filtered_perm_list = [perm for perm in perm_list if sum(perm) % K == 0]
filtered_perm_list.sort()
for perm in filtered_perm_list:
    print(" ".join(map(str, perm)))
