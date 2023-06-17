from Tree import LinkedBinaryTree

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""


class Solution:
    def isSymmetric(self, root: LinkedBinaryTree.root) -> bool:
        """
        递归实现，深度优先搜索
        O(n)
        O(n)
        """
        if not root:
            return True

        def dfs(left, right):
            """函数体内定义终止条件，return中写业务逻辑并启动递归"""
            if not (left or right):  # 两个节点中有一个为空
                return True
            if not (left and right):  # 两个节点都为空
                return False
            if left.val != right.val:  # 两个节点的值不相等
                return False
            # 同时比较左子树的左节点和右子树的右节点，和，左子树的右节点和右子树的左节点。
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


if __name__ == '__main__':
    sol = Solution()
    t1 = LinkedBinaryTree()
    t1.build_tree([1, 2, 2, 3, 4, 4, 3])
    res = sol.isSymmetric(t1.root)

    t2 = LinkedBinaryTree()
    t2.build_tree([1, 2, 2, None, 3, None, 3])
    res2 = sol.isSymmetric(t2.root)
