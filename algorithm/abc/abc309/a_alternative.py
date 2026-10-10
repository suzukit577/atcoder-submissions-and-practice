# 別解
# A, B が書かれたマスがそれぞれ上から何行目, 左から何列目にあるか求める
# A - 1 を 3 で割った際の商と余りが，A が書かれた行と列にそれぞれ対応
A, B = map(int, input().split())
ra, ca = (A - 1) // 3, (A - 1) % 3
rb, cb = (B - 1) // 3, (B - 1) % 3
print("Yes" if ra == rb and ca + 1 == cb else "No")
