#  test

nums=["1","2","3","4","5","6","7","8","9"]
exclude= {'3', '5', '6', '8', '4', '1', '7', '9', '2', '.'}
set_nums=set(nums)
if set_nums.issubset(exclude):
    print("yes")

# n=3
# k=3
# for i in range(k,k+3):
#     print(i)

# q1=int(n/k)
# q,r=divmod(n,k)
# print(q1)