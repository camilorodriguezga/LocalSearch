class TimeTablingModel:
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
	return ("event:%s, area:%s, room:%s, block:%s,  slot:%s \n" % 
			(self.event, self.area, self.room, self.block, self.slot))

  def __str__(self):
	return "event:%s, area:%s, block:%s" % (self.event, self.area, self.block)
