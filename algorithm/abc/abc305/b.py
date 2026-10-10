dist = [0, 3, 4, 8, 9, 14, 23]
p, q = input().split()
if p > q:
    p, q = q, p
p_num = ord(p) - ord("A")
q_num = ord(q) - ord("A")
print(dist[q_num] - dist[p_num])
