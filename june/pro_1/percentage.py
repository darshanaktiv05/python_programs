# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     l_o_a = len(student_marks[query_name]);
#     sum = sum(student_marks[query_name]);
#     average = sum / l_o_a;
#     print(f"{average:.2f}")


import numpy as np


np.set_printoptions(legacy='1.13')
print(np.eye(*map(int, input().split())))
