class Node:

    def __init__(self, name):
        self.name = name
        self.children = []

    def print(self):
        print(self.name)
        for child in self.children:
            child.print()


class Tree:

    def __init__(self, name):
        self.root_node = Node(name)

    def print(self):
        self.root_node.print()




def main():
    my_tree = Tree("Matthias")
    my_tree.print()


if __name__ == "__main__":
    main()