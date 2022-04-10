# Begin by copying your code from Turtle Patterns I and pasting it here.
# Alternatively, you may download your code from Turtle Patterns I and
# upload it here.
'''
Project Name: Turtle Project
Author: Robbie Platt
Due Date: 2021-11-13
Course: CS1400-zzz



I learned how to use Parameterized functions, for loops, scaling of shapes, 
color implementation, and shape rotation. Using import turtle I will draw a sword and a shield. 
When using this program it will be important to input positive
integers(essentially means numbers) for distance values(height, width etc.). I also learned how to scale shapes.
I learned how to use the sys.argv to prompt the user for input to interact with the program.
'''


"""
Program usage: Python main.py time
"""
import sys
from turtle import *

    #draw_scene(t,0,0,1,time)##################################
#def draw_scene()##################################################

def main():
    #Need code here to function
    t = Turtle()
    s = Screen()
    s.update()
    condition = (sys.argv[1]).lower()
    if condition != "peace" and condition != "scuffle" and condition != "ganon":
        print("Error. Usage is Python <Program name> <condition> where condition = 'peace', 'scuffle' or 'ganon'")
        return
    # Error gives the user information on how to use the program.



    draw_scene(t, 100, 100, 1, condition)

   
 
def draw_scene(t, x, y, scale, condition):
    """
    Calls the turtle to draw the scene based on the users condition decision.
    """
    t = Turtle()
    if condition == 'peace':
        draw_peace_time(t, 100, 100, 1)
    elif condition == 'scuffle':
        draw_scuffle(t, 100, 100, 1)
    elif condition == 'ganon':
        draw_ganon_battle(t, 100, 100, 1)

   
def draw_peace_time(t, x, y, scale): 
    """
    Draws the user choice 'peace' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    """
    draw_sword(t, 0, -120, 30, 100, 30, 90, 1)
    draw_shield(t, 200, -50, 100, 0)
    draw_reflection1(t, -100, 0, 0.25)
    draw_shield2(t, -200, -50, 100, 0)
    
    
def draw_scuffle(t, x, y, scale):
    """
    Draws the user choice 'scuffle' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    """
    draw_sword(t, 0, -120, 30, 100, 30, 90, 1)
    draw_shield(t, 200, -50, 100, 0)
    draw_reflection2(t, -100, 0, 0.25)
    draw_shield2(t, -200, -50, 100, 0)

