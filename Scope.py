def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
    # def myininfun():
    #   print(100)
    #   myininfun()
  myinnerfunc()
myfunc()