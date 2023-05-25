import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "当前节点： {} @ <{}>".format(self.val, id(self))


class BaseSolution:
    def create_linklist_tail(self, li):
        """尾插法将列表转换成链表的头节点"""
        head = ListNode(li[0])
        tail = head
        for element in li[1:]:
            node = ListNode(element)
            tail.next = node
            tail = node
        return head

    def print_LinkedList(self, res: ListNode):
        """print a LinkedList node by node from beginning to the end"""
        if res:
            output = []
            output.append(res.val)
            while res.next:
                res = res.next

                output.append(res.val)
            return output if output else None

    def create_linklist_with_circle(self, li, pos):
        """ 尾插法生成带有环的链表 """
        head = ListNode(li[0])
        tail = head
        length = len(li)
        first_in_circle = None

        for i, item in enumerate(li[1:]):
            node = ListNode(item)
            tail.next = node
            tail = node
            if i + 1 == pos:
                first_in_circle = tail

            if i + 1 == length - 1:
                tail.next = first_in_circle

        return head

    def merge_linklist_in_tail(self,old_li:ListNode, new_li: ListNode) -> None:
        while old_li and old_li.next:
            old_li = old_li.next
        old_li.next = new_li
