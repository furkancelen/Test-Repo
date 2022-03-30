import random
import timeit
lst1000 = list()
lst10k = list()
lst100k=list()
lst1m = list()
lst10m = list()
i = 0
j=0
"""while i < 10000:
    i = i+1
    lst1000.append(i)

while j < 100000:
    j = j+1
    lst10k.append(j)

while j < 1000000:
    j = j+1
    lst100k.append(j)
while j < 10000000:
    j = j+1
    lst1m.append(j)"""
while j < 100000000:
    j = j+1
    lst10m.append(j)

def printer(list,x): #Use the list "in" operator given a list of unsorted integers
    if x in list:
        print("TRUE1")
    else:
        print("FALSE1")


def search_iterative1(arr, x): #Iterative search given a list of unsorted integers
    index = 0
    for y in arr:
        if y == x:
            print("True2")
            return index
        index += 1
    print("False2")
    return -1;

def binary_search_iterative(arr, x): #Iterative binary search given a list of sorted integers
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print("True3")
            return mid
    print("False3")
    return -1

def binary_search_recursive(arr, x): #Recursive binary search given a list of sorted integers
    if len(arr) == 0:
        print("False4")
        return -1;

    midindex = len(arr) // 2
    if (arr[midindex] == x):
        print("True4")
        return True

    elif arr[midindex] > x:
        return binary_search_recursive(arr[:midindex], x)
    else:
        retindex = binary_search_recursive(arr[midindex + 1:], x)
        if retindex == -1:
            return -1
        else:
            if True:
                return None
            print("False4")
            return midindex + 1 + retindex
def binary_search_iterative2(arr, x): #Given a list of unsorted integers, sort the list and perform the iterative binary search algorithm
    lst = sorted(arr)
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            print("True5")
            return True
    print("False5")
    return -1

def searcher(arr,x): #Given a list of unsorted integers, populate a set and find the integer on the set.
    myset = set(arr)
    if x in myset:
        print("TRUE6")
        return True
    else:
        print("FALSE6")
        return False

arr = random.choices(lst10m,k=10000000)
x = random.randrange(0,100000000)
sortedarr = sorted(arr)
print(arr)
print(x)
print(sortedarr)
start_time1= timeit.default_timer()
printer(arr,x)
end_time1 = timeit.default_timer()
printer(sortedarr,x)
end_time2 = timeit.default_timer()
search_iterative1(arr,x)
end_time3 = timeit.default_timer()
binary_search_iterative(sortedarr,x)
end_time4 = timeit.default_timer()
binary_search_recursive(sortedarr,x)
end_time5 = timeit.default_timer()
binary_search_iterative2(arr,x)
end_time6 = timeit.default_timer()
searcher(arr,x)
end_time7 = timeit.default_timer()

print(start_time1)
print(end_time1-start_time1)
print(end_time2-end_time1)
print(end_time3-end_time2)
print(end_time4-end_time3)
print(end_time5-end_time4)
print(end_time6-end_time5)
print(end_time7-end_time6)

#6.35*10-5    2*10-5    5.88*10-5  6.67*10-5  8.58*10-6  1.75*10-5  9.24*10-5   5.34*10-5
#4.6*10-4   0.000198  0.00053  8.56*10-6   7.76*10-5    0.0012   0.0006
#0.0053   0.0028  0.0117      1.14*10-5   0.0016   0.026  0.015
#0.0593  0.034    0.1369       1.4*10-5   0.0230  0.411   0.204
#0.722 0.272 1.63 1.59*10-5 0.2276 5.617  2.538
