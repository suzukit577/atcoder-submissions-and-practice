N, K = map(int, input().split())
A = list(map(int, input().split()))[::-1]
emp_seat = K
ans = 0
while len(A) != 0:
    if emp_seat >= A[-1]:
        emp_seat -= A[-1]
        A.pop()
    else:
        emp_seat = K
        ans += 1
print(ans + 1)
