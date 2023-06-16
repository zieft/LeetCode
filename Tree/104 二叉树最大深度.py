from Tree import LinkedBinaryTree

"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""


class Solution(object):
    def maxDepth_recursion(self, root):
        """
        递归法
        N是二叉树的节点。
        时间复杂度：最好情况下（平衡树）：O(log N), 最坏情况下（歪脖子树）：O(N)
        空间复杂度：最好情况下（平衡树）：O(log N), 最坏情况下（歪脖子树）：O(N)
        """
        if root:
            return max(self.maxDepth_recursion(root.left), self.maxDepth_recursion(root.right)) + 1

        return 0

if __name__ == '__main__':

    sol = Solution()
    T = LinkedBinaryTree()
    T.build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.maxDepth_recursion(T.root))
