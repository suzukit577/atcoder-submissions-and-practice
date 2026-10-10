N = int(input())
S = []
A = []
for _ in range(N):
    s, a = input().split()
    a = int(a)
    S.append(s)
    A.append(a)
n = A.index(min(A))
for i in range(n, N):
    print(S[i])
for i in range(n):
    print(S[i])
