S = input()
num_lower, num_upper = 0, 0
for s in S:
    if ord("a") <= ord(s) <= ord("z"):
        num_lower += 1
    else:
        num_upper += 1
print(S.upper() if num_lower < num_upper else S.lower())
