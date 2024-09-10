from turtle import Turtle, exitonclick

def draw_h():
    h = Turtle()
    h.color("pink")
    h.fillcolor("yellow")

    h.pensize(5)

    h.penup()
    h.goto(-110, 0)
    h.pendown()

    h.begin_fill()
    
    h.setheading(90)
    h.forward(80)

    h.right(90)
    h.forward(20)

    h.goto(n.xcor() + 80, h.ycor() - 70)



if __name__ == "__main__":
    draw_h()
    exitonclick()

