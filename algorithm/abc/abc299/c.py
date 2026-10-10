def rle(s: str) -> list:
    """Run Length Encoding: O(n)

    Args:
        s (str): str

    Returns:
        list: list of tuple which elements are character in given string and number of it
    """
    n = len(s)
    ans = []  # 圧縮後のリスト
    l = 0  # 始点
    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:  # 異なる文字になるまで進む
            r += 1
        ans.append((s[l], r - l))  # 文字, 連続する個数
        l = r  # 連続しなかった文字から探索を開始
    return ans


from itertools import groupby

n = int(input())
s = input()
if "o" not in s or "-" not in s:
    print(-1)
else:
    # rle_list = [(k, len(list(g))) for k, g in groupby(s)]
    rle_list = rle(s)
    ans = []
    for t in rle_list:
        if t[0] == "o":
            ans.append(t[1])
    print(max(ans))
