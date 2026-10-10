A, B, C, X, Y = map(int, input().split())
if A + B > 2 * C:
    print(
        min(
            2 * C * max(X, Y), 2 * C * min(X, Y) + A * max(X - Y, 0) + B * max(Y - X, 0)
        )
    )
else:
    print(A * X + B * Y)
