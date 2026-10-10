n = int(input())
s = input()
id_1 = 0
id_2 = 0
id_3 = 0
for i in range(n):
    if s[i] == "|" and id_1 == 0:
        id_1 = i + 1
    elif s[i] == "|" and id_1 != 0:
        id_2 = i + 1
    elif s[i] == "*":
        id_3 = i + 1
print("in" if id_1 < id_3 < id_2 else "out")
