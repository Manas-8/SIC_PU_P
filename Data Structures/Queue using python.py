class queue:
    queue_list=[]
    def __init__(self, size):
        self.size=size
        self.front=-1
        self.rear=-1

    def add(self, value):
        if self.front == self.size-1:
            print("queue is full")
        else:
            self.queue_list.append(value)
            self.front+=1
            print(f'{value} inserted at the front')
    
    def delete(self):
        if self.front == self.rear:
            print("queue is empty")
        else:
            self.queue_list.pop(self.rear)
            self.rear+=1
            print('value deleted from rear')
    def display(self):
        print(self.queue_list)

queue_obj=queue(4)
while True:
    print("1.insert 2.delete 3.display 4.exit")
    choice = int(input('Enter your choice: '))
    if choice == 1:
        value=int(input('Enter the value you want to insert: '))
        queue_obj.add(value)
    elif choice == 2:
        queue_obj.delete()
    elif choice == 3:
        queue_obj.display()
    elif choice == 4:
        print("exiting the program")
        break
    else:
        print("invalid input")
