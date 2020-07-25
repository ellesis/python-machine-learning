import turtle as t

scn = t.Screen()
scn.setup(400, 400)
# scn.bgpic('filename')

t.shape('turtle')
t.forward(100)

def forward():
  t.forward(10)

def backward():
  t.forward(10)

def left():
  t.forward(10)

def right():
  t.forward(10)


scn.onkey(forward, "Up")
scn.onkey(backward, "Down")
scn.onkey(left, "Left")
scn.onkey(right, "Right")
scn.listen()

if __name__ == "__main__":
    main()