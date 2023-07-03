#
# def ffive(n):
#     for i in range(0, n+1):
#
#         for j in range(0, i + 1):
#             print("5", end="")
#         print("\r")
#
# n = 5
# ffive(n)


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2!= 0:
#         print('Weird')
#     else:
#         if n>=2 and n<=5:
#             print('Not Weird')
#         elif n>=6 and n <= 20:
#             print('Weird')
#         elif n > 20:
#             print('Not Weird')

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i**2)
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):
#         print(i,"\r")
#
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     l = []
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if i+j+k == n:
#                     continue
#                 l.append([i,j,k])
#     print(l)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])

