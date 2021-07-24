"""
Sort Stack:
Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
This algorithm complexity is O (N^2 ) in time and O (N) in space.
"""

class StackException(Exception):
    """Exception raised for errors in stack.

    Attributes:
    """

    def __init__(self):
        pass


class StackNode:
    """Nodes stored in stack data structures

    Attributes:
        data -- payload to be stored by node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Implementation of Stack data structure

    Attributes:
    """

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise StackException
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, data):
        t = StackNode(data)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top is None:
            raise StackException
        return self.top.data

    def is_empty(self):
        return self.top is None

    def print(self):
        print("Printing content of stack")
        current_node = self.top
        while current_node is not None:
            print(str(current_node.data) + " ", sep=' ', end='', flush=True)
            current_node = current_node.next
        print("\n")

    def sort(self):
        temporary_stack = Stack()

        while not self.is_empty():
            temp = self.pop()
            while not temporary_stack.is_empty() and temp < temporary_stack.peek():
                self.push(temporary_stack.pop())
            temporary_stack.push(temp)

        while not temporary_stack.is_empty():
            self.push(temporary_stack.pop())


def main():
    stack = Stack()
    stack.push(99)
    stack.push(5)
    stack.push(60)
    stack.push(3)
    stack.push(35)
    stack.push(54)
    stack.push(523)
    stack.push(1)
    stack.print()
    stack.sort()
    stack.print()



if __name__ == "__main__":
    main()
