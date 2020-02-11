import random
n=int(input("enter the size of matrix"))
A= []
B= []
for i in range(n):
    A.append(random.randint(1, 100))
for i in range(n):
    B.append(random.randint(1, 100))
print(A)
print(B)
for i in range(n+1):
    for j in range(n - i):
        if A[j]>A[j-1]:
            A[j-1],A[j]=A[j],A[j-1]

print("****************************")
for i in range(n-1):
    for j in range(n-i):
        if B[j]<B[j-1]:
           B[j-1],B[j]=B[j-1],B[j-1]


print(A)

print(B)