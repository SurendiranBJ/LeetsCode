# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        while head.val in nums:
            head=head.next
        dum=ListNode(head.val)
        pre=dum
        head=head.next
        while head:
            if head.val in nums:
                head=head.next
                continue
            else:
                pre.next=ListNode(head.val)
                pre=pre.next
                head=head.next
        return dum