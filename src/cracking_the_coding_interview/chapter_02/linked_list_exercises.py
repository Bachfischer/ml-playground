"""
Return kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.
"""

class Node:
    next_node = None
    data = 0

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def append_to_tail(self, data: int):
        end_node = Node(data)
        next_node = self

        while next_node.next_node is not None:
            next_node = next_node.next_node
        next_node.next_node = end_node

    def print_data(self) -> None:
        current_node = self
        while current_node is not None:
            print("Data: ", current_node.data)
            current_node = current_node.next_node

    def get_size(self) -> int:
        num_nodes = 0
        current_node = self

        while current_node is not None:
            num_nodes += 1
            current_node = current_node.next_node

        return num_nodes

    def get_element_by_index(self, index: int):
        current_node = self
        num_nodes = 0

        while current_node is not None and num_nodes < index:
            num_nodes += 1
            current_node = current_node.next_node

        return current_node

    def get_element_by_reverse_index(self, reverse_index: int):
        list_length = self.get_size()
        if list_length == 0:
            return None

        index = list_length - 1 - reverse_index

        return self.get_element_by_index(index)

    def remove_element_by_index(self, position):
        if position == 0:
            self = self.next_node
        else:
            front_node = self.get_element_by_index(position -1)
            node_to_delete = front_node.next_node
            front_node.next_node = node_to_delete.next_node
        return self

    """
    Exercise 2.1
    """
    def remove_duplicates(self):
        stored_data = {}
        current_node = self

        while current_node is not None:
            if current_node.data not in stored_data:
                stored_data[current_node.data] = 1
            current_node = current_node.next_node

        start_node = None
        for key in stored_data.keys():
            if start_node is None:
                start_node = Node(key)
            else:
                start_node.append_to_tail(key)

        return start_node

"""
Exercise 2.3
"""
def remove_middle_node(node_to_remove: Node):
    if node_to_remove.next_node is None:
        return False
    node_to_remove.data = node_to_remove.next_node.data
    node_to_remove.next_node = node_to_remove.next_node.next_node
    return True


"""
Exercise 2.2
"""
def print_kth_to_last_element(head, k: int):
    if head is None:
        return 0

    index = print_kth_to_last_element(head.next_node, k) + 1
    if index == k:
        print(k,"th to last node is ", head.data)
    return index


def main():
    head = Node(5)
    head.print_data()

    head.append_to_tail(10)
    head.append_to_tail(15)
    head.append_to_tail(20)

    head.print_data()

    # Remove k-th element from tail (exercise 2.2)
    list_length = head.get_size()
    print("List length: ", list_length)

    print("1st element from head", head.get_element_by_index(0).data)
    print("2nd element from tail: ", head.get_element_by_reverse_index(2).data)

    print_kth_to_last_element(head, 4)

    # Remove duplicates (exercise 2.1)
    head.append_to_tail(5)
    print("List with duplicates")
    head.print_data()
    #head = head.remove_element_by_index(4)
    print("List without duplicates")
    head = head.remove_duplicates()

    head.print_data()
    head.append_to_tail(35)

    # Remove middle node (exercise 2.3)
    head.print_data()
    middle_node = head.get_element_by_index(2)
    print("Data of middle node: ", middle_node.data)
    remove_middle_node(middle_node)
    head.print_data()


if __name__ == "__main__":
    main()
