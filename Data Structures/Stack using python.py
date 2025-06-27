class stack():
    stack_list=[]
    def __init__(self, size):
        self.top=-1
        self.size=size
    def is_empty():
        if self.top == -1:
            print("stack is empty")
    def is_full():
        if self.top == size-1:
            print("stack is full")
    def push(self, value):
        if self.top == self.size-1:
            print("Stack overflow")
        else:
            self.stack_list.append(value)
            self.top+=1
            print(f"{value} inserted inside the stack")
    def pop(self):
        if self.top == -1:
            print("stack undeflow")
        else:
            self.stack_list.pop()
            self.top-=1
            print("element poped")
    def display(self):
        print(self.stack_list)
        
        
stack_object=stack(5)
while True:
    choice=int(input("1.push 2.pop 3.display 4.exit:"))
    print()
    if choice == 1:
        order=input("Enter your order: ")
        stack_object.push(order)
    elif choice == 2:
        stack_object.pop()
    elif choice == 3:
        stack_object.display()
    elif choice == 4:
        print("exited the menu")
        break
    else:
        print("invalid input")
    
    
