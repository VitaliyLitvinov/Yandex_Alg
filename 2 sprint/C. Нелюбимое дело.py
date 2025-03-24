class Node:
    def __init__(self, value=None, next = None):
        self.next = next
        self.value = value
def print_linked_list(head):
    while head:
        print(head.value, end='->')
        head = head.next
    print(head)
def del_value(index, head):
    prev = None
    curr = None
    while index:
        prev = head
        head = head.next
        curr = head.next
        index -= 1
    head = prev
    head.next = curr

n3 = Node("3")
n2 = Node('2', n3)
n1 = Node( '1', n2)

if __name__=="__main__":
    del_value(2, n1)
    print_linked_list(n1)
