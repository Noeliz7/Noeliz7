import turtle

f = turtle.Turtle()

f.color("purple")
f.speed(9)
f.left(0)

f.penup
size=10
def petal():
  f.pendown()
  for x in range (40):
    f.forward(size)
    f.left(x)
  f.penup()
left_d=-15

for pet in range (8):
  petal()
  f.goto(0,0)
  f.left(-15)

if __name__ == "__main__":
  petal()