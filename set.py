# a={(1,2,3),"hello"}
# print(a)
a={1,2,3,4,'aa'}
print(a)
print(id(a))
b=list(a)
b[2]=8
print(b)
a=set(b)
print(type(a))
print(id(a))