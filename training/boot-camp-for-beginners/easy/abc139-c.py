N = int(input())
H = list(map(int, input().split()))
can_descend = [False] * N
for i in range(N):
    if i != N - 1 and H[i] >= H[i + 1]:
        can_descend[i] = True
cnt_list = []
for i in range(N):
    if i == 0:
        tmp_cnt = 0
    if can_descend[i] == True:
        tmp_cnt += 1
    else:
        cnt_list.append(tmp_cnt)
        tmp_cnt = 0
print(max(cnt_list))
