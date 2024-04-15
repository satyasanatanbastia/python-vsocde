# reverse a string
# with out using any pre build function

# str = input("Enter your string-")
# rev_str = ""
# for i in range(len(str) - 1, -1, -1):
#     # print(str[i])
#     rev_str = rev_str + str[i]
# print(f"Reverse string is{rev_str}")


# Program to check if the given character is a vowel or consonant using if-else
# char = input("enter yor charecter--")
# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("it is vowel")
# else:
#     print("its consonant")

# program to check whether the character is an alphabet or not

# char = input("enter yor charecter--")
# if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
#     print("It is alphabate")
# else:
#     print("It is not alphabate")


# Check whether a given character is upper case, lower case, number or special character
char = input("enter yor charecter--")
if char >= "a" and char <= "z":
    print("It is lowercase charecter")
elif char >= "A" and char <= "Z":
    print("It is uperrcase charecter")
elif int(char) >= 0 and int(char) <= 9:
    print("It is Number")
else:
    print("It is special charecter")
