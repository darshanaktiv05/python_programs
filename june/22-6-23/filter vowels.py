# filter string from entered string

# S1 = "string are used for storing text for example hello world is a string fo characters."
S1 = input("enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

new_string = list(filter(lambda x: (i in x for i in vowels), S1))

print(new_string)
print("a is", new_string.count('a'), "times in this string.")
print("e is", new_string.count('e'), "times in this string.")
print("i is", new_string.count('i'), "times in this string.")
print("o is", new_string.count('o'), "times in this string.")
print("u is", new_string.count('u'), "times in this string.")
