class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.value, end=' → ')
            current = current.next
        print('None')

def __main__():

    linked_list = LinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)

    linked_list.display()


    



if __name__ == '__main__':
    __main__()