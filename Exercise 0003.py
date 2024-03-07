"""Sorting Name (Sorting)"""

def getname():
    """Get name"""
    step = int(input())
    allname = []
    for _ in range(step):
        name = input()
        allname.append(name)
    return allname

def mergesord(arr):
    """mergesord"""
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesord(left)
        mergesord(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def rieng():
    """rieng"""
    name = getname()
    mergesord(name)
    #print("--------------------")
    for i in name:
        i = i.split()
        print(i[0].capitalize(), i[1].capitalize())

rieng()
