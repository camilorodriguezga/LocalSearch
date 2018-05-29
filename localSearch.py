import random

class TimeTabling:
	event   = ""
	room    = ""
	block   = ""
	day     = ""
	area    = ""
	slot    = (0,0)

	def __init__(self, e, r, b, d, a, s):
		self.event = e
		self.room = r
		self.block = b
		self.day = d
		self.area = a
		self.slot = s

	def getEvent(self):
		return self.event

	def getSlot(self):
		return self.slot

	def getArea(self):
		return self.area
 
	def setEvent (self, e):
		self.event = e

	def setRoom (self, r):
		self.room = r
 
	def setBlock (self, b):
		self.block = b

	def setDay (self, d):
		self.day = d

	def setArea (self, a):
		self.area = a   

	def setSlot (self, s):
		self.slot = s

class LocalSearch(object):
	def __init__(self, s0, nmax):
		super(LocalSearch, self).__init__()
		self.s0 = s0
		self.nmax = nmax

	def build(self):

		s = self.s0
		while True:
			n = self.getNeighbors(s)
			s = self.improve(s, n)
			if s == None:
				break
		self.show(s)

	def getNeighbors(self, s):
		
		n = []
		for i in range(0, self.nmax):
			ni = self.insertAndDelete(s)
			if ni == None:
				ni = self.swap(s)
			n.append(ni)

		return n

	def insertAndDelete(self, s):

		r1 = random.randint(0, len(s)-1)
		ts = s[r1].getSlot()[1] - s[r1].getSlot()[0]

		for i in range(0, len(s) - 1):
			tsi = s[i].getSlot()[1] - s[i+1].getSlot()[0]
			if tsi != 0 and ts <= tsi:
				temp = s[ts]
				s.remove(temp)
				s.insert(i, temp)
				return s

		return None

	def swap(self, s):
		
		r1 = random.randint(0, len(s)-1)
		r2 = random.randint(0, len(s)-1)

		while True:
			if s[r1].getSlot()[1] - s[r1].getSlot()[0] == s[r2].getSlot()[1] - s[r2].getSlot()[0]:
				temp = []
				temp.insert(0, s[r1].getEvent())
				temp.insert(1, s[r1].getArea())
				s[r2].setEvent(s[r1].getEvent())
				s[r2].setArea(s[r1].getArea())
				s[r1].setEvent(temp[0])
				s[r1].setEvent(temp[1])
				break

		return s, True

	def improve(self, s, n):
		eTotal = self.getTotalEventsPerArea(s)
		eMaxForBlock = self.getMaximunEventsPerAreaEachBlock(s)
		bTotal = self.getTotalBlocksAssignedToEventSameArea(s)

		sCost = self.getCost(eTotal, eMaxForBlock, bTotal)
		
		for nk in n:
			eTotal = self.getTotalEventsPerArea(nk)
			eMaxForBlock = self.getMaximunEventsPerAreaEachBlock(nk)
			bTotal = self.getTotalBlocksAssignedToEventSameArea(nk)
			nk = self.getCost(eTotal, eMaxForBlock, bTotal)
			if nk < sCost:
				return nk

		return None

	def getCost(self, eTotal, eMaxForBlock, bTotal):
		sCost = 0
		for i in eTotal:
			sCost = bTotal[i] * eTotal[i] / eMaxForBlock[i]
		return sCost

	def getTotalEventsPerArea(self, s):
		return {"CB": 2, "ING": 3}

	def getMaximunEventsPerAreaEachBlock(self, s):
		# maximun number event per area
		return {"CB": 2, "ING": 3}

	def getTotalBlocksAssignedToEventSameArea(self, s):
		# area and total number of blocks
		return {"CB":2, "ING":5}

	def show(self, s):
		print s


if __name__ == '__main__':
	t1 = TimeTabling("mate1", "s1", "b1", "L", "CB", (6, 8))
	t2 = TimeTabling("progr", "s1", "b1", "L", "ING", (8, 10))
	t3 = TimeTabling("mate1", "s1", "b1", "L", "CB", (10, 12))
	t4 = TimeTabling("mate1", "s1", "b1", "L", "CB", (14, 16))
	t5 = TimeTabling("mate1", "s2", "b2", "L", "CB", (12, 14))
	t6 = TimeTabling("mate1", "s2", "b2", "L", "CB", (12, 14))
	t7 = TimeTabling("mate1", "s2", "b2", "L", "CB", (12, 14))
	swap = [t1, t2, t3, t4, t5]
	nmax = 10
	LocalSearch(swap, nmax).build()
