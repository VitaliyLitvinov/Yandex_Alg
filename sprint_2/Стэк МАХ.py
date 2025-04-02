class MyQueueSized:
    def __init(self, n):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = n

    def push(self, value):
        if self.size == self.max_size:
            return 'error'
        else:
            self[self.head] = value
            self.head = (self.head + 1) % self.max_size
            self.size += 1

    def pop(self):
        if not is_empty(self):
            value = self[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value
        else: return None

    def peek(self):
        return self[self.tail]

    def size(self):
        return self.size
def is_empty(self):
    return self.size == 0

def Solution()
if __name__=='__main__':
    Solution()