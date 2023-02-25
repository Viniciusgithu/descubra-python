class myClass():
  def __init__(self):
    self.myAttribute = 'Run constructor!'

  def myMethod(self):
    print('Run Method!')  


def newObject():
  myObj = myClass()
  var = myObj.myAttribute
  print(var)

  myObj.myMethod()

newObject()      




