# Biggest digit in a number
number=input("Enter the number: ")
current_max=int(number[0])
for i in number:
    if int(i)>current_max:
        current_max=int(i)

print(f"the biggest digit is {current_max}")



# Find 2nd smallest digit in a number
number = input("Enter the number: ")
smallest = 10
second_smallest = 10

for i in number:
    digit = int(i)
    if digit < smallest:
        second_smallest = smallest
        smallest = digit
    elif smallest < digit < second_smallest:
        second_smallest = digit

if second_smallest == 10:
    print("No second smallest digit exists.")
else:
    print("Second smallest digit:", second_smallest)


# Print the Prime numbers in decreasing order between m and n (m < n)
lower_number=int(input("Enter lower number: "))
higher_number=int(input("Enter higher number: "))
prime_numbers=[]
for i in range(lower_number, higher_number+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        prime_numbers.append(i)
        
prime_numbers.reverse()
print(prime_numbers)



# Count the number of prime numbers
number=input("Enter the number: ")
count=0
for i in number:
    if int(i) in [2, 3, 5, 7]:
        count+=1
    
print(count)


# Fibonacci
number=int(input("Enter the number: "))
list1=[1, 2]
for i in range(2, number):
    fibonacci=list1[i-1]+list1[i-2]
    list1.append(fibonacci)
    
print(list1)

# series
n=int(input("Enter the number for 1 to 4: "))
m=int(input("Enter the number for 2 to 10: "))
sign=-1
sum=0
denominator=-1
for i in range(m):
    numerator=n**(2**i)
    denominator=denominator+2
    sign=(-1) * sign
    terms=numerator/denominator * sign
    sum=sum+terms
    
print(sum)




# Find sum of the Even placed digits in the given number.
number=input("Enter the number: ")
count = 0
sum = 0
for i in number:
    count += 1
    if count % 2 == 1:
        continue
    else:
        sum = sum + int(i)

print(f"the sum of even placed digits is {sum}")

# Find sum of the Odd placed digits in the given number.
number=input("Enter the number: ")
count = 1
sum = 0
for i in number:
    count += 1
    if count % 2 == 1:
        continue
    else:
        sum = sum + int(i)

print(f"the sum of even placed digits is {sum}")


