from LinkedList import ListNode, BaseSolution


class Solution(BaseSolution):
    def isPalindrome(self, head: [ListNode]) -> bool:
        """
        判断一个链表是否为回文链表（Palindrome Linked List）
        通过使用快慢指针的方法，找到链表的中间位置，将链表从中间等分成左右两个链表。当链表长度为奇数时，中间节点位于左链表。
        然后，通过头插法（原地反转链表）将右链表反转。
        通过逐一比较左链表和反转后的右链表的节点值，判断是否相等。如果出现不相等的情况，将结果标记为 False。
        时间复杂度为 O(n)
        空间复杂度为 O(1),只使用了常数个额外变量来存储指针和一些临时节点，而不需要额外的数据结构或数组来存储链表的节点。
        """
        prev = None
        isOdd = False
        fast, slow = head, head
        while fast:  # 快慢指针找链表的中间位置，当链表长度为奇数时，中间节点位于左链表。
            fast = fast.next
            if fast:  # 每次循环fast走两步，如果最后一次循环只能走一步，说明是奇数长度
                fast = fast.next
            else:
                isOdd = True  # 长度为奇数
                break  # 结束循环，不再移动快慢指针

            # 慢指针，移动的同时 用头插法将左链表原地构造成逆序链表
            snext = slow.next  # 缓存slow.next的值，临时变量snext只产生O（1）的空间复杂度

            slow.next = prev
            prev = slow

            slow = snext

        # 原链表被从中间一分为二，并且前半部分已经逆序
        lpart, rpart = prev, slow
        # 用两个指针分别遍历前后部分，比较两个链表是否相同
        cur1, cur2 = lpart, rpart
        # 处理链表长度为奇数的情况，跳过中间数
        if isOdd:
            cur2 = cur2.next
        ans = True
        while cur1 and cur2:
            if cur1.val != cur2.val:
                ans = False
                break
            cur1 = cur1.next
            cur2 = cur2.next

        return ans


if __name__ == '__main__':
    sol = Solution()
    l1 = sol.create_linklist_tail([1, 2, 2, 1])

    print(sol.isPalindrome(head=l1))
