# def add(lst):
#     return sum(lst)

# lst=[1,2,3,4,5]
# temp=add(lst)
# print(temp)

# def num(a):
#    return sum(a)
# a={1,2,3,4}
# a=num(a)
# print(a)


# #Function Creation
# def odd_even(num):
#     if num%2==0:
#       return"even"
#     else:
#       return"odd"


# #Function Calling / Function Use
# for i in range (1,10):
#    num=odd_even(i)
#    print(num,end=" ")


# def greet():
#     print('Hello World!')

# greet()
# print("jay sri ram")
# print('Outside function')

# def power(x=1,y=1):
#     return x+y
# a=power()
# print(a)


# def sum(a,b):
#     return a**b

# x=sum(b=4,a=3)
# print(x)

# for i in "Satya Sanatan Bastia" :
#     print(i)

# student_scores = {"John": 85,
#                    "Alice": 90, 
#                    "Bob": 78}
# # for name, score in student_scores.items():
# #     print(f"{name} scored {score}")

# print(type("student_scores"))

# def name(n='Sanatan'):
#     return 'Satya '+ n +' Bastia'

# a=name('Sonu')
# print(a)

# #*args--------------------------------
# def sum(*args):
#     a=1
#     for i in args:
#         a=a+i
#     return a
# print(sum(2,2,2,25,5,8,8,7,7,9,9,6,6,1,1))


# def mul(*sonu):
#     a=1
#     for i in sonu:
#         a=a*i
#     return a
# print(mul(66,55,7,8,66))


#  #**kwargs------------------------------

# def satya(**kwargs):
#     for (key,value) in kwargs.items():
#         print(key,'---->',value)

# satya(name='grty',age=89)


# def driems(**kwargs):
#     for a,b in kwargs.items():
#         print(a,"---->",b)
    
# driems(clg="Driems University", Loc="tangi", district ='cuttack',pin=7676869 )
# print("ram")

# def check_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Test the function
# num = int(input("Enter a number: "))
# result = check_odd_even(num)
# print(f"The number {num} is {result}.")


# def satya():
#     return 9
# print(type(satya))

# l=[1,2,3,satya]
# print(l)
# print(l[-1])


# a=lambda x,y : x+y
# print(a(4,5))

# a= lambda x: x**2
# print(a(5))


# for i in range (1,100):
#     print(i)

# a= lambda x,y : x**y
# print(a(3,4))

# a= lambda a: "even" if a%2==0 else "odd"
# print(a(55))

# a= lambda a,b : a if a>b else b
# print(a(5,2))

