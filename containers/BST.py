from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __iter__(self):
        for value in super().__iter__():
            yield value

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if value <= node.value:
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if value >= node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.insert(x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        if not self.root:
            return None
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        if node.value == value:
            return True
        if node.value < value:
            if node.right:
                return BST._find(value, node.right)
        else:
            if node.left:
                return BST._find(value, node.left)

    def find_smallest(self):
        if self.root:
            return BST._find_smallest(self.root)
        else:
            return None

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if not node.left:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        if self.root:
            return BST._find_largest(self.root)
        else:
            return None

    @staticmethod
    def _find_largest(node):

        assert Node is not None
        if not node.right:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        self.root = BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):

        if not node:
            return None
        if node.value > value:
            node.left = BST._remove(value, node.left)
        elif node.value < value:
            node.right = BST._remove(value, node.right)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            if node.left and node.right:
                min_node_value = BST._find_smallest(node.right)
                node.value = min_node_value
                node.right = BST._remove(min_node_value, node.right)
        return node

    def remove_list(self, xs):
        for x in xs:
            self.remove(x)
