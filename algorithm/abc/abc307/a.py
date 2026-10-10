N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(sum(A[7 * i : 7 * (i + 1)]))
print(*ans)
