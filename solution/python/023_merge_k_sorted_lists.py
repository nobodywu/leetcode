class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoSortedLists(self, x, y):
        a = ListNode(0)
        b = a

        while x != None and y != None:
            if x.val < y.val:
                a.next = x
                x = x.next
            else:
                a.next = y
                y = y.next

            a = a.next

        a.next = x if x != None else y

        return b.next

    def mergeKLists(self, lists) -> ListNode:
        length = len(lists)

        if 0 == length:
            return
        
        if 1 == length:
            return lists[0]

        mid = length // 2

        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])

        return self.mergeTwoSortedLists(l1, l2)


if __name__ == "__main__":
    # 两个链表是有序的
    # 2 -> 3 -> 4
    nodelist1 = ListNode(2)
    nodelist1.next = ListNode(3)
    nodelist1.next.next = ListNode(4)

    # 1 -> 6 -> 7
    nodelist2 = ListNode(1)
    nodelist2.next = ListNode(6)
    nodelist2.next.next = ListNode(7)

    # 2 -> 7 -> 11
    nodelist3 = ListNode(2)
    nodelist3.next = ListNode(7)
    nodelist3.next.next = ListNode(11)

    # 3 -> 4 -> 5
    nodelist4 = ListNode(3)
    nodelist4.next = ListNode(4)
    nodelist4.next.next = ListNode(5)

    s = Solution()
    a = s.mergeKLists([nodelist1, nodelist2, nodelist3, nodelist4])
    
    if None != a:
        print(a.val)
        while None != a.next:
            a = a.next
            print(a.val)