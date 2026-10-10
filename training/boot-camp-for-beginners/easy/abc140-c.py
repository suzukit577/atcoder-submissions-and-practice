N = int(input())
B = list(map(int, input().split()))
A = [0] * N
for i in range(N - 1):
    A[i], A[i + 1] = B[i], B[i]
    if i > 0 and A[i] > B[i - 1]:
        A[i] = B[i - 1]
print(sum(A))
