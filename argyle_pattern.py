import turtle
from shapes import triangle

def main():
	Philip = turtle.Turtle()
	Philip.speed(0)

	setup(Philip)
	top_and_bottom_triangles(Philip)

def setup(Philip):
	Philip.penup()
	Philip.left(90)
	Philip.forward(400)
	Philip.left(90)
	Philip.forward(530)
	Philip.left(180)
	Philip.pendown()



def top_and_bottom_triangles(Philip):
	for count in range(5):
		Philip.color("red")
		Philip.triangle(Philip, "red")



#def side_triangles(Philip):


#def inside_diamonds(Philip):

main()
turtle.done()