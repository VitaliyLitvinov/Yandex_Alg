import sys
class QueueNode:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next

class Queue:
    def __init(self):
        self.head = 0
        self.tail = 0
        self.size: int = 0
    def put(self):

    def get(self):

    def size(self):



def solution(n):
    queue: Queue = Queue()
    for _ in range(n):
        request: str = sys.stdin.readline().strip()
        if request.startswith('get'):
            queue.get()
        elif request.startswith('put'):
            queue.put()
        elif request.startswith("size"):
            queue.size()


if __name__ == "__main__":
    solution(sys.stdin.readline().strip())