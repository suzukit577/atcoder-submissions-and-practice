def get_keys_from_value(d: dict, val) -> list:
    """get keys from vlue: O(n)

    Args:
        d (dict): dict
        val: value of d

    Returns:
        list: keys corresponding to given value
    """
    return [k for k, v in d.items() if v == val]


n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
d = dict()
if t in c:
    for i in range(n):
        if c[i] == t:
            d[i] = r[i]
    print(get_keys_from_value(d, max(d.values()))[0] + 1)
else:
    c0 = c[0]
    for i in range(n):
        if c[i] == c0:
            d[i] = r[i]
    print(get_keys_from_value(d, max(d.values()))[0] + 1)
