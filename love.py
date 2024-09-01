import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5*\
    math.cos(2 * k) - 2 *\
     math.cos(3 * k)
    math.cos(4 * k)

speed(9000)  # 0 is the fastest speed
bgcolor("black")
color("red")
penup()
goto(hearta(0) * 20, heartb(0) * 20)
pendown()

for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)   
    

done()
