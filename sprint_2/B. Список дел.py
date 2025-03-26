class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
def solution(node):
    while node:
        print(node.value, end='->')
        node = node.next
    print('None')

def test():
    n3 = Node('3')
    n2 = Node('2', n3)
    n1 = Node('1', n2)
    solution(n1)

if __name__=="__main__":
    test()
