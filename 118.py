# import turtle
import turtle as trtl
bob = trtl.Turtle()
bob.speed(0)
bob.hideturtle()
# make bob's body
bob.pencolor("green")
bob.circle(90)
bob.penup()
bob.goto(0,10)
bob.pendown()
bob.circle(80)
# give bob his legs!
bobs_legs = 0
x = 0
y = 0
while (bobs_legs < 4):
   bob.penup()
   bob.goto(80 + x, 50 + y)
   bob.pendown()
   if bobs_legs is 0:
       bob.right(70)
       bob.forward(55)
       bob.right(20)
       bob.forward(10)
       bob.right(130)
       bob.forward(55)
       x = (x-160)
   elif bobs_legs is 1:
       bob.left(120)
       bob.forward(55)
       bob.left(20)
       bob.forward(10)
       bob.left(130)
       bob.forward(50)
       x = (x + 155)
       y = (y + 90)
   elif bobs_legs is 2:
       bob.right(70)
       bob.forward(55)
       bob.right(20)
       bob.forward(10)
       bob.right(130)
       bob.forward(50)
       x = (x - 150)
   elif bobs_legs is 3:
       bob.left(10)
       bob.forward(55)
       bob.left(20)
       bob.forward(10)
       bob.left(130)
       bob.forward(50)
   bobs_legs = (bobs_legs + 1)
 
# Bob needs a head
bobs_head = trtl.Turtle()
bobs_head.speed(0)
bobs_head.hideturtle()
bobs_head.pencolor("green")
 
bobs_head.penup()
bobs_head.goto(20, 178)
bobs_head.pendown()
bobs_head.left(80)
bobs_head.forward(20)
bobs_head.left(20)
bobs_head.forward(20)
 
bobs_head.up()
bobs_head.goto(20, 218)
bobs_head.setheading(120)
bobs_head.down()
bobs_head.circle(20, 120) 
 
bobs_head.pendown()
bobs_head.left(20)
bobs_head.forward(20)
bobs_head.left(20)
bobs_head.forward(20)
bobs_head.hideturtle()
 
# Creating an empty list of bob's shell patterns
my_bobs_shell_pattern_colors = []
# Choose colors for bob's back patterns
bob_bob_shell_pattern_colors = ["black", "gold"]
# Make bob's back patterns
bobx = 0
boby = 90
bob.penup()
for i in range(20):
   bob.goto (bobx,boby)
   bob.pendown()
   if i % 2 == 0:
       bob.color("gold")
       bob.forward(80)
       bob.left(20)
   else:
       bob.color("black")
       bob.forward(80)
       bob.left(20)
# Add a tail to our shelled friend
bobs_tail = trtl.Turtle()
bobs_tail.hideturtle()
bobs_tail.pencolor("green")
bobs_tail.penup()
bobs_tail.goto(-20,0)
bobs_tail.pendown()
 
bobs_tail.right(50)
bobs_tail.forward(30)
bobs_tail.left(95)
bobs_tail.forward(35)
 
# Lastly give bob blinking eyes
bobs_eyes = trtl.Turtle()
bobs_eyes.hideturtle()
 
bobs_eye_blink = 0
while (bobs_eye_blink < 1):
    bobs_eyes.penup()
    bobs_eyes.goto(20,200)
    bobs_eyes.pendown()
    bobs_eyes.fillcolor("black")
    bobs_eyes.begin_fill()
    bobs_eyes.circle(5)
    bobs_eyes.end_fill()
    bobs_eyes.fillcolor("green")
    bobs_eyes.begin_fill()
    bobs_eyes.circle(5)
    bobs_eyes.end_fill()
    bobs_eyes.penup()
    bobs_eyes.goto(-15,200)
    bobs_eyes.pendown()
    bobs_eyes.fillcolor("black")
    bobs_eyes.begin_fill()
    bobs_eyes.circle(5)
    bobs_eyes.end_fill()
    bobs_eyes.fillcolor("green")
    bobs_eyes.begin_fill()
    bobs_eyes.circle(5)
    bobs_eyes.end_fill()
 
 
 
 
wn = trtl.Screen()
wn.mainloop()
 
