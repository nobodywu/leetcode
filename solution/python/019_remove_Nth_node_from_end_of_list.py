# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 复制一个链表
        dummy = ListNode(0, head)

        # 统计链表长度
        count = 0
        # 不是 head.var != None
        while head != None:
            count += 1
            head = head.next

        # 为链表增加一个tag
        cur = dummy
        # count = 3
        #count - 2 + 1 =2
        # i = 1
        for i in range(1, count - n + 1):
            cur = cur.next

        # 只需要移动一次即可
        # 当前cur.val = 2
        cur.next = cur.next.next

        return dummy.next




if __name__ == "__main__":
    # 2 -> 4 -> 3 -> 5 -> 9
    nodelist1 = ListNode(2)
    nodelist1.next = ListNode(4)
    nodelist1.next.next = ListNode(3)
    nodelist1.next.next.next = ListNode(5)
    nodelist1.next.next.next.next = ListNode(9)

    s = Solution()
    a = s.removeNthFromEnd(nodelist1, 2)
    
    if None != a:
        print(a.val)
        while None != a.next:
            a = a.next
            print(a.val)