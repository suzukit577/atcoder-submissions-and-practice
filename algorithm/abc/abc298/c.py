from collections import defaultdict

N = int(input())
Q = int(input())
q2 = defaultdict(list)  # 箱 i に入っているカードを表す辞書型
q3 = defaultdict(set)  # カード i が入っている箱を表す辞書型

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i = query[1]
        j = query[2]
        q2[j].append(i)  # 箱 j にカード i を追加
        q3[i].add(j)  # カード i を箱 j に追加
    elif query[0] == 2:
        i = query[1]
        print(*sorted(q2[i]))
    elif query[0] == 3:
        i = query[1]
        print(*sorted(list(q3[i])))
