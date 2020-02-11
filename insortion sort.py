import random
A=[]
n=int(input("enter the size of matrix"))
for i in range(n):
    A.append(random.randint(1, 50))
print("unsorted array:",A)

for i in range(n):
    temp=A[i]
    j=i-1
    while temp<A[j] and j>=0:
        A[j+1]=A[j]
        j=j-1
    A[j+1]=temp
print("array is :",A)
