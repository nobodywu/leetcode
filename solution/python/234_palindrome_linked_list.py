# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        cur_node = head

        while cur_node:
            nodes.append(cur_node.val)
            cur_node = cur_node.next

        # nodes[::-1] 逆序。不能使用nodes.reverse()，无返回值
        return nodes == nodes[::-1]
