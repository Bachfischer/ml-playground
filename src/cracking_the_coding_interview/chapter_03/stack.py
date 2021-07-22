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

def main():
    stack = Stack()
    stack.push(5)
    print("Retrieved element: ", stack.pop())
    try:
        stack.pop()
    except StackException:
        print("Error occured")


if __name__ == "__main__":
    main()
