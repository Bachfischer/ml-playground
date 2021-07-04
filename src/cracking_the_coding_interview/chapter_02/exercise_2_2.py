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

    list_length = head.get_size()
    print("List length: ", list_length)

    print("1st element from head", head.get_element_by_index(0).data)
    print("2nd element from tail: ", head.get_element_by_reverse_index(2).data)

    print_kth_to_last_element(head, 4)

if __name__ == "__main__":
    main()
