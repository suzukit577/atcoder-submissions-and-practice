N = int(input())
S = input()
t = S.count("T")
a = S.count("A")
if t > a:
    print("T")
elif a > t:
    print("A")
else:
    tt = 0
    aa = 0
    for i in range(N):
        if S[i] == "T":
            tt += 1
        if S[i] == "A":
            aa += 1
        if tt == t:
            print("T")
            exit()
        if aa == a:
            print("A")
            exit()
