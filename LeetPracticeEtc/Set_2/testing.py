# for hard linked list prob - reverse k list

if k==1: return head

cycle=0
a0=a=b=c=z=head
b=a.next
c=b.next

def kloop(a0,a,b,c,z,head,cycle):

    for i in range(k-1):
        if not z.next: 
            return head
        else: 
            z=z.next
        
    if cycle==0: 
        head=z            
    else:
        cycle+=1
    # return head            
    for i in range(k):
        if i==k-1:
            if a.next:
                a0.next=z
                a=a.next
                z=a
                b=a.next
                c=b.next
                kloop(a0,a,b,c,z,head,cycle)
            else:
                return head
        else:
            b.next=a
            a=b
            b=c
            c=c.next
    
return kloop(a0,a,b,c,z,head,cycle)


# another try

        if k==1: return head

        a=b=k2=head
        x=1
        y=0

        for i in range(k-1):
            k2=k2.next
            head=head.next
            x+=1

        b=b.next

        while x>=0:
            x-=1
            if k2.next: 
                k2=k2.next
                y+=1

            a.next=b.next
            b.next=a
            a=a.next
            b=b.next

            if x==0 and y==k:
                x=k
                y=0