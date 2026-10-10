# 別解 (三平方の定理)
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
sqlen_ab, sqlen_bc, sqlen_ca = (
    (xb - xa) ** 2 + (yb - ya) ** 2,
    (xc - xb) ** 2 + (yc - yb) ** 2,
    (xa - xc) ** 2 + (ya - yc) ** 2,
)
if (
    sqlen_ab == sqlen_bc + sqlen_ca
    or sqlen_bc == sqlen_ca + sqlen_ab
    or sqlen_ca == sqlen_ab + sqlen_bc
):
    print("Yes")
else:
    print("No")
