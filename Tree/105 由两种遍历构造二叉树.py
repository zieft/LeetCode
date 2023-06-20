from Tree import LinkedBinaryTree, null

"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], 
       inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> LinkedBinaryTree.root:
        """
        在每次递归调用中，都需要在中序遍历列表中查找根节点的位置，最坏情况下，二叉树为链状结构，高度为 n-1，因此递归调用的次数为 O(n)，
        每次递归调用都会创建新的子列表，因此空间复杂度为 O(n)。

        时间复杂度和空间复杂度都为 O(n)。
        """
        t = LinkedBinaryTree()

        if not (preorder and inorder):
            return None
        # 前序列表可以分为3个部分，第一部分也就是第一个值是树的根，紧接着是跟的左子树的所有节点，再接着是右子树的所有节点
        # 中序列表也可以分为3个部分，第一部分是根的左子树的所有节点，接着是根，再接着是根的右子树所有节点
        root = t._add_root(preorder[0])  # 前序的第一个值是树的根，
        mid_index = inorder.index(preorder[0])  # 按根节点位置将两个数列分成两个部分，分别对应原树的左子树和右子树
        # [].index()操作会产生O(n)的复杂度
        left_preorder = preorder[1:mid_index + 1]
        left_inorder = inorder[:mid_index]
        right_preorder = preorder[mid_index + 1:]
        right_inorder = inorder[mid_index + 1:]

        t._add_left(root, self.buildTree(left_preorder, left_inorder))
        t._add_right(root, self.buildTree(right_preorder, right_inorder))

        return t.root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    res = sol.buildTree(preorder, inorder)
