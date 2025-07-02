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
