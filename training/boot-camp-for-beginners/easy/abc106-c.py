S = input()
K = int(input())
for i in range(len(S)):
    num = int(S[i])
    if num != 1 and i < K:
        print(num)
        break
else:
    print(1)
