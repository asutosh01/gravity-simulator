from cmath import sqrt
from random import random

world=[['/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/','/','/'],['/','/','/','/','/','/','/','/','/','/','/','/']]
object_x=1
object_y=-1
object2_x=object_x
object2_y=1

def update():
 world = [['/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/', '/','/','/','/','/','/','/','/','/','/','/','/'],
          ['/', '/', '/', '/', '/', 'A', 'T', 'A', '/', '/', '/', '/','A','T','A','/','/','/','/','/','/','/','/'],
          ['I', 'I', 'I', 'I', 'I', '|', '|', '|', 'I', 'I', 'I', 'I','|','|','|','I','I','I','I','I','I','I','I']]
 world[object_y - 2][object_x - 1] = 'm'
 #world[object2_y - 2][object2_x - 1] = '='
 #world[object2_y - 2][object2_x - 1] = 'o'
 #print(f"~WORLD~,({object_y}),({object2_y}),({object_x}),({object2_x})")
 print("")
 print(world[0])
 print(world[1])
 print(world[2])
#Space
update()
while object_x<5:
 object_x+=1
 object2_x=object_x
 if object_y != 1:
  object_y += 1
 if object_x == object2_x:
  object_y=object2_y-1
 update()
object2_y=0
while object_x<8:
 object_x+=1
 object2_x=object_x
 if object_y != 1:
  object_y += 1
 if object_x == object2_x:
  object_y=object2_y-1
 update()
object2_y=1
while object_x<12:
 object_x+=1
 object2_x=object_x
 if object_y != 1:
  object_y += 1
 if object_x == object2_x:
  object_y=object2_y-1
 update()
object2_y=0
while object_x<15:
 object_x+=1
 object2_x=object_x
 if object_y != 1:
  object_y += 1
 if object_x == object2_x:
  object_y=object2_y-1
 update()
object2_y=1
while object_x<19:
 object_x+=1
 object2_x=object_x
 if object_y != 1:
  object_y += 1
 if object_x == object2_x:
  object_y=object2_y-1
 update()

