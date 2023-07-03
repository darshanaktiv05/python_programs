# anagram program

s_1 = input("Enter first string: ")
s_2 = input("Enter second string: ")

if sorted(s_1) == sorted(s_2):
    print("These strings are anagram string.")
else:
    print("These strings are not anagram string.")
