N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N - 1):
    diff = abs(A[i + 1] - A[i])
    if diff != 1:
        if A[i + 1] > A[i]:
            ans += [A[i] + j for j in range(diff)]
        elif A[i + 1] < A[i]:
            ans += [A[i] - j for j in range(diff)]
    else:
        ans.append(A[i])
ans.append(A[-1])
print(*ans)
