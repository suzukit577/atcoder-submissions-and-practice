n = int(input())
w = list(input().split())
W = set(["and", "not", "that", "the", "you"])
flag = False
for i in range(n):
    if w[i] in W:
        flag = True
print("Yes" if flag else "No")
