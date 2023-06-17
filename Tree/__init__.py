class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """ Return Position representing the tree's root (or None if empty)"""

    def parent(self, p):
        """ Return Position representing p's parent (or None if p is root)"""

        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ Return the number of children that Position p has."""

        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""

        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ Return the total number of elements in the tree."""

        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0


class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure. """

    # additional abstract methods
    def left(self, p):
        """
        Return a Position representing p's left child
        Return None if p does not have a left child

        :param p:
        :return:
        """

        raise NotImplementedError('must be imlemented by subclass')

    def right(self, p):
        """
        Return a Position representing p's right child
        Return None if p does not have a right child

        :param p:
        :return:
        """

        raise NotImplementedError('must be imlemented by subclass')

    # concrete methods implemented in this class
    def sibling(self, p):
        """ Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if not parent:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = 'val', 'parent', 'left', 'right'

        def __repr__(self):
            return "val:{val}".format(
                val=self.val if not None else None,
            )

        def __init__(self, element, parent=None, left=None, right=None):
            self.val = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.val

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __repr__(self):
            return '{}'.format(self.node)

    def _validate(self, p):
        """return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position Type")

        if p.container is not self:
            raise ValueError('p dose not belong to this container')

        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')

        return p.node

    def _make_position(self, node):
        """return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root(self):
        return self._make_position(self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1

        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position"""
        if self.root is not None:
            raise ValueError('root already exists')
        self.size = 1
        self.root = self._Node(e)

        return self._make_position(self.root)

    def _add_left(self, p, e):
        """Create a new left child for Position P, storing element e"""
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left child already exists")
        self.size += 1
        node.left = self._Node(e, node)
        return self._make_position(node.left)

    def _add_right(self, p, e):
        """Create a new right child for Position P, storing element e"""
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right child already exists")
        self.size += 1
        node.right = self._Node(e, node)
        return self._make_position(node.right)

    def _replace(self, p, e):
        """replace the element at position p with e, and return old element"""
        node = self._validate(p)
        old = node.val
        node.val = e
        return old

    def _delete(self, p):
        """
        delete the node at the position p, and replace it with its child
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

        self.size -= 1
        node.parent = node
        return node.val

    def _attach(self, p, t1, t2):
        """attach trees t1 and t2 as left and right subtrees of external p"""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self.size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root_parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.is_empty():
            t2._root_parent = node
            node.left = t2.root
            t2.root = None
            t2.size = 0

    def build_tree(self, treelist):
        level = 0
        p1 = self._add_root(treelist.pop(0))
        while treelist:
            for i in range(2 ** level):
                try:
                    left = treelist.pop(0)
                    if left:
                        exec("p{} = self._add_left(p{}, left)".format(2 ** (level + 1) + 2 * i, 2 ** level + i))
                    right = treelist.pop(0)
                    if right:
                        exec("p{} = self._add_right(p{}, treelist.pop(0))".format(2 ** (level + 1) + 2 * i + 1,
                                                                                  2 ** level + i))
                except IndexError:
                    break
                level += 1
