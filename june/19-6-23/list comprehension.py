l1 = ['smit', 'sneha', 'sagar', 'samar']

newl = [i for i in l1 if 'a' in i]

print(newl)

new_list = [i for i in l1 if i != 'sanket']

print(new_list)

List_1 = [i for i in range(0, 20, 5)]
print(List_1)

my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_lst = [i ** 3 for i in my_lst[::-1] if i % 2 == 0]
print(my_lst)

mylist = [5, 4, 3, 2, 1]

mylist.sort()

print(mylist)
ML = ["even" if x % 2 == 0 else "odd" for x in range(1, 10)]
print((ML))

l1 = [5, 4, 3, 2, 1]
l2 = [5, 4, 3, 2, 1]
l2.sort()
print(l2)
l1.append(l2)
print(l1)
