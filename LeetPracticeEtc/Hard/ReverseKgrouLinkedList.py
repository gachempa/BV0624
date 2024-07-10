# Leetcode: https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/1316713014/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1: return head
        if not head: return head

        a=b=c=e=head
        n=1
        k1=1
        q=1
        heads, tails = [],[]

        while a:
            if k1==1: heads.append(a)
            if k1==k: tails.append(a)
            n+=1
            k1+=1
            if k1==k+1: k1=1
            a=a.next
        if len(heads)>len(tails): heads.pop() 

        head=tails[0]

        # print(len(heads))
        # return head     
        for i in range(len(heads)):
            a=heads[i]
            b=a.next
            c=b.next
            if n==k:
                e=tails[i]
            elif i==len(heads)-1:
                e=(tails[i].next)
            else:
                e=tails[i+1]
            a.next=e
            
            for j in range(k-1):
                b.next=a
                a=b
                b=c
                if b: c=b.next
                # if j==0:return head
        return head