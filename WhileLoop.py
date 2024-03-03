# n = int(input("Enter the Number of elements in list : "))
# List = list()
# print("Enter the List elements")
# for i in range(0, n):
#     List.append(int(input()))
# print(List) 

# a=1
# b= int(input("enter your no-"))
# while a<=b:
#     print(a,end=" ")
#     a+=1

# a=1
# n= int(input("enter your no-"))
# while n>=a:
#     print(n,end=" ")
#     n-=1

# a=int(input("enter your 1st no-"))
# b=int(input("enter your 2nd no-"))
# while a<=b:
#     print(a, end=" ")
#     a+=1


# i=1
# a=1
# while i<=5:
#     a=a*i
#     i+=1
# print(a, end=" ")/

# a=1
# count=0
# while a<=100:
#     if a%7==0:
#         count=count+1
#     a+=1
# print(count,end=" ")

# a=1
# count=0
# while a<=200:
#     if a%6==0 and a%7==0:
#         print(a, end=" ")
#         count+=1
#     a+=1
# print(count,sep=' ', end="\n")

a=20
count=0
while a<=50:
    if a%4==0:
        print(a)
        count+=1
    a+=1
print(count,end=" ")