#Queue using single linked list
class SLLNode:
    def __init__(self, data, nxt=None):
        self.data, self.next = data, nxt

class QueueSLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        node = SLLNode(val)
        if not self.front:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise IndexError("dequeue from empty queue")
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val



#Queue with double linked list
class DLLNode:
    def __init__(self, data, prev=None, nxt=None):
        self.data, self.prev, self.next = data, prev, nxt

class QueueDLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        node = DLLNode(val, prev=self.rear)
        if self.rear:
            self.rear.next = node
        else:
            self.front = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            raise IndexError("dequeue from empty queue")
        val = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return val


#stack using single linked list
class StackSLL:
    def __init__(self):
        self.head = None

    def push(self, val):
        self.head = SLLNode(val, self.head)

    def pop(self):
        if not self.head:
            raise IndexError("pop from empty stack")
        val = self.head.data
        self.head = self.head.next
        return val


#stack using double linked list
class StackDLL:
    def __init__(self):
        self.tail = None

    def push(self, val):
        node = DLLNode(val, prev=self.tail)
        if self.tail:
            self.tail.next = node
        self.tail = node

    def pop(self):
        if not self.tail:
            raise IndexError("pop from empty stack")
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return val


#reverse a single linked list
def reverse_sll(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev


#merge 2 sorted single linked list
def merge_sorted_sll(a, b):
    dummy = SLLNode(0)
    tail = dummy
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

