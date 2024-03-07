"""Sorting Name (Sorting)"""

def getname():
    """Get name"""
    step = int(input())
    allname = []
    for _ in range(step):
        name = input()
        allname.append(name)
    return allname

def quicksord(arr):
    """quicksord"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksord(left) + [pivot] + quicksord(right)

def rieng():
    """rieng"""
    name = quicksord(getname())
    #print("--------------------")
    for i in name:
        i = i.split()
        print(i[0].capitalize(), i[1].capitalize())

rieng()
