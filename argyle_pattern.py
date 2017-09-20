import turtle

def main():
	Philip = turtle.Turtle()
	Philip.speed(0)

	setup(Philip)
	top_and_bottom_triangles(Philip)
	side_triangles(Philip)

def setup(Philip):
	Philip.penup()
	Philip.left(90)
	Philip.forward(400)
	Philip.left(90)
	Philip.forward(530)
	Philip.left(180)
	Philip.pendown()



def top_and_bottom_triangles(Philip):
	for count in range(10):
		Philip.color("red")
		Philip.begin_fill()
		Philip.right(60)
		Philip.forward(100)
		Philip.left(120)
		Philip.forward(100)
		Philip.left(120)
		Philip.forward(100)
		Philip.end_fill()
		Philip.left(180)
		Philip.forward(100)

	Philip.penup()
	Philip.right(90)
	Philip.forward(800)
	Philip.right(90)
	Philip.forward(1000)
	Philip.right(180)
	Philip.pendown()
	for count in range(10):
		Philip.color("red")
		Philip.begin_fill()
		Philip.left(60)
		Philip.forward(100)
		Philip.right(120)
		Philip.forward(100)
		Philip.right(120)
		Philip.forward(100)
		Philip.end_fill()
		Philip.right(180)
		Philip.forward(100)




def side_triangles(Philip):
	for count in range(10):
		

#def inside_diamonds(Philip):

main()
turtle.done()