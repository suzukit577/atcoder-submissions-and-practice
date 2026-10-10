S = input()
T = input()
cnt_S_at = S.count("@")
cnt_T_at = T.count("@")
alphabets = "abcdefghijklmnopqrstuvwxyz"
reps = "atcoder"
for alphabet in alphabets:
    cnt_S = S.count(alphabet)
    cnt_T = T.count(alphabet)
    if cnt_S > cnt_T:
        if alphabet in reps and cnt_T_at > 0 and cnt_S - cnt_T <= cnt_T_at:
            cnt_T_at -= 1
        else:
            print("No")
            exit()
    elif cnt_T > cnt_S:
        if alphabet in reps and cnt_S_at > 0 and cnt_T - cnt_S <= cnt_S_at:
            cnt_S_at -= 1
        else:
            print("No")
            exit()
print("Yes")
