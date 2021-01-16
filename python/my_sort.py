import numpy as np
from timeit import default_timer as timer

# inherited and translated from c++ merge sort.
def mergeSort_init (v):
  temp = [0] * len(v)
  mergeSort_mid(v, temp, 0, len(v) - 1)


def mergeSort_mid (v, temp, start, end):
  if (start < end):    
    mid = int((start + end) / 2)
    
    mergeSort_mid(v, temp, start, mid)
    mergeSort_mid(v, temp, mid + 1, end)
    merge(v, temp, start, mid, end)
  


def merge(v, temp, start, mid, end): 
  leftpos = start
  rightpos = mid + 1
  temppos = start
  while (leftpos <= mid and rightpos <= end): 
    if (v[leftpos] < v[rightpos]): 
      temp[temppos] = v[leftpos]
      temppos += 1
      leftpos += 1
    else:
      temp[temppos] = v[rightpos]
      temppos += 1
      rightpos += 1
  
  while (leftpos <= mid):
    temp[temppos] = v[leftpos]
    temppos += 1
    leftpos += 1
  while (rightpos <= end):
    temp[temppos] = v[rightpos]
    temppos += 1
    rightpos += 1
  
  i = start
  while i <= end: 
    v[i] = temp[i]
    i += 1


list = [2,6,2,63,7,4,7,3,6] # change as needed
print("Before: ",list)

start = timer()
mergeSort_init(list)
print("After:  ", list)
end = timer()

print(end - start) # Time in seconds