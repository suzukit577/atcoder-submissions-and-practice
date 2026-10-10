N, D = map(int, input().split())
S = input()
print(min(len(S), S.count(".") + D))
