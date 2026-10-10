H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
row_counts = [row.count("#") for row in S]
column_counts = [sum(S[i][j] == "#" for i in range(H)) for j in range(W)]
row_counts = [float("inf") if x == 0 else x for x in row_counts]
column_counts = [float("inf") if x == 0 else x for x in column_counts]
ans_row = row_counts.index(min(row_counts)) + 1
ans_col = column_counts.index(min(column_counts)) + 1
print(ans_row, ans_col)
