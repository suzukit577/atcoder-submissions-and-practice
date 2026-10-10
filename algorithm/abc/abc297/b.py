s = input()
flag = True
b = []
r = []
k = 0
for i in range(len(s)):
    if s[i] == "B":
        b.append(i)
    if s[i] == "R":
        r.append(i)
    if s[i] == "K":
        k = i
if (b[1] - b[0]) % 2 == 0 or k <= r[0] or r[1] <= k:
    flag = False
print("Yes" if flag else "No")
