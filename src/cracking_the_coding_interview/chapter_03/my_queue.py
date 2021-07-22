class QueueException(Exception):
    """Exception raised for errors in stack.

    Attributes:
    """

    def __init__(self):
        pass

class QueueNode:
    """Nodes stored in stack data structures

    Attributes:
        data -- payload to be stored by node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Implementation of Stack data structure

    Attributes:
    """

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        t = QueueNode(data)
        if self.last != None:
            self.last.next = t
        self.last = t
        if self.first is None:
            self.first = t

    def remove(self):
        if self.first is None:
            raise QueueException
        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            raise QueueException
        return self.first.data

    def is_empty(self):
        return self.first is None

def main():
    queue = Queue()
    queue.add(5)
    print("Retrieved element: ", queue.remove())
    try:
        queue.remove()
    except QueueException:
        print("Error occured")


if __name__ == "__main__":
    main()
