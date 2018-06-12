from timetablingmodel import TimeTablingModel

import sys

class BaseFile(object):
  def __init__(self):
  	super(BaseFile, self).__init__()
  """docstring for BaseFile"""
  def getContent(self, nameFile):
  	content = open(nameFile)
  	s = []
  	count = 1
  	with content as fp:
  	  for line in fp:
  	  	data = line.split(";")
  	  	s.append(TimeTablingModel(data[0], data[1], data[2], data[3], 
  	  		data[4], (int(data[5]),int(data[6]))))
  	return s

if __name__ == '__main__':
  nameFile = "data/timetabling1.csv"
  if len(sys.argv) > 1:
  	nameFile = "data/" + sys.argv[1]
  s = BaseFile().getContent(nameFile)
