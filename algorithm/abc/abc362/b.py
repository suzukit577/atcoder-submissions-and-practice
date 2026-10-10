def inner_product(a: list[int], b: list[int]) -> int:
    res, N = 0, len(a)
    for i in range(N):
        res += a[i] * b[i]
    return res


xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

vec_ab, vec_ac = [xb - xa, yb - ya], [xc - xa, yc - ya]
vec_bc, vec_ba = [xc - xb, yc - yb], [xa - xb, ya - yb]
vec_ca, vec_cb = [xa - xc, ya - yc], [xb - xc, yb - yc]

if (
    inner_product(vec_ab, vec_ac) == 0
    or inner_product(vec_bc, vec_ba) == 0
    or inner_product(vec_ca, vec_cb) == 0
):
    print("Yes")
else:
    print("No")
