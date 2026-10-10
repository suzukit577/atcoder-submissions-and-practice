A, B = map(int, input().split())
if A == 3 or A == 6:
    print("No")
else:
    if B == A + 1:
        print("Yes")
    else:
        print("No")
