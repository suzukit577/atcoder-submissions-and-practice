def is_palindrome(s1: str, s2: str) -> bool:
    s = s1 + s2
    if s == "".join(reversed(s)):
        return True
    else:
        return False


N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if is_palindrome(S[i], S[j]) or is_palindrome(S[j], S[i]):
            print("Yes")
            exit()
print("No")
