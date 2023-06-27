"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        找到一个子集，其元素相加后的结果（11）是原集合求和的结果（22）的一半，即返回True
        抽象成01背包，有一个容量为11的背包，有一列物品，其重量和价值相同，问能不能从集合中的物品选出一部分将背包装满，也即价值=11
        O(n^2)
        O(n)，虽然dp数组⼤⼩为⼀个常数，但是⼤常数
        """
        target = sum(nums)
        if target % 2 == 0:
            dp = [0] * (sum(nums) // 2 + 1)

            for i in range(0, len(nums)):
                for j in range(target // 2, nums[i] - 1, -1):
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

                    if dp[j] == target / 2:
                        return True
            return False

        else:
            return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    sol = Solution()
    res = sol.canPartition(nums)
    print(res)
