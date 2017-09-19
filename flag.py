import turtle
from star import star
from shapes import rectangle

def main():
	Philip = turtle.Turtle()
	Philip.pensize(0)
	Philip.speed(1000000)

	setup(Philip)
	blue_field(Philip)
	draw_all_stars(Philip)
	stripe_start(Philip)
	#red_stripes(Philip)

def setup(Philip):
	Philip.penup()
	Philip.left(90)
	Philip.forward(400)
	Philip.left(90)
	Philip.forward(475)
	Philip.left(180)
	Philip.pendown()

def blue_field(Philip):
	Philip.color("blue")
	rectangle(Philip, 350, 250, "blue")
	

def draw_first_star(Philip):
	Philip.pensize(1)
	Philip.penup()
	Philip.forward(50)
	Philip.right(90)
	Philip.forward(25)
	Philip.left(90)
	Philip.pendown()
	star(Philip, "white")

def six_star_setup(Philip):
	Philip.penup()
	Philip.right(180)
	Philip.forward(250)
	Philip.left(90)
	Philip.forward(25)
	Philip.left(90)
	Philip.forward(25	)
	Philip.pendown()
	star(Philip, "white")

def five_star_setup(Philip):
	Philip.penup()
	Philip.right(180)
	Philip.forward(300)
	Philip.left(90)
	Philip.forward(25)
	Philip.left(90)
	Philip.forward(25)
	Philip.pendown()

def five_star_line(Philip):
	for count in range(5):
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")
	

def six_star_line(Philip):
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")
	Philip.penup()
	Philip.forward(50)
	Philip.pendown()
	star(Philip, "white")

	
def draw_all_stars(Philip):
	draw_first_star(Philip)
	six_star_line(Philip)
	five_star_setup(Philip)
	five_star_line(Philip)
	six_star_setup(Philip)
	six_star_line(Philip)
	five_star_setup(Philip)
	five_star_line(Philip)
	six_star_setup(Philip)
	six_star_line(Philip)
	five_star_setup(Philip)
	five_star_line(Philip)
	six_star_setup(Philip)
	six_star_line(Philip)
	five_star_setup(Philip)
	five_star_line(Philip)
	six_star_setup(Philip)
	six_star_line(Philip)


def stripe_start(Philip):
	Philip.penup()
	Philip.forward(50)
	Philip.left(90)
	Philip.forward(250)
	Philip.right(90)

def red_stripes(Philip):
	Philip.color("red")
	rectangle(Philip, , 100, "red")	

main()
turtle.done()