# 99, #112, #119
#

# Idea: Pick random number 1 - 3 to choose between curent node, left and right node
# Would need to factor into account total number of nodes (to make probability of choosing current node lower)
# TODO: As you descent the tree, you need to increase the probability / decrease the range to sample from

import random

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None

    def in_order_traversal(self):
        if self.left_child is not None:
            self.left_child.in_order_traversal()
        self.visit()
        if self.right_child is not None:
            self.right_child.in_order_traversal()

    def pre_order_traversal(self):
        self.visit()
        if self.left_child is not None:
            self.left_child.in_order_traversal()

        if self.right_child is not None:
            self.right_child.in_order_traversal()

    def post_order_traversal(self):
        if self.left_child is not None:
            self.left_child.in_order_traversal()

        if self.right_child is not None:
            self.right_child.in_order_traversal()
            
        self.visit()


    def visit(self):
        print(self.data)

    def insert(self, data : int):
        if data < self.data and self.left_child is None:
            self.left_child = Node(data)
        elif data < self.data:
            self.left_child.insert(data)
        elif data > self.data and self.right_child is None:
            self.right_child = Node(data)
        elif data > self.data:
            self.right_child.insert(data)
        else:
            print("Data already stored in tree!")

    def get_size(self):
        size_left = 0
        size_right = 0
        if self.left_child is not None:
            size_left = self.left_child.get_size()
        if self.right_child is not None:
            size_right = self.right_child.get_size()

        return size_left + size_right + 1

    def find(self, data: int):
        if data == self.data:
            return self
        elif data < self.data:
            self.left_child.find(data)
        else:
            self.right_child.find(data)

    def delete(self, data: int):
        if self is None:
            return self
        if data < self.data:
            self.left_child = self.left_child.delete(data)
            return self
        if data > self.data:
            self.right_child = self.right_child.delete(data)
            return self
        if self.right_child is None:
            return self.left_child
        if self.left_child is None:
            return self.right_child
        min_larger_node = self.right_child
        while min_larger_node.left_child:
            min_larger_node = min_larger_node.left_child
        self.data = min_larger_node.data
        self.right_child = self.right_child.delete(min_larger_node.data)
        return self

    def get_random_node(self):
        total_size = self.get_size()
        size_left = 0
        if self.left_child is not None:
            size_left = self.left_child.get_size()

        random_number = random.randint(0, total_size -1)
        if random_number < size_left:
            return self.left_child.get_random_node()
        elif random_number == size_left:
            return self
        else:
            return self.right_child.get_random_node()

    def get_data(self):
        return self.data


class Tree:

    def __init__(self, data: int):
        self.root_node = Node(data)

    def in_order_traversal(self):
        print("In-order traversal:")
        self.root_node.in_order_traversal()

    def pre_order_traversal(self):
        print("Pre-order traversal:")
        self.root_node.pre_order_traversal()

    def post_order_traversal(self):
        print("Post-order traversal:")
        self.root_node.post_order_traversal()

    def insert(self, data):
        self.root_node.insert(data)

    def find(self, data):
        self.root_node.find(data)

    def delete(self, data):
        self.root_node.delete(data)

    def get_random_node(self):
        return self.root_node.get_random_node()

def main():
    my_tree = Tree(10)
    my_tree.insert(20)
    my_tree.insert(5)
    my_tree.insert(15)
    my_tree.in_order_traversal()
    my_tree.delete(15)
    my_tree.in_order_traversal()
    my_random_node = my_tree.get_random_node()
    print("Randomly selected node is: ", my_random_node.get_data())



if __name__ == "__main__":
    main()