N, M = map(int, input().split())
K, A = [0] * N, [[] * N for _ in range(N)]
foods = set()
for i in range(N):
    input_list = list(map(int, input().split()))
    K[i], A[i] = input_list[0], set(input_list[1:])
    foods |= A[i]

for i in range(N):
    foods &= A[i]
print(len(foods))
