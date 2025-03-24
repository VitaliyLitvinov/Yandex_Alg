class Node:
    def __init__(self, value=None, next = None):
        self.next = next
        self.value = value
def revers_list(head):
    prev = None
    while head:
        curr = head.next
        head.next = prev
        prev = head
        head = curr
    return prev


n3 = Node("3")
n2 = Node('2', n3)
n1 = Node( '1', n2)


if __name__=="__main__":
    print(revers_list(n1))
