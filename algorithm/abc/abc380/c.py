# submit
N, K = map(int, input().split())
S = input()
ones_blocks = []
i = 0
while i < N:
    if S[i] == "1":
        start = i
        while i < N and S[i] == "1":
            i += 1
        end = i - 1
        ones_blocks.append((start, end))
    else:
        i += 1
k_minus_1_block = ones_blocks[K - 2]
k_block = ones_blocks[K - 1]
ans = list(S)
for i in range(k_block[0], k_block[1] + 1):
    ans[i] = "0"
for i in range(k_block[1] - k_block[0] + 1):
    ans[k_minus_1_block[1] + 1 + i] = "1"
print("".join(ans))
