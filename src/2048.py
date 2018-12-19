"""
    ProductName:2048
    Author:Sword
    CreateTime:2018-12-17
    ModefiedTime:2018-12-19
"""
import random, os

class Game:
	def __init__(self, _WinScore_ = 32, _BEST_FILE_ = "bestScore.dat"):
		self.matrix = [[0 for n in range(4)] for m in range(4)]
		self.score = 0
		self._BEST_FILE_ = _BEST_FILE_
		self.best = self.readFile()		
		self._WinScore_ = _WinScore_
		initNumFlag = 0
		while True:
			s = divmod(random.randrange(0, 16), 4)
			if self.matrix[s[0]][s[1]] == 0:
				self.matrix[s[0]][s[1]] = 2
				initNumFlag += 1
			if initNumFlag == 2:
				break

	# 0值判断
	def notzero(self, s):
		return s if s != 0 else ''

	# 显示结果
	def display(self):
		print(r"----------------------------2048----------------------------")
		print(r"操作说明： 上（W） 下（S） 左（A） 右（D） 退出（Q）")
		print(r"当前积分：%d，最高积分：%d" % (self.score, self.best))
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
			%(self.notzero(self.matrix[0][0]), self.notzero(self.matrix[0][1]), self.notzero(self.matrix[0][2]), self.notzero(self.matrix[0][3]),
			  self.notzero(self.matrix[1][0]), self.notzero(self.matrix[1][1]), self.notzero(self.matrix[1][2]), self.notzero(self.matrix[1][3]),
			  self.notzero(self.matrix[2][0]), self.notzero(self.matrix[2][1]), self.notzero(self.matrix[2][2]), self.notzero(self.matrix[2][3]),
			  self.notzero(self.matrix[3][0]), self.notzero(self.matrix[3][1]), self.notzero(self.matrix[3][2]), self.notzero(self.matrix[3][3]))
			  )

	# 往左移动
	def moveLeft(self):
		for i in range(4):
			for j in range(3):
				for k in range(j+1, 4):
					if self.matrix[i][j] == 0 and self.matrix[i][k] > 0:
						self.matrix[i][j] = self.matrix[i][k]
						self.matrix[i][k] = 0
					elif self.matrix[i][j] > 0 and self.matrix[i][j] == self.matrix[i][k]:
						self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][k]					
						self.matrix[i][k] = 0
						self.score += self.matrix[i][j]
						break;
					elif self.matrix[i][j] > 0 and self.matrix[i][k] > 0 \
						and self.matrix[i][j] != self.matrix[i][k]:
						self.matrix[i][j+1] = self.matrix[i][k]
						if k != j + 1:
							self.matrix[i][k] = 0
						break;

	# 往右移动
	def moveRight(self):
		for i in range(4):
			for j in range(3, -1, -1):
				for k in range(j-1, -1, -1):
					if self.matrix[i][j] == 0 and self.matrix[i][k] > 0:
						self.matrix[i][j] = self.matrix[i][k]
						self.matrix[i][k] = 0
					elif self.matrix[i][j] > 0 and self.matrix[i][j] == self.matrix[i][k]:
						self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][k]
						self.matrix[i][k] = 0
						self.score += self.matrix[i][j]
						break;
					elif self.matrix[i][j] > 0 and self.matrix[i][k] > 0 \
						and self.matrix[i][j] != self.matrix[i][k]:
						self.matrix[i][j-1] = self.matrix[i][k]
						if k != j - 1:
							self.matrix[i][k] = 0
						break;				

	# 往上移动
	def moveUp(self):
		for j in range(4):
			for i in range(3):
				for k in range(i+1, 4):
					if self.matrix[i][j] == 0 and self.matrix[k][j] > 0:
						self.matrix[i][j] = self.matrix[k][j]
						self.matrix[k][j] = 0
					elif self.matrix[i][j] > 0 and self.matrix[i][j] == self.matrix[k][j]:
						self.matrix[i][j] = self.matrix[i][j] + self.matrix[k][j]
						self.matrix[k][j] = 0
						self.score += self.matrix[i][j]
						break;
					elif self.matrix[i][j] > 0 and self.matrix[k][j] > 0 \
						and self.matrix[i][j] != self.matrix[k][j]:
						self.matrix[i+1][j] = self.matrix[k][j]
						if k != i + 1:
							self.matrix[k][j] = 0
						break;

	# 往下移动
	def moveDown(self):
		for j in range(4):
			for i in range(3, -1, -1):
				for k in range(i-1, -1, -1):
					if self.matrix[i][j] == 0 and self.matrix[k][j] > 0:
						self.matrix[i][j] = self.matrix[k][j]
						self.matrix[k][j] = 0
					elif self.matrix[i][j] > 0 and self.matrix[i][j] == self.matrix[k][j]:
						self.matrix[i][j] = self.matrix[i][j] + self.matrix[k][j]
						self.matrix[k][j] = 0
						self.score += self.matrix[i][j]
						break;
					elif self.matrix[i][j] > 0 and self.matrix[k][j] > 0 \
						and self.matrix[i][j] != self.matrix[k][j]:
						self.matrix[i-1][j] = self.matrix[k][j]
						if k != i - 1:
							self.matrix[k][j] = 0
						break;	

	# 判断是否还有空位
	def isHaveSpace(self):
		for i in range(4):
			for j in range(4):
				if self.matrix[i][j] == 0:
					return True
		return False

	# 随机生成新的数字2
	def addRandomNum(self):    
	    while self.isHaveSpace() == True:
	        s = divmod(random.randrange(0, 16), 4)
	        if self.matrix[s[0]][s[1]] == 0:
	            self.matrix[s[0]][s[1]] = 2
	            return


	# 判断游戏状态，是否失败
	def isfailed(self):
		for i in range(4):
			for j in range(4):
				if self.matrix[i][j] == 0 or \
				i > 0 and self.matrix[i][j] == self.matrix[i-1][j] or \
				i < 3 and self.matrix[i][j] == self.matrix[i+1][j] or \
				j > 0 and self.matrix[i][j] == self.matrix[i][j-1] or \
				j < 3 and self.matrix[i][j] == self.matrix[i][j+1] :
					return False
		print("--------------------------游戏失败--------------------------")
		return True

	# 判断游戏状态，是否获胜
	def isWin(self):	
		for i in range(4):
			for j in range(4):
				if self.matrix[i][j] >= self._WinScore_:
					print("--------------------------游戏胜利--------------------------")
					return True
		return False

	# 读取文件
	def readFile(self):
		bestScore = 0
		if os.path.exists(self._BEST_FILE_):
			with open(self._BEST_FILE_, 'r') as f:
				bestScore = int(f.read())
		return bestScore

	# 写入文件
	def writeFile(self):
		with open(self._BEST_FILE_, 'w') as f:
			f.write(str(self.best))

	# 更新最高分
	def updateBest(self):
		if self.score > self.best:
			self.best = self.score

	# 主程序
	def start(self):    
		self.display()
		while True:
			d = input()
			if d == 'q' or d == 'Q':
				self.writeFile()
				print("退出游戏，本次积分为：%d" % (self.score))
				break
			elif d == 'w' or d == 'W':    		
				self.moveUp()    		
			elif d == 's' or d == 'S':    		
				self.moveDown()    		
			elif d == 'a' or d == 'A':
				self.moveLeft()   	    		
			elif d == 'd' or d == 'D':    		
				self.moveRight()    		
			else:
				continue
			self.updateBest()
			self.addRandomNum()
			self.display()

			if self.isfailed() == True or self.isWin() ==True:
				self.writeFile()
				print("游戏结束，本次积分为：%d" % (self.score))
				break;
	    	
if __name__ == "__main__":
	game = Game(2048)
	game.start()