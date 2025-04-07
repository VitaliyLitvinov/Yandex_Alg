import sys
class Linked_Deueu:
    def __init__(self, head=None, value = None):
        self.value = value
        self.next = None
        self.size = 0

    def get(self, head, size):
        if size != 0:
            curr = head.value
            head = head.next
            sys.stdout.write(curr)

        else: sys.stdout.write('error')
        sys.stdout.write("\n")

    def put(self, value, tail, head):
        if tail:
            tail.next = self
            atail = self
        else:
            tail = self
        if not head is None:
            head = self
        self.value = value

def solution():
    size = 0
    n = int(sys.stdin.readline())
    tail = None
    head = None
    for i in range(n):
        request = sys.stdin.readline()
        if request.startswith('put'):
            node = Linked_Deueu()
            node.put(request.rstrip().split()[-1], tail, head)
            if not head is None:
                head = node
            size += 1
            tail = node
        if request.startswith('get', size):
            node = Linked_Deueu()
            node.get(head)
            if not head is None:
                node = Linked_Deueu()
                head = node
            if size != 0: size -= 1
        if request.startswith('size'):
            sys.stdout.write(str(size))
            sys.stdout.write("\n")
if __name__=="__main__":
    solution()
# 10
# put -34
# put -23
# get
# size
# get
# size
# get
# get
# put 80
# size
