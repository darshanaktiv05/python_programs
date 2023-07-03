# def split_and_join(line):
#     a = line.split(" ")
#     f = "-".join(a)
#     return f
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# def print_full_name(first, last):
#     # Write your code here
#     return print(f" Hello {first_name} {last_name}! You just delved into python.")
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def count_substring(string, sub_string):
#     string=string.lower()
#     substring=sub_string.lower()
#     lensub=len(substring)
#     i=0
#     while True:
#         if substring==string[0:lensub]:
#             i += 1
#         string=string[1:len(string)+1]
#         if len(string)<len(substring):
#             break
#     return i
#
#
# string = input().strip()
# sub_string = input().strip()
#
# count = count_substring(string, sub_string)
# print(count)
#Replace all ______ with rjust, ljust or center.

#Replace all ______ with rjust, ljust or center.
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(5):
    print(('H'*i).rjust(5-1,' ') + 'H' + ('H'*i).ljust(5-1,' '))

#Top Pillars
for i in range(5+1):
    print(('H'*5).center(5*2,' ')+('H'*5).center(5*6,' '))

#Middle Belt
for i in range((5+1)//2):
    print(('H'*5*5).center(5*6,' '))

#Bottom Pillars
for i in range(5+1):
    print(('H'*5).center(5*2,' ')+('H'*5).center(5*6,' '))

#Bottom Cone
for i in range(5):
    print(((c*(5-i-1)).rjust(5,' ')+c+(c*(5-i-1)).ljust(5)).rjust(5*6,' '))