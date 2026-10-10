N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
cumsum_A = 0
cumsum_B = 0
for i in range(N):
    cumsum_A += A[i]
    cumsum_B += B[i]
    if cumsum_A > X or cumsum_B > Y:
        print(i + 1)
        break
else:
    print(N)
