from Tree import LinkedBinaryTree

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Input: root = [2,1,3]
Output: true
"""


class Solution:
    def isValidBST(self, root: LinkedBinaryTree.root) -> bool:
        """
        中序遍历
        时间复杂度为 O(N)
        空间复杂度为 O(H)
        """
        stack = []
        inorder = float('-inf')  # 记录当前节点前一个节点的值

        while stack or root:
            # 将根节点及其左子树依次入栈，直到左子树为空
            while root:
                stack.append(root)
                root = root.left

            # 然后从栈中取出节点，检查节点的值是否满足 BST 的性质
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val

            # 将右子树入栈
            root = root.right

        return True


if __name__ == '__main__':
    sol = Solution()
    t = LinkedBinaryTree()
    t.build_tree([5, 1, 4, None, None, 3, 6])
    print(sol.isValidBST(t.root))

    t2 = LinkedBinaryTree()
    t2.build_tree([2, 1, 3])
    print(sol.isValidBST(t2.root))
