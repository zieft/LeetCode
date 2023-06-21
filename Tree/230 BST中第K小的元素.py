from Tree import LinkedBinaryTree, null

"""
Given the root of a binary search tree, and an integer k, return the k-th smallest value (1-indexed) of all the values 
of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""


class Solution:
    def kthSmallest(self, root: LinkedBinaryTree.root, k: int) -> int:
        """
        中序遍历，递归实现
        时间复杂度 O(N)
        空间复杂度 O(H)
        """
        self.counter = 0
        self.kthSmallest = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.counter += 1
            if self.counter == k:
                self.kthSmallest = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.kthSmallest


if __name__ == '__main__':
    sol = Solution()
    t = LinkedBinaryTree()
    t.build_tree([1,null,2])
    res = sol.kthSmallest(t.root, 3)
