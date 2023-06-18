from Tree import LinkedBinaryTree

"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]
"""


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> LinkedBinaryTree.root:
        """
        递归实现，不断地将数组二分，直到子列表无法继续分割， 此时相邻地两个列表可以直接构成左右孩子。
        时间复杂度：O(N log N)
        空间复杂度：O(log N)
        """
        if not nums:
            return None

        # 递归业务逻辑，二分数组，构建子树的根节点
        mid = len(nums) // 2
        t = LinkedBinaryTree()
        cur = t._add_root(nums[mid])

        # 递归启动，给各个子树增加左右孩子
        cur.left = self.sortedArrayToBST(nums[:mid])
        cur.right = self.sortedArrayToBST(nums[mid + 1:])

        return cur

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    res = sol.sortedArrayToBST(nums)
