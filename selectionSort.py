"""selectionSort"""
import json

def compare(elem1, elem2):
    """Comparison function"""
    if elem1[0] != elem2[0]:
        return elem1[0] < elem2[0]
    else:
        return int(elem1[1:]) < int(elem2[1:])

def selectionsort(listt, last):
    """selection sort"""
    count = 0
    for i in range(last):
        small = i
        for j in range(i+1, last+1):
            count += 1
            if compare(listt[j], listt[small]):
                small = j
        listt[i], listt[small] = listt[small], listt[i]
        print(listt)
    print("Comparison times:", count)

def main():
    """main"""
    input1 = input()
    input1 = input1.replace("'", '"')
    selectionsort(json.loads(input1), int(input()))

main()
