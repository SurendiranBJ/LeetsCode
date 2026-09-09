# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre=None
        if head is None:
            return head
        while head and head.val==val:
            head=head.next    
        curr=head    
        while curr:
            if curr.val==val:
                pre.next=curr.next
            else:    
                pre=curr
            curr=curr.next
        return head