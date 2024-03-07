"""bubbleSort"""
import json

def compare(elem1, elem2):
    """Comparison function"""
    if elem1[0] != elem2[0]:
        return elem1[0] < elem2[0]
    else:
        return int(elem1[1:]) < int(elem2[1:])

def bubblesort(listt, last):
    """bubbleSort"""
    count = 0
    current = 0
    issorted = False
    while current <= last and not issorted:
        walker = last
        issorted = True
        while walker > current:
            if compare(listt[walker], listt[walker - 1]):
                issorted = False
                listt[walker], listt[walker - 1] = listt[walker - 1], listt[walker]
            walker -= 1
            count += 1
        current += 1
        print(listt)
    print("Comparison times:", count)

def main():
    """main"""
    input1 = input()
    input1 = input1.replace("'", '"')
    bubblesort(json.loads(input1), int(input()))

main()
