class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self, value):
        if self == None:
            return False
        elif self.value == value:
            return True
        else:
            return self.left.search(value) + self.right.search()

    def find_all(self, value):
        if self == None:
            return 0
        elif self.value == value:
            return 1
        else:
            return self.left.find_all() + self.right.find_all()

    def count_leaves(self):
        if self == None:
            return 0
        elif self.left == None and self.right == None:
            return 1
        else:
            return self.left.count_leaves() + self.right.count_leaves()

    # def count_nodes(self):
    #     if self == None:
    #   

    def __repr__(self):
        return f'BinaryNode({self.value})'      

hi = BinaryNode(2)
hi.left = BinaryNode(3)
hi.right = BinaryNode(4)
hi.right.right = BinaryNode(5)
hi.right.left = BinaryNode(6)

print(hi, hi.left, hi.count_leaves())
