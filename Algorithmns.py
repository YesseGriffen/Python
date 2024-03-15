##Need working, Get iters for merge and make quickSort

#Sorting Algorthims
dArr = [4, 2, 0, 5, 1, 7, 8, 3, 1, 8, 5]
#Bubblesort basically swaps the positions of the biggest numbers so they appear at the end, bubbling up.
def bubbleSort(arr):
    iters = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            iters += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Iters: ", iters)


#Insertionsort starts with an element "current" and compares up the list. once swaps are done it will even compare the swapped element with the element behind it if it can.
def insertionSort(arr):
    iters = 0
    for i  in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            iters += 1
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = current
    print("Iters: ", iters)



#Cant get iters with recursive without another function or something similiar 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i, j, k = 0, 0, 0

        while i < len(leftHalf) and j < len(rightHalf):
            if(leftHalf[i] < rightHalf[j]):
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[i]
            j += 1
            k += 1







def allSorts():
    uin = int(input("Selection: 1,2,3,4: "))
    if uin == 1:
        bubbleSort(dArr)
        print(dArr)
    elif uin == 2:
        insertionSort(dArr)
        print(dArr)
    elif uin == 3:
        mergeSort(dArr)
        print(dArr)
    elif uin == 4:
        print("Working on QuickSort")


#Test sorts.
allSorts()





#Search Algorithmns

#Need work on.

def binarySearch(arr, target):
    low, high = 0, len(arr) - 1 #setting 2 different variables one at the left side 0 and one at the right max of arr.

    while low <= high:
        mid = (low + high) // 2
        midN = arr[mid]

        if midN == target:
            return mid
        elif midN < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

