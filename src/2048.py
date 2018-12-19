"""
    ProductName:2048
    Author:Sword
    ModefiedTime:2018-12-17
"""
import random

matrix = [[0 for n in range(4)] for m in range(4)]
score = 0

# 初始化游戏
def init():
    initNumFlag = 0
    while True:
        s = divmod(random.randrange(0, 16), 4)
        if matrix[s[0]][s[1]] == 0:
            matrix[s[0]][s[1]] = 2
            initNumFlag += 1
        if initNumFlag == 2:
            break

# 0值判断
def notzero(s):
    return s if s != 0 else ''

# 显示结果
def display():
    print(r"----------------------------2048----------------------------")
    print(r"操作说明： 上（W） 下（S） 左（A） 右（D） 退出（Q）")
    print(r"总分：%d" % score)
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

# 随机生成新的数字2
def randomNum():
    initNumFlag = 0
    while True:
        s = divmod(random.randrange(0, 16), 4)
        if matrix[s[0]][s[1]] == 0:
            matrix[s[0]][s[1]] = 2
            initNumFlag = 1
        if initNumFlag == 1:
            break

# 往左移动
def moveLeft():
	for i in range(4):
		for j in range(3):
			for k in range(j+1, 4):
				if matrix[i][j] == 0 and matrix[i][k] > 0:
					matrix[i][j] = matrix[i][k]
					matrix[i][k] = 0
				elif matrix[i][j] > 0 and matrix[i][j] == matrix[i][k]:
					matrix[i][j] = matrix[i][j] + matrix[i][k]					
					matrix[i][k] = 0
					global score 
					score += matrix[i][j]
					break;
				elif matrix[i][j] > 0 and matrix[i][k] > 0 \
					and matrix[i][j] != matrix[i][k]:
					matrix[i][j+1] = matrix[i][k]
					if k != j + 1:
						matrix[i][k] = 0
					break;

# 往右移动
def moveRight():
	for i in range(4):
		for j in range(3, -1, -1):
			for k in range(j-1, -1, -1):
				if matrix[i][j] == 0 and matrix[i][k] > 0:
					matrix[i][j] = matrix[i][k]
					matrix[i][k] = 0
				elif matrix[i][j] > 0 and matrix[i][j] == matrix[i][k]:
					matrix[i][j] = matrix[i][j] + matrix[i][k]
					matrix[i][k] = 0
					global score
					score += matrix[i][j]
					break;
				elif matrix[i][j] > 0 and matrix[i][k] > 0 \
					and matrix[i][j] != matrix[i][k]:
					matrix[i][j-1] = matrix[i][k]
					if k != j - 1:
						matrix[i][k] = 0
					break;				

# 往上移动
def moveUp():
	for j in range(4):
		for i in range(3):
			for k in range(i+1, 4):
				if matrix[i][j] == 0 and matrix[k][j] > 0:
					matrix[i][j] = matrix[k][j]
					matrix[k][j] = 0
				elif matrix[i][j] > 0 and matrix[i][j] == matrix[k][j]:
					matrix[i][j] = matrix[i][j] + matrix[k][j]
					matrix[k][j] = 0
					global score
					score += matrix[i][j]
					break;
				elif matrix[i][j] > 0 and matrix[k][j] > 0 \
					and matrix[i][j] != matrix[k][j]:
					matrix[i+1][j] = matrix[k][j]
					if k != i + 1:
						matrix[k][j] = 0
					break;

# 往下移动
def moveDown():
	for j in range(4):
		for i in range(3, -1, -1):
			for k in range(i-1, -1, -1):
				if matrix[i][j] == 0 and matrix[k][j] > 0:
					matrix[i][j] = matrix[k][j]
					matrix[k][j] = 0
				elif matrix[i][j] > 0 and matrix[i][j] == matrix[k][j]:
					matrix[i][j] = matrix[i][j] + matrix[k][j]
					matrix[k][j] = 0
					global score
					score += matrix[i][j]
					break;
				elif matrix[i][j] > 0 and matrix[k][j] > 0 \
					and matrix[i][j] != matrix[k][j]:
					matrix[i-1][j] = matrix[k][j]
					if k != i - 1:
						matrix[k][j] = 0
					break;	

#判断游戏状态，是否结束
def gameOver():
	gameoverFlag = True
	for i in range(4):
		for j in range(4):
			if matrix[i][j] == 0:
				gameoverFlag = False
				break
		if gameoverFlag == False:
			break;
	return gameoverFlag

# 主程序
def main():
    init()
    display()
    while True:
    	d = input()
    	if d == 'q' or d == 'Q':
    		print("退出游戏，本次得分为：%d" % score)
    		break
    	elif d == 'w' or d == 'W':
    		print("上")
    		moveUp()
    		randomNum()
    		display()
    	elif d == 's' or d == 'S':
    		print("下")
    		moveDown()
    		randomNum()
    		display()
    	elif d == 'a' or d == 'A':
    		moveLeft()
    		print("左")
    		randomNum()
    		display()
    	elif d == 'd' or d == 'D':
    		print("右")
    		moveRight()
    		randomNum()
    		display()
    	if gameOver() == True:
    		print("游戏结束，本次得分为：%d" % score)
    		break;
    	
if __name__ == "__main__":
    main()