#Print the following pattern.
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()


#Print the following pattern.
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()



#Print the following pattern.
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()



#Print the following pattern.
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()



#Print the following pattern.
# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 
# for i in range(5,0,-1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()



#Ask N from user. N means number of lines. Then print the following pattern.
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# n=int(input("Enter your No-"))
# for i in range (1,n+1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()



# Ask N from user. N means number of lines. Then print the following pattern. 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1
# n=int(input("Enter your No-"))
# for i in range (n,0,-1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()



#_______________________Advance Nested Loop Prtice___________________________



# Print the following pattern.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j ,end=" ")
#     print()


#. Print the following pattern.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


#Print the following pattern1 
# 1
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


#Print the following pattern
# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


#Print the following pattern
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end=" ")
#     print()


#Print the following pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#Print the following pattern.
# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


#Print the following pattern.
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()


#Print the following pattern.
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


#Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


#Print the following pattern.
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

# start = 1
# for i in range(1, 6):
#     for j in range(i):
#         print(start, end=' ')
#         start += 1
#     print()

