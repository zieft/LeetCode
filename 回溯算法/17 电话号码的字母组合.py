"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        回溯 组合问题
        时间复杂度：O(3^m×4^n)
        空间复杂度：O(m+n)
        m 是输入中对应 3 个字母的数字个数（包括数字 2、3、4、5、6、8）
        n 是输入中对应 4 个字母的数字个数（包括数字 7、9）
        m+n 是输入数字的总个数
        """
        combinations = []
        if not digits:
            return combinations
        self.hashmap = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }
        self.digits = list(digits)

        def backtrack(combination, index, digits):
            # 当把整个问题抽象成树结构的时候，index和len(digits)就是树的深度
            # 记录数据发生在树的叶子上（深度最深的地方）
            if index == len(digits):
                combinations.append(combination)
                return  # 结束这个叶子的处理，回溯到父节点

            for i in self.hashmap[digits[index]]:  # 横向遍历，访问每一个元素
                backtrack(combination + i, index + 1, self.digits)  # 纵向遍历，遍历到树的最深处，实质上是DFS

        backtrack('', 0, digits)
        return combinations


if __name__ == '__main__':
    sol = Solution()
    digits = "23"
    res = sol.letterCombinations(digits)
    print(res)
