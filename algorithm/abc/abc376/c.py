N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
for i in range(N - 1):
    if A[i + 1] > B[i]:
        print(-1)
        break
else:
    for i in range(N - 1):
        if A[i] > B[i]:
            print(A[i])
            break
    else:
        print(A[-1])
