"""insertionSort"""
import json

def compare(elem1, elem2):
    """Comparison function"""
    if elem1[0] != elem2[0]:
        return elem1[0] < elem2[0]
    else:
        return int(elem1[1:]) < int(elem2[1:])

def insertionsort(listt, last):
    """insertionsort"""
    count = 0
    for current in range(1, last+1):
        hold = listt[current]
        walker = current-1

        while walker >= 0:
            count += 1
            if compare(hold, listt[walker]):
                listt[walker+1] = listt[walker]
                walker -= 1
            else:
                break

        listt[walker+1] = hold
        print(listt)
    print("Comparison times:", count)

def main():
    """main"""
    input1 = input()
    input1 = input1.replace("'", '"')
    insertionsort(json.loads(input1), int(input()))

main()
