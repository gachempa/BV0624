# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        for _ in range(2):
            if not curr: return head
            curr=curr.next
        
        prev=None
        curr=head
        for _ in range(2):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        head.next=self.swapPairs(curr)
        return prev