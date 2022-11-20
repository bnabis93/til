# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while head:
            stack.append(head)
            head = head.next
        middle_idx = int(len(stack) /2 )
        return stack[middle_idx]
