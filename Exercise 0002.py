""" ฝนตกไหม? ตากผ้าได้รึเปล่า?"""

def main():
    """main"""
    inout = input()
    sec = float(input())
    minute = sec//60
    if inout == "Indoor":
        print(minute >= 8)
    else:
        print(minute >= 4)
main()
