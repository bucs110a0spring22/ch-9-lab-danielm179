class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y
    self.h = height
    self.w = width
    #while (x, y, height, width) < 0:
      #return 0

  def __str__(self):
    r1 = Rectangle(x, y, height, width)
    return "x:", r1.x
    return "y: ", r1.y
    return "height: ", r1.h
    return "width: ", r1.w

class Surface:
  def __init__(self, filename, x, y, height, width):
    self.rect = Rectangle((x,y) + (height,width))
    self.image = filename
    #self.image = str($PATH = )
    self.x = x
    self.y = y
    self.h = height
    self.w = width
  def perim(self):
    return (2 * (self.x + self.y)) + (2 * (self.h + self.w))

  def area(self):
    return (self.x + self.y) * (self.w + self.h)

  def position(self):
    return (self.x, self.y, self.w, self.h)

  def getRect(self):
    self.rect = Rectangle((x,y) + (height,width))