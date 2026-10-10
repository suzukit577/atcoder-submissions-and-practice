S = set(input())
alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
for a in alphabet:
    if a not in S:
        print(a)
        break
else:
    print("None")
