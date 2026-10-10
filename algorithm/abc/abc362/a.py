prices = list(map(int, input().split()))
C = input()
if C == "Red":
    print(min(prices[1:]))
if C == "Green":
    print(min(prices[0], prices[2]))
if C == "Blue":
    print(min(prices[:2]))
