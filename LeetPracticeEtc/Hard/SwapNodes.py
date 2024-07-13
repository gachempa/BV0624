# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# v messy solution ... don't like it 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next==None: return head

        if head.next and head.next.next==None:
            a=head
            b=head.next
            head=b
            head.next=a
            a.next=None
            return head

        bprev=eprev=e=head
        eptr=1

        while e:
            if k>1 and eptr==k-1:
                bprev=e
            if eptr>k+1:
                eprev=eprev.next
            if e.next and e.next.next==None:
                eprevk1=e #eprev to use for k=1
            e=e.next
            eptr+=1
        # print(eptr)
        if k==1 or k==eptr-1:
            last = eprevk1.next
            h=head
            b2=head.next
            head=last
            head.next=b2
            eprevk1.next=h
            h.next=None
            return head
        else:            
            e2=eprev.next.next
            e=eprev.next
            b2=bprev.next.next
            b=bprev.next
            # if the nodes to swap are adjacent to each other
            # below code can be compressed ... but works
            if e.next==b:
                t=b.next
                b.next=e
                e.next=t
                eprev.next=b
                return head
            elif b.next==e:
                t=e.next
                e.next=b
                b.next=t
                bprev.next=e
                return head
            else:
                bprev.next=e
                e.next=b2
                eprev.next=b
                b.next=e2
                return head
        
        # bprev.next=eprev
        # print(e)
        # print(bprev)
        # print(eprev)
        # return head