# head = ListNode(-3)
# head.next = ListNode(-2)
# head.next.next = ListNode(-1)
# head.next.next.next = ListNode(0)
# tmp = head.next.next.next
# tmp.next = ListNode(1)
# tmp.next.next = ListNode(2)
# tmp.next.next.next = tmp
from LinkedList import ListNode, BaseSolution

class Solution(BaseSolution):
    def hasCycle(self, head: ListNode) -> bool:
        """
        时间复杂度 O(n)
        空间复杂度 O(1)
        """
        if not head:
            # 空链表一定不是环形链表
            return False

        slow = head
        fast = head

        while fast and fast.next:
            # 如果我们只检查while fast:，那么在快指针已经到达链表末尾时，fast.next将会引发空指针异常。
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # slow == fast的条件是数值相等，并且next以及next的next。。。都要相等

                return True
        # 如果不是环形链表，快指针肯定会比满指针更快触底并退出循环
        return False

