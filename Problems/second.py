# Oranges Problem
number_of_oranges = 8
orange_sizes = [4, 3, 8, 6, 1, 1, 9, 5]
k = 0
for i in range(number_of_oranges):
    if orange_sizes[i] <= orange_sizes[number_of_oranges - 1]:
        orange_sizes[i], orange_sizes[k] = orange_sizes[k], orange_sizes[i]
        k+=1
orange_sizes[k], orange_sizes[number_of_oranges - 1], orange_sizes[number_of_oranges - 1], orange_sizes[k]

print(orange_sizes)


#Harry Potter problem
def harry_potter_stone():
    n = int(input())
    coins = list(map(int, input().split()))
    q, x = map(int, input().split())
    instructions = [input().strip() for _ in range(q)]

    stack = []
    index = 0
    total = 0

    for ins in instructions:
        if ins == "Harry":
            if index < n:
                coin = coins[index]
                stack.append(coin)
                total += coin
                index += 1
        elif ins == "Remove":
            if stack:
                total -= stack.pop()

        if total == x:
            print(len(stack))
            return

    print(-1)


#captain tsubasa
T = int(input())
for _ in range(T):
    parts = input().split()
    N = int(parts[0])
    current = int(parts[1])
    history = []

    for _ in range(N):
        command = input().split()
        if command[0] == 'P':
            history.append(current)
            current = int(command[1])
        elif command[0] == 'B':
            current = history.pop()
    print("Player", current)

