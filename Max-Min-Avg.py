"""max-min-avg"""
import json

def main():
    """main"""
    my_list = json.loads(input())
    if len(my_list) > 1:
        low = my_list[0]
        high = my_list[1]
        for i in my_list:
            if i < low:
                low = i
            if i > high:
                high = i
        low = round(low, 2)
        high = round(high, 2)
        aver = round(sum(my_list)/len(my_list), 2)
        output = (high, low, aver)
        print(output)
    else:
        my_list = round(my_list[0], 2)
        output = (my_list, my_list, my_list)
        print(output)
main()
