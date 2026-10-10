K, N = map(int, input().split())
A = list(map(int, input().split()))
dist_list = [A[i + 1] - A[i] for i in range(N - 1)]
dist_list.append(A[0] - A[-1] + K)
print(K - max(dist_list))
