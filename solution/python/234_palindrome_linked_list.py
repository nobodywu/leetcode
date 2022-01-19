# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
        nodes = []
        cur_node = head

        while cur_node:
            nodes.append(cur_node.val)
            cur_node = cur_node.next

        # nodes[::-1] 逆序。不能使用nodes.reverse()，无返回值
        return nodes == nodes[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        def find_first_half_end(node: ListNode):
            '''
            使用快慢指针查找链表中间位置
            '''
            slow = node
            fast = node

            while fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse_list(node: ListNode):
            '''
            翻转链表
            '''
            current = node
            previous = None

            while current != None:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            return previous

        first_half_end = find_first_half_end(head)
        second_half_end = reverse_list(first_half_end.next)  # 翻转后为后半部分链表的开始

        # 判断两个链表是否相等
        found = True
        p1 = head
        p2 = second_half_end
        while found and p2 != None:
            if p1.val != p2.val:
                found = False

            p1 = p1.next
            p2 = p2.next

        first_half_end.next = reverse_list(second_half_end)  # 恢复链表
        return found


if __name__ == "__main__":
    s = Solution()

    l1 = [1, 2, 2, 1]
    l2 = [1, 2]

    ln = ListNode(-1)
    dummy = ln
    for each in l1:
        n = ListNode(each)
        dummy.next = n
        dummy = dummy.next

    print(s.isPalindrome1(ln.next))
