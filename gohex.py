from graphics import *
import time
from HexCell import *
from HexGrid import *
import random
import statistics as stats

GRID_SIDE_LENGTH = 35
NUM_EMPIRES = 6

def getNeighborStates(cell):
	poss_states = []
	for neighbor in cell.getNeighbors():
		poss_states.append(neighbor.getState())
	return poss_states

def makeRainbow(cell):
	cell.setState(random.randrange(NUM_EMPIRES))

def life1(cell):
	n = 0
	for neighbor in cell.getNeighbors():
		if neighbor.getState() == 1:
			n += 1
	self_on = cell.getState() == 1
	if self_on:
		if n > 4 or n == 0:
			return 0
	else:
		if 0 < n and n < 4:
			return 1
	if self_on:
		return 1
	else:
		return 0

def empireSimple(cell):
	poss_states = []
	for neighbor in cell.getNeighbors():
		poss_states.append(neighbor.getState())

	return random.choice(poss_states)

def empiresRandom(cell):
	poss_states = []
	for neighbor in cell.getNeighbors():
		poss_states.append(neighbor.getState())
	terr = max(set(poss_states), key=poss_states.count)
	if terr and poss_states.count(terr) == len(poss_states) - 1:
		return terr
	return random.choice(poss_states)

def empireDefend(cell):
	poss_states = []
	for neighbor in cell.getNeighbors():
		poss_states.append(neighbor.getState())
	counts = [poss_states.count(x) for x in range(0, NUM_EMPIRES)]
	maxN = max(counts)
	choices = []
	for i in range(0, NUM_EMPIRES):
		if counts[i] >= maxN:
			choices.append(i)
	return random.choice(choices)

TROOP_SPAWN_CHANCE = 10
def empireTroop(cell):
	if random.randrange(0, 100) == 7:
		cell.setTroops(cell.getTroops() + 1)
	if cell.getTroops() > 0:
		for n in cell.getNeighbors():
			if n.getState() != cell.getState():
				n.moveTroops(cell.getTroops(), cell.getState())
				cell.setTroops(0)
		return cell.getState()
	return cell.getState()



STRENGTH = [1000] * NUM_EMPIRES
def empireStrong(cell):
	states = getNeighborStates(cell).append(cell.getState())
	ind_str = [STRENGTH[i] * states.count(i) for i in range(0, NUM_EMPIRES)]
	r = ind_str.index(max(ind_str))
	STRENGTH[r] += 1
	STRENGTH[cell.getState()] -= 1
	return r

print("HI")
win = GraphWin("Go Hex!", 1000, 1000)
myhexgrid = HexGrid(win, 750, 750, GRID_SIDE_LENGTH, GRID_SIDE_LENGTH)
myhexgrid.draw()
myhexgrid.setState(5, 7, 1)
# myhexgrid.runFunction(makeRainbow)

while not win.checkMouse():
	myhexgrid.runStateFunction(life1)