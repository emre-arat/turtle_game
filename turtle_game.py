import turtle
import random
import time

window = turtle.Screen()
window.bgcolor("white")
simge = turtle.Turtle()
simge.shape("turtle")
simge.color("green")
simge.penup()
score_turtle = turtle.Turtle()
kalan_turtle = turtle.Turtle()

####

xxx = 0
def score(puan):

    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.sety(240)
    score_turtle.color("blue")
    score_turtle.write(f"Score:{puan} ",False,align="center", font=("Arial",30,"normal"))

def kalan(zaman):
    global numara
    kalan_turtle.hideturtle()
    kalan_turtle.penup()
    kalan_turtle.sety(200)
    kalan_turtle.color("red")
    kalan_turtle.clear()
    kalan_turtle.write(f"time:{zaman} ",False,align="center", font=("Arial",30,"normal"))
    numara -= 1




def locate():
    global numara
    turtle.tracer(0)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    simge.setx(x)
    simge.sety(y)
    turtle.tracer(1)
    kalan(numara)
    if numara > 0:
        window.ontimer(locate, 1000)
    else:
        kalan_turtle.clear()
        kalan_turtle.write("GAME OVER ", False, align="center", font=("Arial", 30, "normal"))
        simge.hideturtle()




def hand_click(x,y):
    global xxx
    xxx += 1
    score_turtle.clear()
    score_turtle.write(f"Score:{xxx} ", False, align="center", font=("Arial", 30, "normal"))
    print(x,y)

numara = 60
if numara > 0:
    simge.onclick(hand_click)
    locate()
    time.sleep(1)
    score(xxx)
    kalan(numara)
    window.listen()
    window.onkeypress(fun=locate,key="space")
    numara += -1
else:
    print("game over")



window.mainloop()


