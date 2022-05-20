'''
Project Name:  turtle Project
Author: Robbie Platt
Due Date: 2022-04-09
Course: CS1400



I learned how   _to use Parameterized functions, for loops,_scaling of_shapes,
color implementation, and_shape rotation. Using import   _turtle I will draw a_sword and a_shield. 
When using   _this program it will be important   _to input positive
integers(essentially means numbers)for distance values(height, width etc.). I also learned how   _to_scale_shapes.
I learned how   _to use   _the_sys.argv   _to prompt   _the user for input  _to interact with  _the program.
'''
import sys
import turtle




    #draw_scene(t,0,0,1,time)##################################
#def draw_scene()##################################################

def main(scale):
    """
    Usage: choose the scene you want to see: peace, scuffle, or ganon.

    """
    _t = turtle.Turtle()
    _s = turtle.getscreen()
    _s.update()
    try:
        condition = (sys.argv[1]).lower() # Draw peace time
        if condition == "1":
            draw_peace_time(_t) #Draw Scuffle
            print("Our supplies are well stocked")
        elif condition == "2":
            print("A mild skirmish")
            draw_scuffle(_t, 1, "red")
        elif condition == "3": #Draw Ganon
            draw_ganon_battle(_t, 100, 100, "yellow")
            print("Defeating Ganon is no easy task")
        elif condition != 1 or condition != 2 or condition != 3:
            print("Error. Usage is Python <Program name> <condition> where condition = '1' for peace, '2' for scuffle or '3' for ganon")
    except IndexError:
        for _i in sys.argv:
            print("Usage index 0: turtle_project_5.py ")
            print("Usage index 1: 1 for 'peace', 2 for 'scuffle', or 3 for 'ganon'")
    # Error gives the user information on how to use the program.



    #draw_scene(t, 100, 100, 1, condition)







def draw_peace_time(_t):
    """
    Draws the user choice 'peace' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    """
    _s = turtle.getscreen()
    _s.bgcolor("sky blue")
    draw_sword(_t, 0, -120, 100, 30, 30, 90, 0.5, "silver")
    draw_shield(_t, 200, -50, 100)
    #draw_reflection1(_t, -100, 0, 0.25)
    draw_shield(_t, -200, -50, 100)


def draw_scuffle(_t, scale, blade):
    """
    Draws the user choice 'scuffle' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    scale is used to change the size of the sword.
    blade is used to change the color of the blade.
    """
    _s = turtle.getscreen()
    _s.bgcolor("light green")
    draw_sword(_t, 0, -120, 100, 30, 30, 90, 1, blade)
    draw_shield(_t, 200 * scale, -50 * scale, 100 * scale)






def draw_ganon_battle(_t, _x, _y, blade):
    """
    Draws the user choice 'ganon' It also takes the functions defined below to draw 2 shields, one of which has the reflections of the other wall.
    _x, and _y parameters are just for location
    blade is for color of the blade.
    """
    _s = turtle.getscreen()
    _s.bgcolor("dark red")
    side = 60

    draw_sword(_t, 0, -150, 100, 30, 30, 90, 1.15, blade)
    draw_triforce(_t, (_x - 116), (_y + 20), side)


def draw_sword(_t, _x, _y, height, width, side, tilt, scale, blade):
    """
    Draws a sword using the atomic shapes of rectangle, diamond, trapezoid 1 and 2, and circle.
    _x, and _y are for coordinates
    height is used for the hilts' rectangles
    Width is like the height
    tilt is used for the rectangles that are not facing the same direction.
    scale is used to determine the size of the sword, the parameter applies to all shapes herein.
    blade is for the blades color.
    """
    _t.setheading(tilt)



    draw_diamond(_t, _x, (_y + 280) * scale, side * scale, blade, 'black')
    draw_trapezoid(_t, _x * scale,(_y + 280) * scale, side * scale, blade, 'black', scale)
    draw_trapezoid2(_t, (_x-30) * scale, (_y + 280) * scale, side * scale, blade, 'black', scale)
    draw_rectangle(_t, (_x - 65) * scale, (_y + 24) * scale, width * scale, height * scale, 0, '#7B3F00', 'black')
    draw_rectangle(_t, (_x + 35) * scale, (_y + 24) * scale, (width -70) * scale, (height - 25) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 105) * scale, (_y + 24) * scale, (width -70) * scale, (height - 25) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 30) * scale, (_y + 14) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 30) * scale, (_y + 4) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 30) * scale, (_y - 6) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 30) * scale, (_y - 16) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_rectangle(_t, (_x - 30) * scale, (_y - 26) * scale, (width -60) * scale, (height - 90) * scale, 90, '#7B3F00', 'black')
    draw_circle(_t, (_x - 15) * scale, (_y - 66) * scale, 20 * scale, blade, 'black')










def draw_trapezoid(_t, _x, _y, side, fillcolor, pencolor, scale):
    """
    Draws a side trapezoid (only used on the blade of the sword in coordination with trapezoid2)
    _x, and _y are for coordinates.
    side is for one of the sides.
    fillcolor is for the color inside of the shape
    pencolor is for the border of the shape
    scale is to allow for size adjustments
    """

    length1 = 200
    length2 = 16.2
    length3 = 226

    _t.up()
    _t.goto(_x, _y)
    _t.setheading(240)
    _t.down()
    _t.color(pencolor, fillcolor)

    _t.begin_fill()
    _t.forward(side)
    _t.left(30)
    _t.forward(length1 * scale)
    _t.left(90)
    _t.forward(length2 * scale)
    _t.left(90)
    _t.forward(length3 * scale)
    _t.end_fill()
    _t.up()



