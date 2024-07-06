# for hard linked list prob - reverse k list

        cycle=0
        a=b=c=z=head
        b=a.next
        c=b.next

        def kloop(a,b,c,z,head):
            for i in range(k-1):
                z=z.next

            if z==None: return head
            if cycle==0: head=z
