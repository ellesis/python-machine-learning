import turtle as t


def rectangle(horizontal, vertical, color):
  t.pendown()
  t.pensize(1)
  t.color(color)
  t.begin_fill()
  for couter in range(1, 3):
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
  t.end_fill()
  t.penup()

def setup():
  t.penup()
  t.speed('slow')
  t.bgcolor('Dodger blue')

def draw_robot():
  t.goto(-100,-150)
  rectangle(50, 20, 'blue')
  t.goto(-30, -150)
  rectangle(50, 20, 'blue')

def main():
  setup()
  draw_robot()
  t.hideturtle()
  t.mainloop()

if __name__ == "__main__":
    main()