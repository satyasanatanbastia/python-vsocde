# a=[1,2,3]
# a.append(9)
# print(a)



#Create ATM System using python
# class Atm:

#   # constructor(special function)->superpower -> 
#   def __init__(self):
#     print(id(self))
#     self.pin = ''
#     self.balance = 0
#     #self.menu()

#   def menu(self):
#     user_input = input("""
#     Hi how can I help you?
#     1. Press 1 to create pin
#     2. Press 2 to change pin
#     3. Press 3 to check balance
#     4. Press 4 to withdraw
#     5. Anything else to exit
#     """)

#     if user_input == '1':
#       self.create_pin()
#     elif user_input == '2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input == '4':
#       self.withdraw()
#     else:
#       exit()

#   def create_pin(self):
#     user_pin = input('enter your pin')
#     self.pin = user_pin

#     user_balance = int(input('enter balance'))
#     self.balance = user_balance

#     print('pin created successfully')
#     self.menu()

#   def change_pin():
#     old_pin = input('enter old pin')

#     if old_pin == self.pin:
#       # let him change the pin
#       new_pin = input('enter new pin')
#       self.pin = new_pin
#       print('pin change successful')
#       self.menu()
#     else:
#       print('nai karne de sakta re baba')
#       self.menu()

#   def check_balance(self):
#     user_pin = input('enter your pin')
#     if user_pin == self.pin:
#       print('your balance is ',self.balance)
#     else:
#       print('chal nikal yahan se')

#   def withdraw(self):
#     user_pin = input('enter the pin')
#     if user_pin == self.pin:
#       # allow to withdraw
#       amount = int(input('enter the amount'))
#       if amount <= self.balance:
#         self.balance = self.balance - amount
#         print('withdrawl successful.balance is',self.balance)
#       else:
#         print('abe garib')
#     else:
#       print('sale chor')
#     self.menu()


# class demo:
#     def __init__(self):
#         print("jay sri ram")
# object=demo()



# class satya:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return f"{self.name}--{self.age}"

# obj1=satya("Satya",22)
# obj2=satya("sonu",33)
# print(obj1)
# print(obj2)


# class shell:
#     def __init__(self,name, age, gender):
#         self.name=name
#         self.age=age
#         self.gennder=gender
#     def check(self):
#         if self.gennder == "male":
#             return "hello ji"
#         else:
#             return "hii ji"
        
# a=shell("satya", 21, "male")
# # print(a.check())
# a.country="india"
# print(a.country)

# class radaha:
#     name="sonu"
#     age=34
#     pin=4567
# s1=radaha()
# print(s1.pin)


#<<<<<<-------------------------------------------------------------------------------------------------------------->>>>>>


