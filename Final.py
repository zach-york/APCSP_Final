import turtle

def main():
	Philip = turtle.Turtle()
	Philip.pensize(0)
	Philip.speed(1000000000)

	directions(Philip)
	setup(Philip)
	colors(Philip)
	outline_of_2x2(Philip)

def setup(Philip):
	Philip.pensize(5)
	Philip.color("black")
	Philip.penup()
	Philip.right(180)
	Philip.forward(300)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.pendown()
 
def directions(Philip):
	Philip.write('''
This is a 2D 2x2 Rubik's cube simulator. At the bottom, 
please input a scramble and the cube will be
 scrambled accordingly
Moves on a Rubik's cube are as follows:
U, U' F, F', R, R', L, L', D, D', B and B'
U is the top layer
F is front face
R is the right side
L is the left side
D is the bottom layer
B is the back face, opposite the F

A normal move, U, R, L, etc. or a letter without a prime 
symbol (', U', R', etc.) is clockwise
 on that face while a prime 
or inverse move is counter clockwise

The move U R U' R' has been preset
''', align="left", font=("Arial", 10, "normal"))

def outline_of_2x2(Philip):
	#outline
	Philip.pendown()
	Philip.color("black")
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(200)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(200)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(200)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(200)
	Philip.right(90)
	Philip.forward(100)
	Philip.left(90)
	#2x2 shape
	Philip.pensize(2)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(180)
	Philip.forward(400)
	Philip.right(90)
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(180)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(300)
	Philip.right(90)
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(100)
	Philip.left(90)
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(150)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(250)
	Philip.right(90)
	Philip.forward(100)
	Philip.right(90)



def colors(Philip):
	color1 = "orange"
	color2 = "green"
	color3 = "white"
	color4 = "yellow"
	color5 = "red"
	color6 = "blue"

	Philip.color(color1)
	square(Philip)
	Philip.forward(100)
	Philip.color(color2)
	square(Philip)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.color(color3)
	square(Philip)
	Philip.right(90)
	Philip.forward(200)
	Philip.left(90)
	Philip.color(color4)
	square(Philip)
	Philip.left(90)
	Philip.forward(100)
	Philip.right(90)
	Philip.forward(100)
	Philip.color(color5)
	square(Philip)
	Philip.forward(100)
	Philip.color(color6)
	square(Philip)
	Philip.right(180)
	Philip.forward(300)
	Philip.right(180)


def	square(Philip):
	Philip.pendown()
	Philip.begin_fill()
	for count in range(4):
		Philip.forward(100)
		Philip.right(90)
	Philip.end_fill()
	Philip.penup()

def turns(Notation):
	if Notation == "U" or "U'" or "R" or "R'" or "L" or "L'" or "B" or "B'" or "D" or "D'" or "F" or "F'":
		if Notation == "U":
			print
	else:
		print "Please enter correct Rubik's Cube notation"




main()
turns("U'")
turtle.done()
