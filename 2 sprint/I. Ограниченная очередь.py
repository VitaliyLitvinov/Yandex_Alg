class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = n

    def push(self, value):
        if self.size == self.max_size:
            print('error')
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop(self):
        if not is_empty(self):
            value = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value
        else:
            return None

    def peek(self):
        if is_empty(self):
            return None
        else:
            return self.queue[self.tail]

    def size(self):
        return self.size

def is_empty(self):
    return self.size == 0


def Solution():
    n = int(input())
    size = int(input())
    Queue = MyQueueSized(size)
    for i in range(n):
        request = input()
        if request.startswith('push'):
            Queue.push(request.rstrip().split()[-1])
        elif request.startswith('pop'):
            print(Queue.pop())
        elif request.startswith('peek'):
            print(Queue.peek())
        elif request.startswith('size'):
            print(Queue.size)


if __name__ == '__main__':
        Solution()

# 8
# 2
# peek
# push 5
# push 2
# peek
# size
# size
# push 1
# size
