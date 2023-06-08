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

    def sortList_iteration(self, head: ListNode) -> ListNode:
        """
        迭代实现的归并排序算法，有点复杂。

        intv定义了当前待合并的子链长度，当此长度大于等于链表长度时，结束合并

        算法首先迭代地获取子链表，然后归并排序。

        时间复杂度： O(n log n)
        空间复杂度： O(1)
        """

        cur = head
        length = 0
        intv = 1  # 待合并的链表长度

        # 求链表长度，
        while cur:
            cur = cur.next
            length = length + 1

        # 给原链表添加dummy节点
        dummy = ListNode(0)
        dummy.next = head

        # 将子链表合并.
        while intv < length:
            pre = dummy  # 用于合并链表的指针
            h = dummy.next  # 用于获取子链表的指针，h每次沿原链表从头遍历到尾
            while h:
                # get the two merge head `h1`, `h2`
                h1 = h
                i = intv
                while i and h:
                    h = h.next
                    i = i - 1
                if i:  # h走完，i还不为0，说明h1子链表长度等于原链表
                    break  # no need to merge because the `h2` is None.
                h2 = h
                i = intv
                while i and h:
                    h = h.next
                    i = i - 1

                c1 = intv  # h1的长度（元素数量）
                c2 = intv - i  # h2的长度（元素数量），可能小于intv

                # 合并h1和h2
                while c1 and c2:  # 当h1和h2内都存在元素时，执行归并排序
                    # 将两个子链表较小的一个先插入到pre.next
                    # 循环结束后一定会剩下一个子链表还有残余
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        c1 = c1 - 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        c2 = c2 - 1
                    pre = pre.next

                pre.next = h1 if c1 else h2  # 归并结束后，将还有残余的子链表直接加到合并后的链表后面

                while c1 > 0 or c2 > 0:  # 将pre指针相应地向后移动
                    pre = pre.next
                    c1 = c1 - 1
                    c2 = c2 - 1
                pre.next = h
            intv *= 2  # 将子链表的宽度扩大一倍
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([-1, 5, 3, 4, 0])

    res = sol.sortList_iteration(l1)
    sol.print_LinkedList(res)
