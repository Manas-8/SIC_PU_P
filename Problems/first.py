# the array division problem
total_size=int(input())
first_half=int(input())
second_half=int(input())
list1=list(map(int, input().split()))
list2=sorted(list1)
lower_limit=list2[first_half-1]
upper_limit=list2[first_half]
count=0
for i in range(lower_limit+1, upper_limit):
    count+=1

print(count)


# memory allocation problem
num_of_req=int(input())
list_req=list(map(int, input().split()))
memory_allocated=0
count=0
for i in list_req:
    if count % 2 == 0:
        if i > 0:
            memory_allocated+=i
        elif i == 0:
            continue
        else:
            memory_allocated-=i
    count+=1
    

print(f'the memory alocated by server 1 is {memory_allocated}') 


# reflection string problem
def is_same_reflection():
    string1=input()
    string2=input()
    if string1 == string2 or string1 == (string2[1:]+string2[:1]) or string1 == (string2[2:]+string2[:2]) or string1 == (string2[3:]+string2[:3]) or \
        string1 == (string2[4:]+string2[:4]) or string1 == (string2[5:]+string2[:5]):
        print(1)
    else:
        print(-1)

is_same_reflection()
