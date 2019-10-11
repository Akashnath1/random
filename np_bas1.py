import numpy as np
#hello world
# a = np.array([[2, 4, 6,8, 10, 12], [1, 3, 5, 7, 9, 11]])  # normal array
# b = np.array([[(2, 5, 6), (3, 4)], [2, 3, 4]])  # list into arrat
# c = np.array([[2, 3, 4], [3, 4, 5]], dtype=complex)  # complex data type
# print(b.shape)
# print(b)
# print(a.shape)
# print(c)
#
# d = np.zeros((2, 3))
# print(d)
#
# e = np.ones([3,3])
# print(e)
#
# print (a [1,2]) # specific value [row, column]
# print(a[1, :]) # whole row
# print (a[:, 2]) # whole column
# print(a[1, 1:5:2])
# a[1, :] = 2
# a [1,2] = 5
# print(a)
# g = np.array([[[2,3], [4,5], [6,7]], [[1,3], [5,7], [9,11]]])
# print(g)
#
# print(g[0,:,:])
# h = np.full([3,3], 100, dtype=float)
# print(h)
# i = np.full_like(a,5)
# print(i)
# k = np.random.rand(2, 3, 3)
# print(k)
# j = np.random.randint(1,2, size=(3,4,2))
# print(j)
# l = np.identity(7)
# print(l)
# m= np.array([[1,2,3,4]])
# n = np.repeat(m, 4, axis=0)
# print(n)
# o = m.copy()
# print(m)

#Mathematical operations
# aa = np.array([1,2,3,4])
# print(aa)
# print(aa+2)
# print(aa-4)
# print(aa*5)
# print(np.sin(aa))

# a = np.array([1,2,3])
# b = np.full_like(a,3)
# d = np.random.rand(3,3)
# print(a)
# print(d)
# c = np.matmul(a,d)
# print(c)

# num = np.array([[1,2,3,4], [12,13,14,14]])
# print(num)
# print(num.ndim)
# print(np.sum(num,axis=1))
#
# a= np.array([[1,2,4,3], [3,4,4,5]])
# print(a)
# b = a.reshape(2,2,2)
# print(b)
c = np.array([1,2,3,4,4,5])
d = np.array([2,34,45,533,4,5])
print(np.vstack([c,d]))
print(np.hstack([c,d]))
#load data from text file
e = np.genfromtxt('text1.txt', delimiter=',')
print(e)
f = e.astype(int)
print(f)
print(f[f > 15])
print(np.any(f>15, axis=0))

