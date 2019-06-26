class simpleObject:
 somevar = 5
 def __init__(self, someAttribute, anotherAttribute):
  self.someAttribute = someAttribute 
  self.anotherAttribute = anotherAttribute
 
 def displaySomeVar(self):
  print "The value of someVar is %d" %self.somevar

 def displayAttributes(self):
  print "The first attribute is ", self.someAttribute, " and the second is ", self.anotherAttribute,"\n"

first = simpleObject("thing", 6)
second = simpleObject((1,2,3),[1,2,3])

first.displaySomeVar()
first.displayAttributes()

second.displaySomeVar()
second.displayAttributes()
