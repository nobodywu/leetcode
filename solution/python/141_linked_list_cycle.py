# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = []

        # 如果没有环，则一定会跳出这个循环
        while head:
            if head in visited:
                return True

            visited.append(head) # 添加的是对象
            head = head.next

        return False

if __name__ == "__main__":
    # 需要补充测试用例
    pass