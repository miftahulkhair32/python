data = [1,2,3,4,5]

print ('sekarang :',data)
x = data.pop()
print ('berubah :',data)
print ('yang diambil :',x)


# penting import library
from collections import deque

data1 = deque([1,2,3,4])

y = data1.popleft()
print ('berubah : ',data1)
print ('yang diambil : ',y)

print (70*'=')

# untuk mengetahui ukuran data dari list dan tuple
import sys
l = [1,2,3,4,5,'ade','jafar','idul',True]
t = (1,2,3,4,5,'ade','jafar','idul',True)

dataList = sys.getsizeof(l)
dataTuple = sys.getsizeof(t)

print ('besar data list :',dataList)
print ('besar data tuple :',dataTuple)

print (70*'+')
# print (dir(t))
print (70*'=')

# untuk mengetahui waktu proses
import timeit
dataList1 = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
dataTuple1 = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print ('waktu proses list :',dataList1)
print ('waktu proses tuple :',dataTuple1)