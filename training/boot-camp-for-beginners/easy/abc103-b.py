S = input()
T = input()
N = len(S)
S *= 2
for i in range(N):
    if S[i : i + N] == T:
        print("Yes")
        break
else:
    print("No")
