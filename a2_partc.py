# Main Author: Shailendra Zala
# Main Reviewer: Jeel Patel ,Maharshi Patel 

class Stack:
    def __init__(self, cap=10):
        self.items = [None] * cap
        self.size = 0
        self.cap = cap

    def capacity(self):
        return self.cap

    def push(self, data):
        if self.size == self.cap:
            self.cap *= 2
            self.items += [None] * (self.cap - self.size)
        self.items[self.size] = data
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        self.size -= 1
        return self.items[self.size]

    def get_top(self):
        if self.is_empty():
            return None
        return self.items[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Queue:
    def __init__(self, cap=10):
        self.items = [None] * cap
        self.front = 0
        self.rear = 0
        self.size = 0
        self.cap = cap

    def capacity(self):
        return self.cap

    def enqueue(self, data):
        if self.size == self.cap:
            self.cap *= 2
            new_items = [None] * self.cap
            for i in range(self.size):
                new_items[i] = self.items[(self.front + i) % len(self.items)]
            self.items = new_items
            self.front = 0
            self.rear = self.size
        self.items[self.rear] = data
        self.rear = (self.rear + 1) % len(self.items)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        data = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Deque:
    def __init__(self, cap=10):
        self.items = [None] * cap
        self.front = 0
        self.rear = 0
        self.size = 0
        self.cap = cap

    def capacity(self):
        return self.cap

    def push_front(self, data):
        if self.size == self.cap:
            self.cap *= 2
            new_items = [None] * self.cap
            for i in range(self.size):
                new_items[i] = self.items[(self.front + i) % len(self.items)]
            self.items = new_items
            self.front = 0
            self.rear = self.size
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = data
        self.size += 1

    def push_back(self, data):
        if self.size == self.cap:
            self.cap *= 2
            new_items = [None] * self.cap
            for i in range(self.size):
                new_items[i] = self.items[(self.front + i) % len(self.items)]
            self.items = new_items
            self.front = 0
            self.rear = self.size
        self.items[self.rear] = data
        self.rear = (self.rear + 1) % len(self.items)
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        data = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        return data

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        self.rear = (self.rear - 1) % len(self.items)
        data = self.items[self.rear]
        self.size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        return self.items[(self.rear - 1) % len(self.items)]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.items[(self.front + k) % len(self.items)]
