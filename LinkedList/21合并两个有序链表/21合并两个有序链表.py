from LinkedList import ListNode, BaseSolution

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


class Solution(BaseSolution):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        时间复杂度：O(n)
        空间复杂度：【考虑递归开栈】O(n)【不考虑】O(1)
        """
        # 判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
        if l1 and l2:
            # 当l1的值比l2的值大时，交换 l1 和 l2 节点的位置，使得 l1 总是指向比较小的那个节点对象
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # 递归重复以上过程直至l1、l2其中之一为空
            l1.next = self.mergeTwoLists(l1.next, l2)
        # 返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None
        # 有l1的时候返回l1，没有的时候直接返回l2，并赋值给l1.next
        return l1 or l2


"""
备注： 在 Python 中，and 和 or 都有提前截止运算的功能。

and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
例子：[] and 7 等于 []
https://leetcode.cn/problems/merge-two-sorted-lists/solutions/4116/python-4xing-by-knifezhu-3/
"""

if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([1, 2, 4])
    l2 = sol.create_linklist_tail([1, 3, 4])
    res = sol.mergeTwoLists(l1, l2)
    sol.print_LinkedList(res)
