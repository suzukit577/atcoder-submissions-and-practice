N = int(input())
A = [0]
counts = [0] * 200001
for _ in range(N):
    a = int(input())
    A.append(a)
    counts[a] += 1
max_num = max(A)
for i in range(1, N + 1):
    if A[i] == max_num and counts[max_num] == 1:
        for j in range(max_num - 1, 0, -1):
            if counts[j] != 0:
                print(j)
                break
    else:
        print(max_num)
