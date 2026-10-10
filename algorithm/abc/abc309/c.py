# def solve(N, K, prescriptions):
#     left = 1  # 初日
#     right = 10**18  # 十分に大きな値で初期化
#     while left < right:
#         mid = (left + right) // 2  # 二分探索で日数を求める
#         required = 0
#         for a, b in prescriptions:
#             if a >= mid:
#                 required += b
#         if required <= K:
#             right = mid
#         else:
#             left = mid + 1
#     return left

# # 入力を受け取る
# N, K = map(int, input().split())
# prescriptions = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     prescriptions.append((a, b))
# # 解法を呼び出して結果を出力
# result = solve(N, K, prescriptions)
# print(result)
