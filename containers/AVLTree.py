'''
This file implements the AVL Tree data structure.
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the
    class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''

        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        elif not node:
            return True
        else:
            left = AVLTree._is_avl_satisfied(node.left)
            right = AVLTree._is_avl_satisfied(node.right)
            return left and right

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''

        former_root = node
        if node.right:
            new = Node(former_root.right.value)
            new.left = Node(former_root.value)
            new.right = former_root.right.right
            new.left.left = former_root.left
            new.left.right = former_root.right.left
            return new
        return former_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        and the textbook provides full python code.
        '''

        former_root = node
        if node.left:
            new = Node(former_root.left.value)
            new.right = Node(former_root.value)
            new.left = former_root.left.left
            new.right.right = former_root.right
            new.right.left = former_root.left.right
            return new
        return former_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        but it will also call the left and right rebalancing functions.
        '''

        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        if xs:
            for x in xs:
                if self.root:
                    self.root = AVLTree._insert(self.root, x)
                else:
                    self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''

        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            else:
                node = AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            else:
                node = AVLTree._right_rotate(node)
        return node
