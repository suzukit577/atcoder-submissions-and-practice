X = input()
if set(X[X.index(".") + 1 :]) == {"0"}:
    X = X[: X.index(".")]
else:
    i = len(X) - 1
    while X[i] == "0":
        i -= 1
    X = X[: i + 1]
print(X)
