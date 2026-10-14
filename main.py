#ACTIVITY-NEON MANDELA
#PART-1 IMPORT AND SCREEN SETUP
#turtle.Screen()creates the canvas we draw on
#bgcolor("Black") sets the background - - Neon colors pop on black!
#title() sets the text that appears on the windows title bar.
import turtle
screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Neon Mandela")
#PART-2 CREATE THE TURTLE PEN
#turtle.Tutle() creates our drawing pen.
#speed("fastest") skips the slow animation so it draws instantly
#hideturtle() hides the arrow shape - - only the art is visible
board = turtle.Turtle
board.speed("fastest")
board.hideturtle()
#PART-3 OUTER COLOR SPIRAL (MOVMENT+LOOPS+COLOR)
#forward(n) moves the turtle color forward n pixels.
##right(91) turns is 91 degrees - - 1 degree extra creates the spiral drift!
#the for loop repeats 80 times, growing the distance each round 
#colors[1 % len(colors)] cycles trough the color list endlessly
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colors[1 % len(colors)])
    board.width(2)
    board.forward(1 * 2)
    board.right(91)
    #PART-4 PEN CONTROL: MOVE TO THE CENTER AND DRAW A FILLED STAR
    #penup() lifts the pen so moving it dosent draw a line
    #goto(0, 0) teleports th eturtle to the exact center of the canvas
    #pendown() puts the pen back on the canvas - - drawing starts again
    #begin_fill() + end_fill fills the shape with the chosen color
    # A 5 pointed star turns 144 degrees at each point. 
    board.penup()
    board.goto(0, -60)
    board.setheading(90)
    board.pendown()
    board.color("gold", "yellow")
    board.begin_fill()
    for i in range:(5)
    board.forward(130)
    board.right(144)
    board.end_fill()
    # PART 5 - INNER PETAL RING (NESTED LOOP + FILL)
# The outer loop spins around 360 degrees (36 petals x 10 degrees each).
# The inner loop draws one square petal each rotation.
# Nesting loops inside loops is how complex patterns are built!
board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]
for i in range:(36)
board.color (petal_colors[i % len(petal_colors)],
petal_colors[(i + 2) % len(petal_colors)])
board.begin_fill()
for j in range(4):
board.forward (55)
board.right (90)
board.end_fill()
board.right (10)

#KEEP WINDOW OPEN
turtle.done()

    


