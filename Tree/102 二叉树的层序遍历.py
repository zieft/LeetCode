from Tree import LinkedBinaryTree, null

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, 
    level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1, 2, null, 3, null, 4, null, 5]
Output: [[1], [2], [3], [4], [5]]
"""


class Solution:
    def levelOrder_iteration(self, root: LinkedBinaryTree.root):
        """
        层序遍历，迭代实现，用队列储存节点。
        时间复杂度 O(N)
        空间复杂度 O(N)，空间复杂度与树的宽度成正比。
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            tmp = []
            for i in range(len(queue)):
                root = queue.pop(0)
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp)

        return res

    def levelOrder_recursion(self, root: LinkedBinaryTree.root):
        """
        深度优先搜索，递归实现，用栈存储节点。
        时间复杂度O(N)
        空间复杂度O(H)，空间复杂度与树的高度成正比
        """
        res = []
        if not root:
            return res

        def dfs(index, node):
            if len(res) - 1 < index:  # index表示当前所在的层数
                # 如果列表的长度小于当前层数，插入一个空列表用于储存当前层的值
                res.append([])
            # 插入当前值
            res[index].append(node.val)

            # 递归
            if node.left:
                dfs(index + 1, node.left)
            if node.right:
                dfs(index + 1, node.right)

        dfs(0, root)
        return res


if __name__ == '__main__':
    sol = Solution()
    t = LinkedBinaryTree()
    t.build_tree([1, 2, null, 3, null, 4, null, 5])
    res = sol.levelOrder_recursion(t.root)
