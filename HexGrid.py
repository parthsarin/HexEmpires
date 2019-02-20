from graphics import *
from HexCell import *
import math
import copy

class HexGrid:
	def inBounds(self, x, y):
		return 0 <= x and x < self.width and 0 <= y and y < self.height

	def createNeighbors(self, cell, points):
		tmp = []
		for p in points:
			x = int(p.getX())
			y = int(p.getY())
			if self.inBounds(x, y):
				tmp.append(self.grid[x][y])
		cell.setNeighbors(tmp)


	def __init__(self, graphwin, p_height, p_width, height, width):
		buffer = 30
		self.height = height
		self.width = width
		t_hex_height = p_height / height
		t_hex_width = p_width / width
		max_r = max(t_hex_width / (1 + math.sin(math.pi / 6)), t_hex_height / 2 * math.sin(math.pi / 3))
		self.hex_height = 2 * max_r * math.sin(math.pi / 3)
		self.hex_width = max_r * (1 + math.sin(math.pi / 6))
		self.r = max_r
		self.grid = []
		self.graphwin = graphwin
		for y in range(0, height):
			new_row = []
			for x in range(0, width):
				hex_y = (y + 1/(2 * math.sin(math.pi / 3))) * self.hex_height;
				if x % 2 == 1:
					hex_y += self.hex_height / 2
				hex_x = (x + 1/(1 + math.sin(math.pi / 6))) * self.hex_width
				tmp = HexCell(Point(hex_x, hex_y), self.r)
				new_row.append(tmp)
			self.grid.append(new_row)

		for j in range(0, height):
			for i in range(0, width):
				if j % 2 == 0:
					adj = [Point(i-1, j-1), Point(i-1, j), Point(i-1, j+1), Point(i, j-1), Point(i, j+1), Point(i+1, j)]
				else:
					adj = [Point(i+1, j-1), Point(i+1, j), Point(i+1, j+1), Point(i, j-1), Point(i, j+1), Point(i-1, j)]
				self.createNeighbors(self.grid[i][j], adj)


	def draw(self):
		for row in self.grid:
			for cell in row:
				cell.draw(self.graphwin)



	def color(self, x, y, color):
		self.grid[x][y].setColor(color)

	def setState(self, x, y, state):
		self.grid[x][y].setState(state)

	def setStates(self, states):
		for i in range(0, self.width):
			for j in range(0, self.height):
				self.grid[i][j].setState(states[i][j])

	def runFunction(self, function):
		for row in self.grid:
			for cell in row:
				function(cell)

	def runStateFunction(self, function):
		state_grid = []
		for row in self.grid:
			new_row = []
			for cell in row:
				new_row.append(function(cell))
			state_grid.append(new_row)
		self.setStates(state_grid)



