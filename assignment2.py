class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if n <= 0:
                raise IndexError("Index must be a positive integer.")
            if not self.head:
                raise Exception("Cannot delete from an empty list.")
            if n == 1:
                print(f"Deleting node at position {n}: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            prev = None
            count = 1
            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n}: {current.data}")
            prev.next = current.next

        except Exception as e:
            print(f"Error: {e}")


# Sample Test
if __name__ == "__main__":
    ll = LinkedList()
    print("Initial List:")
    ll.print_list()

    # Adding nodes
    for value in [10, 20, 30, 40, 50]:
        ll.add_to_end(value)

    print("\nList after adding nodes:")
    ll.print_list()

    # Deleting nodes
    ll.delete_nth_node(3)  # delete the 3rd node (value 30)
    print("\nList after deleting 3rd node:")
    ll.print_list()

    ll.delete_nth_node(1)  # delete the head node (value 10)
    print("\nList after deleting 1st node:")
    ll.print_list()

    ll.delete_nth_node(10)  # out of range
    ll.delete_nth_node(0)   # invalid index
    ll.delete_nth_node(2)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)   # now list is empty
    ll.delete_nth_node(1)   # delete from empty list
