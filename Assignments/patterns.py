def right_angled_triangle(n):
    print("Right Angled Triangle")
    for i in range(1, n+1):
        print('*' * i)
    print()

def equilateral_triangle(n):
    print("Equilateral Triangle")
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    print()

def hollow_square(n):
    print("Hollow Square")
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n-2) + '*')
    print()

def hollow_rhombus(n):
    print("Hollow Rhombus")
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
    print()

def x_shape(n):
    print("X Shape")
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

def x_in_hollow_square(n):
    print("X Shape Inside Hollow Square")
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

# pascals traingle
def pascal_triangle(n):
    """Prints Pascal's Triangle with n rows"""
    for row in range(1, n + 1):
        value = 1  # First value in each row is always 1
        print(" " * (n - row), end="")  # Leading spaces for pyramid shape
        
        for i in range(1, row + 1):
            print(value, end=" ")
            value = value * (row - i) // i  # Calculate next value
            
        print()  # New line after each row

# Example usage:
num_rows = 5
print(f"Pascal's Triangle with {num_rows} rows:")
pascal_triangle(num_rows)



# Set the size
size = 7

# Call all pattern functions
right_angled_triangle(size)
equilateral_triangle(size)
hollow_square(size)
hollow_rhombus(size)
x_shape(size)
x_in_hollow_square(size)
