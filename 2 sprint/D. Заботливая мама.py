class Node:
    def __init__(self, value=None, next = None):
        self.next = next
        self.value = value
def find_index(head, elem):
    count = 0
    while head:
        if head.value == elem: return count
        count += 1
        head = head.next
    return 'element not in linked list'

n3 = Node("3")
n2 = Node('2', n3)
n1 = Node( '1', n2)


if __name__=="__main__":
    print(find_index(n1, '2'))


