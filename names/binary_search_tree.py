class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            self = self.right
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # implemented using a recursive depth first PreOrder traversal
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the result in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # implemented using InOrder depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        """[Level order traversal]
        1- create an empty queue
        2- enqueue the root node
        3- loop until the queue is empty
            1- dequeue the first node in the queue
            2- manipulate the picked node
            3- enqueue the left node if it exists
            4- enqueue the right node if it exists
            - repeat...
        """
        queue = []
        queue.append(self)
        while len(queue):
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        """[iterative PreOrder traversal]
        1- create an empty stack
        2- push the root node to the stack
        3- loop until the stack is empty
            1- pop the top element in the stack
            2- manipulate the popped node
            3- push the right node if it exists (push right first to have left on top)
            4- push the left node if it exists
            - repeat...
        """
        stack = []
        stack.append(self)
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

    def get_height(self):
        if self.left and self.right:
            return max(self.left.get_height(), self.right.get_height()) + 1
        if self.left:
            return self.left.get_height() + 1
        if self.right:
            return self.right.get_height() + 1
        else:
            return 0

