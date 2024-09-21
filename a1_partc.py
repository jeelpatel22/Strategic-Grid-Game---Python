# Copy over your a1_partc.py file here

class Stack:
    def __init__(self, cap=10):
        self.my_stack = [None] * cap
        self.s_size = 0
        self.s_capacity = cap

    def capacity(self):
        return self.s_capacity

    def push(self, data):
        if self.s_size == self.s_capacity:
            self.size_formatting(2 * self.s_capacity)
        
        self.my_stack[self.s_size] = data
        self.s_size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        
        self.s_size -= 1
        data = self.my_stack[self.s_size]
        self.my_stack[self.s_size] = None  
        return data

    def get_top(self):
        if self.is_empty():
            return None
        return self.my_stack[self.s_size - 1]

    def is_empty(self):
        return self.s_size == 0

    def __len__(self):
        return self.s_size

    def size_formatting(self, n_capacity):
        n_stack = [None] * n_capacity
        for i in range(self.s_size):
            n_stack[i] = self.my_stack[i]
        self.my_stack = n_stack
        self.s_capacity = n_capacity

class Queue:
    def __init__(self, cap=10):
        self.s_queue = [None] * cap
        self.s_front = 0 
        self.s_size = 0  
        self.s_capacity = cap

    def capacity(self):
        return self.s_capacity

    def enqueue(self, data):
        if self.s_size == self.s_capacity:
            self.size_formatting(2 * self.s_capacity)
        
        b_index = (self.s_front + self.s_size) % self.s_capacity
        self.s_queue[b_index] = data
        self.s_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        
        data = self.s_queue[self.s_front]
        self.s_queue[self.s_front] = None  
        self.s_front = (self.s_front + 1) % self.s_capacity
        self.s_size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            return None
        return self.s_queue[self.s_front]

    def is_empty(self):
        return self.s_size == 0

    def __len__(self):
        return self.s_size

    def size_formatting(self, n_capacity):
        n_queue = [None] * n_capacity
        for i in range(self.s_size):
            n_queue[i] = self.s_queue[(self.s_front + i) % self.s_capacity]
        self.s_queue = n_queue
        self.s_front = 0
        self.s_capacity = n_capacity




class Deque:
    def __init__(self, cap=10):
        self.s_deque = [None] * cap
        self.s_front = 0  
        self.s_size = 0  
        self.s_capacity = cap

    def capacity(self):
        return self.s_capacity

    def push_front(self, data):
        if self.s_size == self.s_capacity:
            self.size_formatting(2 * self.s_capacity)
        
        self.s_front = (self.s_front - 1) % self.s_capacity
        self.s_deque[self.s_front] = data
        self.s_size += 1

    def push_back(self, data):
        if self.s_size == self.s_capacity:
            self.size_formatting(2 * self.s_capacity)
        
        b_index = (self.s_front + self.s_size) % self.s_capacity
        self.s_deque[b_index] = data
        self.s_size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        
        data = self.s_deque[self.s_front]
        self.s_deque[self.s_front] = None  
        self.s_front = (self.s_front + 1) % self.s_capacity
        self.s_size -= 1
        return data

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        
        b_index = (self.s_front + self.s_size - 1) % self.s_capacity
        data = self.s_deque[b_index]
        self.s_deque[b_index] = None  
        self.s_size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            return None
        return self.s_deque[self.s_front]

    def get_back(self):
        if self.is_empty():
            return None
        b_index = (self.s_front + self.s_size - 1) % self.s_capacity
        return self.s_deque[b_index]

    def is_empty(self):
        return self.s_size == 0

    def __len__(self):
        return self.s_size

    def __getitem__(self, k):
        if k < 0 or k >= self.s_size:
            raise IndexError('Index out of range')
		
        return self.s_deque[(self.s_front + k) % self.s_capacity]

    def size_formatting(self, n_capacity):
        n_deque = [None] * n_capacity
        for i in range(self.s_size):
            n_deque[i] = self.s_deque[(self.s_front + i) % self.s_capacity]
        self.s_deque = n_deque
        self.s_front = 0
        self.s_capacity = n_capacity
