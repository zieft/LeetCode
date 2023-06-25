"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        回溯

        """
        combinations = []
        n = len(nums)

        def backtrack(index):
            tmp = tuple(combination)
            combinations.append(list(tmp))

            for i in range(index, n):
                # combination += [nums[j]]  # 这样写会报local variable 'combination' referenced before assignment
                combination.append(nums[i])
                backtrack(i + 1)
                combination.pop()

        combination = list()
        backtrack(0)
        return combinations


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    res = sol.subsets(nums)
    print(res)
