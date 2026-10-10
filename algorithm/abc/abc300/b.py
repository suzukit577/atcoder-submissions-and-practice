def eqaul_matrix(A, B):
    H, W = len(A), len(A[0])
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True


def left_shift_matrix(A):
    H, W = len(A), len(A[0])
    for i in range(H):
        A[i] = A[i][1:] + A[i][:1]


H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
for i in range(H):
    A = A[1:] + A[:1]
    for j in range(W + 1):
        if eqaul_matrix(A, B):
            print("Yes")
            exit()
        left_shift_matrix(A)
print("No")
