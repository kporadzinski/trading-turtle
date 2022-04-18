import turtle
import random
import math

def kos(marg,efect) :
    postep = abs(marg*efect-marg)
    timekrok = 5

    dyst = math.sqrt(postep**2+timekrok**2)
    return (math.asin(postep/dyst))*180/math.pi,dyst



def test_turtle(time,loss=0.8,win=1.34):
    kazik = turtle.Turtle()
    kazik.speed(1)
    margin = 2.5
    loss_count = 0
    win_count = 0
    randt = [random.randrange(100) for i in range(time)]

    for i in randt:
        if i>65:
            kazik.color('red')
            angle,dyst=kos(margin,loss)
            margin=margin*loss
            loss_count+=1
            kazik.rt(angle)
            kazik.fd(dyst)
            kazik.lt(angle)
        else:
            kazik.color('green')
            angle,dyst=kos(margin,win)
            margin=margin*win
            win_count+=1
            kazik.lt(angle)
            kazik.fd(dyst)
            kazik.rt(angle)

    turtle.mainloop()

# kazik = turtle.Turtle()
# kazik.speed(1)
# kazik.fd(100)
# kazik.lt(23)
# kazik.fd(23)
#
#
# turtle.mainloop()

test_turtle(40,0.9)
