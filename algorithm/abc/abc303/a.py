N = int(input())
S = input()
T = input()
flag = True
for i in range(N):
    if S[i] != T[i] and {S[i], T[i]} != {"1", "l"} and {S[i], T[i]} != {"0", "o"}:
        flag = False
print("Yes" if flag else "No")
