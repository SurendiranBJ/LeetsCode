# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        pre=None
        while fast and fast.next:
            if fast==slow and pre is not None:
                print(fast,slow)
                return True
            else:
                slow=slow.next
                fast=fast.next.next
                pre=slow
        return False            