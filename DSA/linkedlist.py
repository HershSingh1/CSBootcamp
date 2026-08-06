# singly linked lists


class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)


Head.next = A
A.next = B
B.next = C

# print(Head)

# to traverse - o(n)

curr = Head

while curr:  # until curr turns into none
    print(curr)
    curr = curr.next


# display the linked list - o(n)


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))


display(Head)


# search for node value - o(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False


search(Head, 7)


# doubly linked list


class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

    head = tail = DoublyNode(1)
    print(head)
    print(tail)

    def display(head):
        curr = head
        elements2 = []
        while curr:
            elements2.append(str(curr.val))
            curr = curr.next
        print(" <-> ".join(elements))

    display(head)


# insert at beginning


def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail


head, tail = insert_at_beginning(head, tail, 3)
display(head)


# insert at end (this and beginning is o(1))


def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node


head, tail = insert_at_end(head, tail, 7)
display(head)
