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
        return "当前节点： {}".format(self.val)


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
            print(output if output else "None")

    def create_linklist_with_circle(self, li, pos):
        """ 头插法生成带有环的链表 """
        head = None
        length = len(li)

        last_before_circle = None

        for i, item in enumerate(li):
            new_node = ListNode(item)
            new_node.next = head
            head = new_node
            if i == pos:
                last_before_circle = head
            if i == length - 1:
                last_before_circle.next = head

        return head
