"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        回溯
        backtrack 的调用次数是 O(n!)，将当前答案使用 O(n) 的时间复制到答案数组中
        时间复杂度：O(n×n!)
        空间复杂度：O(n)

        """
        combinations = []
        if not nums:
            return combinations

        def backtrack(index):
            if index == len(nums):
                if len(set(combination)) == len(nums):
                    tmp = tuple(combination)    # 这一步将combination的值拷贝至另一块内存
                                                # 否则combinations里存的都是combination的引用
                    combinations.append(list(tmp))
                return

            for i in range(len(nums)):
                combination.append(nums[i])
                backtrack(index + 1)
                combination.pop()

        combination = list()
        backtrack(0)
        return combinations


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    res = sol.permute(nums)
    print(res)
