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

# another try

        if k==1: return head
        if not head: return head

        a=b=c=e=head
        n=1
        while a.next:
            n+=1
            a=a.next
        a=b
        if n<k: return head

        q,r=divmod(n,k)
        # print(q)
        for i in range(q):
            e=b=a
            b=a.next
            
            if i==0:
                for _ in range(k-1):
                    head=head.next                
                # return head
            if i==q-1:
                for _ in range(k):
                    e=e.next 
            else:
                for _ in range(2*k-1):
                    e=e.next
            print(e)
            return head
            for j in range(k-1):
                if j==0:
                    a.next=e
                c=b.next
                b.next=a
                
                if j==k-2:
                    a=a.next.next
                    if a: b=a.next
                else:
                    a=b
                    b=a.next
                # return b
                
                    # print("j",j)
                    # return b            

        return head