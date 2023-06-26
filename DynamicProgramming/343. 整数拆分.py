"""
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        给一个数i，将其拆分成k个整数后的最大乘积是dp[i]。
        dp[i-j] 是规模更小的子问题，在i从小到大的遍历中，一定会比dp[i]先被求解
        O(n^2)
        O(n)
        """
        dp = [1] * (n + 1)  # 问题的规模是[2到n]共n-1个数，数组的大小为n+1 抛去下标为0和1的两个无意义点，正好和问题规模对齐
        # dp[0] = 0
        # dp[1] = 0
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):  # 因为拆分后的数相互越接近，乘积越大，
                                            # 而拆两次得到的被拆数最大，为i/2 (+1), 所以遍历到ceil(i/2)即可
                dp[i] = max(
                    j * (i - j),
                    j * dp[i - j],
                    dp[i]  # 在内循环中更新dp[i]的值
                )

        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    res = sol.integerBreak(2)
    print(res)
