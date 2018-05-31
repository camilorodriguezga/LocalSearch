from basefile import BaseFile
from timetablingmodel import TimeTablingModel

from copy import deepcopy
import random
import sys

class LocalSearch(object):
  def __init__(self, s0, nmax):
    super(LocalSearch, self).__init__()
    self.s0 = s0
    self.nmax = nmax

  def build(self):
    s2 = self.s0
    self.show(s2)
    while True:
      s1 = s2
      n = self.getNeighbors(s1)
      s2 = self.improve(s1, n)
      if s2 == None:
        break
      else :
        self.show(s2)

  def getNeighbors(self, s):
    n = []
    sc = deepcopy(s)
    for i in range(0, self.nmax):
      ni = self.insertAndDelete(sc)
      if ni == None:
        ni = self.swap(sc)
      n.append(ni)
    return n

  def insertAndDelete(self, s):
    r1 = random.randint(0, len(s)-1)
    sc = deepcopy(s)
    sc = [i for i in sc if i.room != sc[r1].room]
    while sc:
      er = filter(lambda i: i.room == sc[0].room, sc)
      for i in range(0, len(er) - 1):
        if s[r1].slot[0] >= er[i+1].slot[1] and s[r1].slot[1] <= er[i].slot[0]:
          s[r1].block = er[i].block
          s[r1].room = er[i].room
          return s
      sc = [i for i in sc if i.room != sc[0].room]
    return None

  def swap(self, s):    
    while True:
      r1 = random.randint(0, len(s)-1)
      r2 = random.randint(0, len(s)-1)
      while r1 == r2:
        r2 = random.randint(0, len(s)-1)
      if (s[r1].block != s[r2].block 
        and s[r1].slot[1] - s[r1].slot[0] == s[r2].slot[1] - s[r2].slot[0]):
        temp = []
        temp.insert(0, s[r2].room)
        temp.insert(1, s[r2].block)
        temp.insert(2, s[r2].slot)
        s[r2].room = s[r1].room
        s[r2].block = s[r1].block
        s[r2].slot = s[r1].slot
        s[r1].room = temp[0]
        s[r1].block = temp[1]
        s[r1].slot = temp[2]
        break
    return s

  def improve(self, s, n):
    sCost = self.getCost(s)
    for nk in n:
      nkCost = self.getCost(nk)
      if nkCost < sCost:
        return nk
    return None

  def getCost(self, s):
    sCost = 0
    eTotal = self.getTotalEventsPerArea(s)
    eMaxForBlock = self.getMaximunEventsPerAreaEachBlock(s)
    bTotal = self.getTotalBlocksAssignedToEventSameArea(s)  
    for i in eTotal:
      sCost = (bTotal[i] * eTotal[i] / eMaxForBlock[i] ) + sCost
    return sCost

  def getTotalEventsPerArea(self, s):
    totalE = {}
    sc = deepcopy(s)
    while sc:
      totalE[sc[0].area] = len(filter(lambda i: i.area == sc[0].area, sc))
      sc = [i for i in sc if i.area != sc[0].area]
    return totalE

  def getMaximunEventsPerAreaEachBlock(self, s):
    totalE = {}
    sc = deepcopy(s)
    while sc:
      eventForArea = filter(lambda i: i.area == sc[0].area, sc)
      # te: total event for area and block
      te = []
      while eventForArea:
        te.append(len(filter(lambda i: i.block == eventForArea[0].block, eventForArea)))
        # remove items counted
        eventForArea = [i for i in eventForArea if i.block != eventForArea[0].block]
      # set the maximun number events for area block 
      totalE[sc[0].area] = max(te)
      # remove items counted
      sc = [i for i in sc if i.area != sc[0].area]
    
    return totalE

  def getTotalBlocksAssignedToEventSameArea(self, s):
    totalE = {}
    sc = deepcopy(s)
    while sc:
      ev = filter(lambda i: i.area == sc[0].area, sc)
      # get the total number of block for area in each ev
      totalE[sc[0].area] = len({x.block:ev.count(x) for x in ev})
      sc = [i for i in sc if i.area != sc[0].area]
    return totalE

  def show(self, s):
    print "min z =",self.getCost(s), "\n", s

if __name__ == '__main__':
  nameFile = "data/timetabling2.csv"
  nmax = 100
  if len(sys.argv) > 1:
    nameFile = "data/" + sys.argv[1]
  if len(sys.argv) > 2:
    nmax = int(sys.argv[2])
  swap = BaseFile().getContent(nameFile)
  LocalSearch(swap, nmax).build()
