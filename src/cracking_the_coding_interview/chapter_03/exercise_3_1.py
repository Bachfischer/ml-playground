"""
Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #72, #38, #58
"""

class StackException(Exception):
    """Exception raised for errors in stack.

    Attributes:
    """

    def __init__(self):
        pass


class MultiStack:
    """Implementation of Stack data structure

    Attributes:
    """

    def __init__(self, length_of_array):
        self.number_of_stacks = 3
        if length_of_array % self.number_of_stacks != 0:
            raise Exception("Length of array must be multiple of ", self.number_of_stacks)
        self.length = int(length_of_array / self.number_of_stacks)
        self.array = [None for _ in range(length_of_array)]


    def push(self, target_stack, data):
        # Calculate range of target_stack in array
        start_pos = target_stack * self.length
        end_pos = start_pos + self.length -1

        for i in range(start_pos, end_pos):
            if self.array[i] is None:
                self.array[i] = data
                return True
        # stack is full
        raise StackException

    def pop(self, target_stack):
        # Calculate range of target_stack in array
        start_pos = target_stack * self.length
        end_pos = start_pos + self.length -1

        for i in range(end_pos, start_pos -1, -1):
            if self.array[i] != None:
                data = self.array[i]
                self.array[i] = None
                return data
        # stack is empty - no element to pop
        raise StackException


    def peek(self, target_stack):
        # Calculate range of target_stack in array
        start_pos = target_stack * self.length
        end_pos = start_pos + self.length -1

        for i in range(end_pos, start_pos -1, -1):
            if self.array[i] != None:
                return self.array[i]
        # stack is empty - no element to peek
        raise StackException

    def is_empty(self, target_stack):
        start_pos = target_stack * self.length
        end_pos = start_pos + self.length -1

        for i in range(end_pos, start_pos, -1):
            if self.array[i] != None:
                return False
        return True

def main():
    multi_stack = MultiStack(9)
    multi_stack.push(0, 5)
    print("Retrieved element: ", multi_stack.pop(0))
    try:
        multi_stack.pop(0)
    except StackException:
        print("Error occured")
    multi_stack.push(1, 4)
    multi_stack.push(2,1)
    print("Retrieving data from second stack: ", multi_stack.peek(1))


if __name__ == "__main__":
    main()
