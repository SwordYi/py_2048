"""
    ProductName:2048
    Author:Sword
    ModefiedTime:2018-12-17
"""
import random

matrix = [[0 for n in range(4)] for m in range(4)]

def init():
    initNumFlag = 0
    while True:
        s = divmod(random.randrange(0, 16), 4)
        if matrix[s[0]][s[1]] == 0:
            matrix[s[0]][s[1]] = 2
            initNumFlag += 1
        if initNumFlag == 2:
            break

def notzero(s):
    return s if s != 0 else ''

def display():
    print(r"----------------------------2048----------------------------")
    print(r"操作说明： 上（W） 下（S） 左（A） 右（D） 退出（Q）")
    print("\n\
        ┌────┬────┬────┬────┐\n\
        │%4s│%4s│%4s│%4s│\n\
        ├────┼────┼────┼────┤\n\
        │%4s│%4s│%4s│%4s│\n\
        ├────┼────┼────┼────┤\n\
        │%4s│%4s│%4s│%4s│\n\
        ├────┼────┼────┼────┤\n\
        │%4s│%4s│%4s│%4s│\n\
        └────┴────┴────┴────┘"
        %(notzero(matrix[0][0]), notzero(matrix[0][1]), notzero(matrix[0][2]), notzero(matrix[0][3]),
          notzero(matrix[1][0]), notzero(matrix[1][1]), notzero(matrix[1][2]), notzero(matrix[1][3]),
          notzero(matrix[2][0]), notzero(matrix[2][1]), notzero(matrix[2][2]), notzero(matrix[2][3]),
          notzero(matrix[3][0]), notzero(matrix[3][1]), notzero(matrix[3][2]), notzero(matrix[3][3]))
          )


def main():
    init()
    display()

if __name__ == "__main__":
    main()