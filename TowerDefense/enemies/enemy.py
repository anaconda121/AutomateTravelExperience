import pygame
import math

class Enemy:
	imgs = []

	def __init__(self, x, y, height, width):
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.width = width
		self.height = height
		self.animation_count = 0
		self.health = 1
		self.path = [(965, 462) ,(912, 457),(855, 445),(805, 432),(751, 417),(710, 414),(657, 419),(622, 432),(582, 442),(542, 450),(499, 444),(477, 429),(440, 422),(407, 425),(378, 436),(335, 427)
					,(267, 441),(226, 456),(178, 470),(153, 479),(98, 477),(67, 468),(37, 454),(22, 446),(12, 461),(11, 481),(9, 502),(11, 519),(16, 534),(25, 542),(36, 543),(85, 545),(166, 545),(285, 544)
					,(213, 544),(238, 544),(354, 543),(458, 547),(412, 543),(503, 544),(539, 544),(593, 544),(568, 542),(632, 544),(658, 544),(687, 544),(727, 542),(756, 543),(785, 545),(813, 545),(838, 545)
					,(884, 545),(927, 547),(980, 547)]
		self.img = None
		self.vel = 3
		self.path_pos = 0
		self.move_count = 0
		self.dis = 0

	def draw(self, win):
		"""
		draws enemy
		param: window
		return: none
		"""
		self.animation_count += 1
		self.img = self.imgs[self.animation_count]  #loads in enemy imgs

		if self.animation_count >= len(self.imgs):
			#error handler in case enemies have all been drawn
			self.animation_count = 0

		win.blit(self.img, (self.x, self.y)) #draws img onto screen


	def collide(self, X, Y):
		"""
		returns if bullet has hit enemy
		param : x-coor, y-coor
		returns bool if hit
		"""
		if X <= self.x + self.width and X >= self.x:
			if Y <= self.y + self.height and Y >= self.y:
				return True
		return False

	def move(self):
		"""
		move enemy, return none
		"""
		x1, y1 = self.path[self.path_pos]

		if self.path_pos + 1>= len(self.path):
			#if path goes off left screen
			x2, y2 = (-10, 547)
		else:
			x2, y2 = self.path[self.path_pos+1]

		move_dis = math.sqrt((x2 - x1)**2 + (y2- y1)**2) 

		self.dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #distance formula
		self.move_count += 1
		dirn = (x2 - x1 , y2 - y1)

		move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count) 
		self.dis += math.sqrt((move_x - x1)**2 + (move_y - y1)**2) #distance formula

		if self.dis >= move_dis:
			#go to next point
			self.dis = 0
			self.move_count = 0
			self.path_pos += 1 #increment through pos list

		self.x = move_x
		self.y = move_y


	def hit(self):
		""" 
		decide if enemy should be dead, returns bool, removes health
		"""
		self.heath -= 1
		if self.health <= 0:
			return True