def draw_reflection1(t, x_offset, y_offset, scale):
    """
    Draws 5 swords and a shield on the opposite wall
    """
    draw_sword(t, x_offset + ( -100 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 
    draw_sword(t, x_offset + ( -200 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 
    draw_shield(t, -200, -50, 100, 0, 0.25)    
    draw_sword(t, x_offset + ( -300 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25)
    draw_sword(t, x_offset + ( -400 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 
    draw_sword(t, x_offset + ( -500 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 

def draw_reflection2(t, x_offset, y_offset, scale):
    """
    Draws 3 swords and a shield on the opposite wall
    """
    draw_sword(t, x_offset + ( -100 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 
    draw_shield(t, -200, -50, 100, 0, 0.25)     
    draw_sword(t, x_offset + ( -300 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25)
    draw_sword(t, x_offset + ( -500 * scale),  y_offset + ( -120 * scale), 30 * scale, 100 * scale, 30 * scale, 90, 0.25) 

def draw_reflection3(t, x_offset, y_offset, scale):
    """
    Draws a stand alone shield on the opposite wall
    """
    draw_shield(t, x_offset + 200 * scale, y_offset -50 * scale, 100 * scale, 0, 0.25)



def draw_ganon_battle(t, x_offset, y_offset, scale):
    """
    Draws the user choice 'ganon' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    """
    s = Screen()
    s.bgcolor("sky blue")
    t = Turtle()
    s.tracer(0,0)
    t.st()
    t.ht()
    t.speed(11)


    radius = 100
    side = 30
    s.setup(40, 90, -250, -250)
    s.setup(900, 600, 0, 0)
    draw_sword(t, 0, -120, 30, 100, 30, 90, 1)
    draw_shield(t, 200, -50, 100, 0, 1)
    draw_reflection2(t, -100, 0, 0.25)
    draw_shield2(t, -200, -50, 100, 0, 1)

    
def draw_sword(t, x, y, height, width, side, tilt, scale):
    """
    Draws a sword using the atomic shapes of rectangle, diamond, trapezoid 1 and 2, and circle.
    """
    t.setheading(tilt)
    height = 100 * scale
    width = 30 * scale
    side = 30 * scale


    draw_diamond(t, x, (y + 280) * scale, side * scale, 0, 'silver', 'black')
    draw_trapezoid(t, x,(y + 280) * scale, side * scale, 0, 'silver', 'black')
    draw_trapezoid2(t, x, y, side * scale, 0, "silver", 'black')
    draw_rectangle(t, (x + 35) * scale, (y + 24) * scale, width, height, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x + 65) * scale, (y + 24) * scale, (width -70) * scale, (height + 50) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, (x - 65) * scale, (y + 24) * scale, (width -70) * scale, (height + 50) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, x, (y + 14) * scale, (width -70) * scale, (height - 20) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, x, (y + 4) * scale, (width -70) * scale, (height - 20) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, x, (y - 6) * scale, (width -70) * scale, (height - 20) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, x, (y - 16) * scale, (width -70) * scale, (height - 20) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(t, x, (y - 26) * scale, (width -70) * scale, (height - 20) * scale, 90, '#7B3F00', 'black')
    draw_circle(t, (x - 15) * scale, y - 66 * scale, 20 * scale, 0, 'silver', 'black')



"""
This takes multiple atomic shapes to form a sword. It will tilt the diamond
to be vertical. Use 2 trapezoids specified to be sides of the blade. Multiple
rectangles (some tilted) and a circle are used to make up the hilt. Fill colors are used for
the look.
"""






def draw_trapezoid(t, x, y, side, tilt, fillcolor, pencolor):
    """
    Draws a side trapezoid (only used on the blade of the sword in coordination with trapezoid2)
    """
    x = 0
    y = 160
    length1 = 200
    length2 = 16.2
    length3 = 226

    t.up()
    t.goto(x, y)
    t.setheading(240)
    t.down()

    t.begin_fill()
    t.forward(side)
    t.left(30)
    t.forward(length1)
    t.left(90)
    t.forward(length2)
    t.left(90)
    t.forward(length3)
    t.end_fill()
    t.up()

"""
Right side of the blade. 4 varying lenght lines and 4 varying length angles are
used to shape the right side of the blade. Silver fill color is used.
"""
  
#t, 0, -120, 30,  100,    30, 90)
#t, x, y, height, width, side, tilt
def draw_trapezoid2(t, x, y, side, tilt, fillcolor, pencolor):
    """
    Draws a side trapezoid (only used on the blade of the sword in coordination with draw_trapezoid)
    """
    x = -30
    y = 160
    length1 = 200
    length2 = 16.2
    length3 = 226
    

    t.up()
    t.goto(x, y)
    t.setheading(300)
    t.down()
    t.color('black', 'silver')
    t.begin_fill()
    t.forward(side)
    t.right(30)
    t.forward(length1)
    t.right(90)
    t.forward(length2)
    t.right(90)
    t.forward(length3)
    t.end_fill()
    t.up()
"""
Right side of the blade. 4 varying lenght lines and 4 varying length angles are
used to shape the right side of the blade. Silver fill color is used.
"""

#t, 0, -120, 30, 100, 30, 90)
#t, x, y, height, width, side, tilt
def draw_shield(t, x, y, radius, tilt, scale):
    """
    Uses the atomic shapes of circle, and triangle (via the function draw_triforce) to create a shield.
    """
    t.speed(11)



    draw_circle(t, x, y - 10, radius, 0, 'silver', 'black')
    draw_circle(t, x, y, 90, 0, 'silver', 'black')
    draw_circle(t, x, y - 8, 3, 0, 'silver', 'black')
    draw_circle(t, x + 30, y - 2, 3, 0, 'silver', 'black')
    draw_circle(t, x + 60, y + 14, 3, 0, 'silver', 'black')
    draw_circle(t, x + 78, y + 34, 3, 0, 'silver', 'black')
    draw_circle(t, x + 91, y + 64, 3, 0, 'silver', 'black')
    draw_circle(t, x + 94, y + 94, 3, 0, 'silver', 'black')
    draw_circle(t, x + 87, y + 124, 3, 0, 'silver', 'black')
    draw_circle(t, x + 66, y + 154, 3, 0, 'silver', 'black')
    draw_circle(t, x + 37, y + 173, 3, 0, 'silver', 'black')
    draw_circle(t, x, y + 181, 3, 0, 'silver', 'black')
    draw_circle(t, x - 30, y - 2, 3, 0, 'silver', 'black')
    draw_circle(t, x - 60, y + 14, 3, 0, 'silver', 'black')
    draw_circle(t, x - 78, y + 34, 3, 0, 'silver', 'black')
    draw_circle(t, x - 91, y + 64, 3, 0, 'silver', 'black')
    draw_circle(t, x - 94, y + 94, 3, 0, 'silver', 'black')
    draw_circle(t, x - 87, y + 124, 3, 0, 'silver', 'black')
    draw_circle(t, x - 66, y + 154, 3, 0, 'silver', 'black')
    draw_circle(t, x - 37, y + 173, 3, 0, 'silver', 'black')
    draw_triforce(t, x, y, side, 0)
"""
2 large circles are used to create the outer layers of the shield. Multiple tiny
circles are used for an asthetic bolt appearance around the edge of the shield
(in between the 2 larger circles.)
The triforce function is used to create 3 triangles in the center to suggest
a zelda shield. Silver fill color is used for the shields circles and yellow fill
color is used for the triangles.
"""

#t, 0, -120, 30,  100,    30, 90)
#t, x, y, height, width, side, tilt
def draw_triforce(t, x, y, side, tilt):
    """
    3 triangles are used to create a triforce (a shape from Zelda the video game)
    Each triangle has 3 equal sides and 3 equal angles and a yellow fill color.
    """
    side = 60
    draw_triangle(t, x, y + 60, side, 0, fillcolor = "yellow", pencolor = 'black')
    draw_triangle(t, x - 60, y + 60, side, 0, fillcolor = "yellow", pencolor = 'black')    
    draw_triangle(t, x - 30, y + 111.9, side, 0, fillcolor = "yellow", pencolor = 'black')

"""
3 triangles are used to create a triforce (a shape from Zelda the video game)
Each triangle has 3 equal sides and 3 equal angles and a yellow fill color.
"""

# t.circle(50, steps = 4) Draws a diamond, steps = 5 draws a pentagon
def draw_circle(t, x, y, radius, tilt, fillcolor, pencolor):
    """
    This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
    """
    t.color('black', 'silver')
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(radius)
    t.end_fill()
    t.speed(0)
    x = -250
    y = -250
    
"""
The draw_circle function is used to create the atomic shapes used in the
other functions. Silver fill color is used with a black outline to emphasize
the border.
"""
    
def draw_rectangle(t, x, y, height, width, tilt, fillcolor, pencolor):
    """
    Atomic shape used primarily for the hilt of the sword.
    """
    t.setheading(tilt)
    t.up()
    t.goto(x, y)
    t.down()
    t.color('black', '#7B3F00')
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.right(90)
    t.end_fill()
    t.up()

"""
The draw_rectangle function is used to draw the rectangle atomic shape
used to form various parts of the hilt in the sword function. The color chosen
was to appear as leather. (Note: I tried to use a for loop to shrink the code and
it broke the image, leaving as is to avoid ruining the image.)
"""

def draw_diamond(t, x, y, side, tilt, fillcolor, pencolor):
    """
    Atomic shape used to create the tip of the sword.
    """
    t.color('black', 'silver')
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(120)
    for i in range(2):
        t.forward(side)
        t.left(120)
        t.forward(side)
        t.left(60)
    t.end_fill()
    t.up()
    
"""
The draw_diamond function is used for the diamond shape tip of the blade. Silver
fill color is used with a black outline to emphasize the border.
"""

def draw_triangle(t, x, y, side, tilt, fillcolor, pencolor):
    """
    Atomic shape used to create the triforce used on the shield.
    """
    t.up()
    t.goto(x, y)

    t.fillcolor('yellow')
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.up()
    
    
def draw_shield2(t, x, y, radius, tilt, scale):
    """
    this function is used to create a shield without a triforce on it so that it could reflect the opposing wall.
    """
    t.speed(11)



    draw_circle(t, x, y - 10, radius, 0, 'silver', 'black')
    draw_circle(t, x, y, 90, 0, 'silver', 'black')
    draw_circle(t, x, y - 8, 3, 0, 'silver', 'black')
    draw_circle(t, x + 30, y - 2, 3, 0, 'silver', 'black')
    draw_circle(t, x + 60, y + 14, 3, 0, 'silver', 'black')
    draw_circle(t, x + 78, y + 34, 3, 0, 'silver', 'black')
    draw_circle(t, x + 91, y + 64, 3, 0, 'silver', 'black')
    draw_circle(t, x + 94, y + 94, 3, 0, 'silver', 'black')
    draw_circle(t, x + 87, y + 124, 3, 0, 'silver', 'black')
    draw_circle(t, x + 66, y + 154, 3, 0, 'silver', 'black')
    draw_circle(t, x + 37, y + 173, 3, 0, 'silver', 'black')
    draw_circle(t, x, y + 181, 3, 0, 'silver', 'black')
    draw_circle(t, x - 30, y - 2, 3, 0, 'silver', 'black')
    draw_circle(t, x - 60, y + 14, 3, 0, 'silver', 'black')
    draw_circle(t, x - 78, y + 34, 3, 0, 'silver', 'black')
    draw_circle(t, x - 91, y + 64, 3, 0, 'silver', 'black')
    draw_circle(t, x - 94, y + 94, 3, 0, 'silver', 'black')
    draw_circle(t, x - 87, y + 124, 3, 0, 'silver', 'black')
    draw_circle(t, x - 66, y + 154, 3, 0, 'silver', 'black')
    draw_circle(t, x - 37, y + 173, 3, 0, 'silver', 'black')

"""
The draw_triangle function is used to create the triforce for the shield decor.
Yellow fill is used as well as a black outline to emphasize the borders.
"""

  
    
    
    
    
    
    
    
    
    #s.exitonclick()##############################################################################
    
    
if __name__== "__main__":
    main()