#t, 0, -120, 30,  100,    30, 90)
#t, _x, _y, height, width, side, tilt
def draw_trapezoid2(_t, _x, _y, side, fillcolor, pencolor, scale):
    """
    # Draws a side trapezoid (only used on the blade of the sword in coordination with draw_trapezoid)
    _x, and _y are for coordinates
    side is for one of the sides length. (Not the same as the other sides.)
    fillcolor is for the color inside of the shape
    pencolor is for the border of the shape
    scale is to allow for size adjustments
    """

    length1 = 200
    length2 = 16.2
    length3 = 226


    _t.up()
    _t.goto(_x, _y)
    _t.setheading(300)
    _t.down()
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.forward(side)
    _t.right(30)
    _t.forward(length1 * scale)
    _t.right(90)
    _t.forward(length2 * scale)
    _t.right(90)
    _t.forward(length3 * scale)
    _t.end_fill()
    _t.up()


#t, 0, -120, 30, 100, 30, 90)
#t, _x, _y, height, width, side, tilt
def draw_shield(_t, _x, _y, radius):
    """
    # Uses the atomic shapes of circle, and triangle (via the function draw_triforce) to create a shield.
    _x, and _y are for coordinates
    radius is used for the circle size
    """
    _t.speed(11)


    side = 60
    draw_circle(_t, _x, _y - 10, radius, 'silver', 'black')
    draw_circle(_t, _x, _y, 90, 'silver', 'black')
    draw_circle(_t, _x, _y - 8, 3, 'silver', 'black')
    draw_circle(_t, _x + 30, _y - 2, 3, 'silver', 'black')
    draw_circle(_t, _x + 60, _y + 14, 3, 'silver', 'black')
    draw_circle(_t, _x + 78, _y + 34, 3, 'silver', 'black')
    draw_circle(_t, _x + 91, _y + 64, 3, 'silver', 'black')
    draw_circle(_t, _x + 94, _y + 94, 3, 'silver', 'black')
    draw_circle(_t, _x + 87, _y + 124, 3, 'silver', 'black')
    draw_circle(_t, _x + 66, _y + 154, 3, 'silver', 'black')
    draw_circle(_t, _x + 37, _y + 173, 3, 'silver', 'black')
    draw_circle(_t, _x, _y + 181, 3, 'silver', 'black')
    draw_circle(_t, _x - 30, _y - 2, 3, 'silver', 'black')
    draw_circle(_t, _x - 60, _y + 14, 3, 'silver', 'black')
    draw_circle(_t, _x - 78, _y + 34, 3, 'silver', 'black')
    draw_circle(_t, _x - 91, _y + 64, 3, 'silver', 'black')
    draw_circle(_t, _x - 94, _y + 94, 3, 'silver', 'black')
    draw_circle(_t, _x - 87, _y + 124, 3, 'silver', 'black')
    draw_circle(_t, _x - 66, _y + 154, 3, 'silver', 'black')
    draw_circle(_t, _x - 37, _y + 173, 3, 'silver', 'black')
    draw_triforce(_t, _x, _y, side)


#t, 0, -120, 30,  100,    30, 90)
#t, _x, _y, height, width, side, tilt
def draw_triforce(_t, _x, _y, side):
    """
    _x, and _y are for coordinates
    side is used for the size of the triangles. (Each side is the same length)
    """
    side = 60
    draw_triangle(_t, _x, _y + 60, side, fillcolor = "yellow", pencolor = 'black')
    draw_triangle(_t, _x - 60, _y + 60, side, fillcolor = "yellow", pencolor = 'black')
    draw_triangle(_t, _x - 30, _y + 111.9, side, fillcolor = "yellow", pencolor = 'black')



# t.circle(50, steps = 4) Draws a diamond, steps = 5 draws a pentagon
def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
    """
    This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
    _x, and _y are for coordinates
    radius is used for the circle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.up()
    _t.goto(_x,_y)
    _t.down()
    _t.circle(radius)
    _t.end_fill()
    _t.speed(0)




def draw_rectangle(_t, _x, _y, height, width, tilt, fillcolor, pencolor):
    """
    Atomic shape used primarily for the hilt of the sword.
    _x, and _y are for coordinates
    height and width are used for the rectangle size
    tilt is for the direction that the rectangle is tilted or not.
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.setheading(tilt)
    _t.up()
    _t.goto(_x, _y)
    _t.down()
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    for _i in range(2):
        _t.forward(width)
        _t.left(90)
        _t.forward(height)
        _t.left(90)

    _t.right(90)
    _t.end_fill()
    _t.up()



def draw_diamond(_t, _x, _y, side, fillcolor, pencolor):
    """
    Atomic shape used to create the tip of the sword.
    _x, and _y are for coordinates
    side is used for the diamond size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.up()
    _t.goto(_x, _y)
    _t.down()
    _t.setheading(120)
    for _i in range(2):
        _t.forward(side)
        _t.left(120)
        _t.forward(side)
        _t.left(60)
    _t.end_fill()
    _t.up()



def draw_triangle(_t, _x, _y, side, fillcolor, pencolor):
    """
    Atomic shape used to create the triforce used on the shield.
    _x, and _y are for coordinates
    side is used for the triangle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.up()
    _t.goto(_x, _y)

    _t.fillcolor(fillcolor)
    _t.down()
    _t.begin_fill()
    for _i in range(3):
        _t.forward(side)
        _t.left(120)
    _t.end_fill()
    _t.up()







if __name__== "__main__":
    if len(sys.argv) == 1:
        scale = 1.0
        print("Error, why is there only one? It might be lonely")
    else:
        scale = float(sys.argv[1])
    main(scale)

