from LinkedList import BaseSolution, ListNode

"""
Given the head of a linked list, return the list after sorting it in ascending order.
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""


class Solution(BaseSolution):
    def sortList_recursion(self, head: ListNode) -> ListNode:
        """
        递归实现的归并排序算法。
        时间复杂度：O(n log n)， n 是链表的长度
        空间复杂度：O(log n)，递归调用，因此会使用递归栈空间。在最坏情况下，递归深度为 log n。
        """
        if not head or not head.next:
            return head  # termination.
        # 快慢指针找链表的中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # 切断链表，一分为二
        # 链表为奇数长度时，mid指向的的是正中间那个元素的后面一个
        # 此时原链表head被切成head和mid两条链表

        # 递归，两条链表再次对半切开，直到每个链表只剩1个元素为止
        # left, right是两个指针，分别操作head 和 mid 两个链表
        # 递归至每个链表只有1个或0个元素的时候结束
        left, right = self.sortList_recursion(head), self.sortList_recursion(mid)

        # 递归结束后进行有序合并
        # 将左右指针较小的一方，添加到dummy中
        cur = dummy = ListNode(0)
        while left and right:  # 将较小的链表接入dummy，使得dummy链表最终有序
            if left.val < right.val:
                cur.next, left = left, left.next  # 将left链表接入dummy，并将left指针指向left的下个元素
            else:
                cur.next, right = right, right.next
            cur = cur.next
        # While循环结束后，一定有一个列表是空的
        # 把未空的加到新建链表的尾部
        # 返回新建链表
        cur.next = left if left else right
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([-1, 5, 3, 4, 0])

    res = sol.sortList_recursion(l1)
    sol.print_LinkedList(res)
