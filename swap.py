# a=5
# b=4
# a=a+b
# print(a)
# b=a-b
# print("b=",b)
# a=a-b
# print("a=",a)

# a=3
# b=5
# c=a
# a=b
# b=c
# print("a=",a)
# print("b=",b)

# a="satya"
# print(f"my name is-{a}")

# x=int(input("enter 1st no-"))
# y=int(input("enter 2nd no-"))
# z=x+y
# print(z)

# x="990"
# print(x,type(x))
# y=int(x)
# print(y,type(y))

# length=float(input("enter length of triangle-"))
# breadth=float(input("enter breadth of triangle-"))
# area=length*breadth
# print(f"area={area}")

# x=int(input("enter your 1st number-"))
# y=int(input("enter your 2nd number-"))
# z=int(input("enter your 3rd number-"))
# k=(x+y+z)/3
# print(k)

# f=float(input("enter your fahrehnheite value-"))
# c=(f-32)*5/9
# print(f"celcious={c}")

# fullmark=500
# physics=float(input("Enter your physics mark-"))
# math=float(input("Enter your math mark-"))
# chemistry=float(input("Enter your chemistry mark-"))
# sanskrit=float(input("Enter your sanskrit mark-"))
# odia=float(input("Enter your odia mark-"))
# total_mark=physics+math+chemistry+sanskrit+odia
# avg_percentage=(total_mark/500)*100
# print(f"Total mark is {total_mark} out of {fullmark}")
# print(f"Total Percentage is {avg_percentage}%")

# n=int(input())
# if (n%2)==0 and range(2,5):
#     print("Not Weird")
# elif (n%2)==0 and range(6,20):
#     print("Weird")
# elif (n%2)==0 and range(20):
#     print("Weird")
# else:
#     print("Weird")

n = int(input())
if n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")

