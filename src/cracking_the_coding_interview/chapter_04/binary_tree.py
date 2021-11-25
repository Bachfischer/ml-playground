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

def main():
    my_tree = Tree(10)
    my_tree.insert(20)
    my_tree.insert(5)
    my_tree.insert(15)
    my_tree.in_order_traversal()
    my_tree.delete(15)
    my_tree.in_order_traversal()




if __name__ == "__main__":
    main()