N = int(input())
cards = []
for i in range(N):
    A, C = map(int, input().split())
    cards.append((A, C, i + 1))
cards.sort(key=lambda x: x[0])

stack = []
for card in cards:
    while stack and stack[-1][1] > card[1]:
        stack.pop()
    stack.append(card)

ans = [card[2] for card in stack]
print(len(ans))
print(*sorted(ans))
