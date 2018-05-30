import random
import copy as cp

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

	def __repr__(self):
		return "{event : %s, area : %s, block : %s,  slot : %s-%s} \n" % (self.getEvent(), self.getArea(), self.getBlock(), self.getSlot()[0], self.getSlot()[1])

	def __str__(self):
		return "{event : %s, area : %s, block : %s }" % (self.getEvent(), self.getArea(), self.getBlock())

	def getEvent(self):
		return self.event

	def getRoom(self):
		return self.room

	def getSlot(self):
		return self.slot

	def getArea(self):
		return self.area

	def getBlock (self):
		return self.block
 
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

		s2 = self.s0
		while True:
			s1 = s2
			n = self.getNeighbors(s1)
			s2 = self.improve(s1, n)
			if s2 == None:
				break
		self.show(s1)

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
		#TODO validate room is bad and insert is bad 

		for i in range(0, len(s) - 1):
			tsi = s[i].getSlot()[1] - s[i+1].getSlot()[0]
			if tsi != 0 and ts <= tsi:
				#TODO is bad
				temp = s[ts]
				s.remove(temp)
				s.insert(i, temp)
				print "entro"
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

		totalE = {}
		sc = cp.copy(s)

		while sc:
			totalE[sc[0].getArea()] = len(filter(lambda i: i.getArea() == sc[0].getArea(), sc))
			sc = [i for i in sc if i.getArea() != sc[0].getArea()]

		return totalE

	def getMaximunEventsPerAreaEachBlock(self, s):

		totalE = {}
		sc = cp.copy(s)

		while sc:
			eventForArea = filter(lambda i: i.getArea() == sc[0].getArea(), sc)
			# te: total event for area and block
			te = []
			while eventForArea:
				te.append(len(filter(lambda i: i.getBlock() == eventForArea[0].getBlock(), eventForArea)))
				# remove items counted
				eventForArea = [i for i in eventForArea if i.getBlock() != eventForArea[0].getBlock()]
			# set the maximun number events for area block 
			totalE[sc[0].getArea()] = max(te)
			# remove items counted
			sc = [i for i in sc if i.getArea() != sc[0].getArea()]
		
		return totalE

	def getTotalBlocksAssignedToEventSameArea(self, s):
		totalE = {}
		sc = cp.copy(s)

		while sc:
			ev = filter(lambda i: i.getArea() == sc[0].getArea(), sc)
			# get the total number of block for area in each ev
			totalE[sc[0].getArea()] = len({x.getBlock():ev.count(x) for x in ev})
			sc = [i for i in sc if i.getArea() != sc[0].getArea()]
		return totalE

	def show(self, s):
		print s


if __name__ == '__main__':
	t1 = TimeTabling("mate2", "s1", "b3", "L", "CB", (6, 8))

	t2 = TimeTabling("progr", "s1", "b1", "L", "ING", (8, 10))
	t3 = TimeTabling("mate1", "s1", "b1", "L", "CB", (10, 12))
	
	t4 = TimeTabling("mate1", "s1", "b2", "L", "CB", (14, 16))
	t5 = TimeTabling("mate1", "s2", "b2", "L", "CB", (13, 14))
	t6 = TimeTabling("mate1", "s2", "b2", "L", "CB", (8, 9))
	t7 = TimeTabling("mate1", "s2", "b2", "L", "CB", (6, 8))
	swap = [t1, t2, t3, t4, t5, t6, t7]
	nmax = 1
	LocalSearch(swap, nmax).build()
