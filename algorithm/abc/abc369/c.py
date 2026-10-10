N = int(input())
A = list(map(int, input().split()))
ans, left, right = N, 0, 0
while left < N - 1:
    if right < N - 1 and (
        left == right or A[right + 1] - A[right] == A[left + 1] - A[left]
    ):
        right += 1
        ans += (
            right - left
        )  # 左端を A[left] に固定し、右端として A[left + 1], ..., A[right] のいずれかを選んで得られる部分列の個数
    else:
        left += 1
print(ans)
