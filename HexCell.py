from graphics import *
import math

class HexCell:
	def __init__(self, p, r):
		points = []
		b_points = []
		for i in range(0, 6):
			theta = i * math.pi / 3
			new_x = round(p.getX() + r * math.cos(theta))
			new_y = round(p.getY() + r * math.sin(theta))
			points.append(Point(new_x, new_y))
		self.poly = Polygon(points)
		self.state = 0
		self.colors = ["white", "blue", "red", "green", "yellow", "purple"]
		self.troops = 0
		self.text = Text(p, str(self.troops))

	def draw(self, graphwin):
		self.poly.draw(graphwin)
		# self.text.draw(graphwin)

	def getTroops(self):
		return self.troops

	def setTroops(self, newNum):
		self.troops = newNum
		self.text.setText(str(newNum))
	
	def moveTroops(self, troop, state):
		if state == self.state:
			self.troops += troop
		else:
			if troop > self.troops:
				self.troops = troop - self.troops
				self.setState(state)
			else:
				self.troops -= troop
		self.text.setText(str(self.troops))

	def setColor(self, color):
		self.poly.setFill(color)

	def getState(self):
		return self.state

	def setState(self, state):
		self.state = state
		self.poly.setFill(self.colors[state])

	def setNeighbors(self, neighbors):
		self.neighors = neighbors

	def getNeighbors(self):
		return self.neighors


