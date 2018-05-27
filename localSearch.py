class myAccount:
	event   = ""
	room    = ""
	block   = ""
	day     = ""
	slot    = (0,0)

	def __init__(self, e, r, b, d, s):
		self.event = e
		self.room = r
		self.block = b
		self.day = d
		self.slot = s
 
	def setEvent (self, e):
		self.event = e

	def setRoom (self, r):
		self.room = r
 
	def setBlock (self, b):
		self.block = b

	def setDay (self, d):
		self.day = d

	def setSlot (self, s):
		self.slot = s

class LocalSearch(object):
	def __init__(self, s0):
		super(LocalSearch, self).__init__()
		self.s0 = s0

	def build(self):
		print self.s0
		s = self.s0
		while True:
			s1 = s
			s = self.improve(s1)
			if s == None:
				break
		self.show(s)

	def improve(self, s):
		print s
		return None

	def show(self, s):
		print s


if __name__ == '__main__':
	swap = 2
	LocalSearch(swap).build()
