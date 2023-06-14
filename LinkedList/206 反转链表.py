from LinkedList import ListNode, BaseSolution

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


class Solution(BaseSolution):
    def reverseList(self, head: ListNode) -> ListNode:
        """
        基于链表节点的修改，而不创建新的节点。
        时间复杂度 O(n)
        空间复杂度 O(1)
        """
        # 原地头插法，复杂度O(n), O(1)
        # 其实也是双指针
        cur = head  # cur指针用于遍历原链表
        prev = None  # prev用于原地修改链表
        while cur:
            next_node = cur.next  # 缓存cur.next（断开cur和cur.next）
            cur.next = prev  # cur和prev接起来，也即给prev插上链表头
            prev = cur  # 向左移动prev指针，使其指向新链表头
            cur = next_node  # cur继续向后遍历
        return prev


if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([1, 2, 3, 4, 5])
    res = sol.reverseList(l1)
    sol.print_LinkedList(res)
