import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8]])
print('A:')
print A
#shallow copy
B = A[1:]
#changing a value in B will affect A
B[0,0] = 9

print('B:')
print B
print('A:')
print A

print('is B a view of A?')
print B.base is A

#deep copy
C = A[1:].copy()

#changing a value in C does not affect A
C[0,0] = 10

print('C:')
print C
print('A:')
print A