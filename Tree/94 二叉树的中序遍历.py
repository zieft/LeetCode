from Tree import LinkedBinaryTree, null

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
"""


class Solution:
    def inorderTraversal(self, root: LinkedBinaryTree.root) -> list[int]:
        """
        中序遍历，就是在递归的中间输出节点。
        时间复杂度：O(N)
        空间复杂度：最坏情况下为O(N)（当二叉树为链表结构时）
        """
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res


if __name__ == '__main__':
    sol = Solution()
    t = LinkedBinaryTree()
    t.build_tree([1, null, 2, 3])
    res = sol.inorderTraversal(t.root)
