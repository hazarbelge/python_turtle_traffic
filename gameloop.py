
import pickle
import turtle
import random
import winsound

import playsound


arabagenisligi = 3
arabayuksekligi = 3
screen = turtle.Screen()
screen.title("Turtle Traffic")
screen.setup(1.0, 1.0)
background = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/arkaplan.gif"
araba1 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba1.gif"
araba2 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba2.gif"
araba3 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba3.gif"
araba4 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba4.gif"
araba5 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba5.gif"
araba6 = "C:/Users/hazar/PycharmProjects/Bilg.Muh.Gir.Oyun/GIFs/araba6.gif"
screen.bgcolor("grey")
screen.bgpic(background)
screen.update()
renkler = ["red", "blue", "green", "black", "purple", "yellow", "orange", "pink"]
car1 = turtle.Turtle()
car1x = -28
car1y = -290
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
car5 = turtle.Turtle()
car6 = turtle.Turtle()
car7 = turtle.Turtle()
skor = 0
highskor = 0
m = 0
ykonum1 = 500
ykonum2 = 540
ykonum3 = 680
ykonum4 = 840
ykonum5 = 980
ykonum6 = 1090
randx1 = random.randrange(-250,250)
randx2 = random.randrange(-250,250)
randx3 = random.randrange(-250,250)
randx4 = random.randrange(-250,250)
randx5 = random.randrange(-250,250)
randx6 = random.randrange(-250,250)
solatrue = False
sagatrue = False
asagitrue = True

def sola():
    global solatrue
    global sagatrue
    global asagitrue
    asagitrue = False
    sagatrue = False
    solatrue = True

def saga():
    global solatrue
    global sagatrue
    global asagitrue
    asagitrue = False
    solatrue = False
    sagatrue = True

def asagi():
    global solatrue
    global sagatrue
    global asagitrue
    solatrue = False
    sagatrue = False
    asagitrue = True

def bizimaraba():
    car1.color("black")
    car1.width(20)
    car1.penup()
    car1.setheading(90)
    car1.goto(car1x, car1y)
    car1.speed(0)
    car1.shapesize(arabagenisligi, arabayuksekligi, 5)
    car1.shape("turtle")

    turtle.listen()
    turtle.onkey(saga, "Right")
    turtle.onkey(sola, "Left")
    turtle.onkey(asagi, "Down")
    turtle.onkey(saga, "d")
    turtle.onkey(sola, "a")
    turtle.onkey(exit, "e")
    turtle.onkey(muzik, "m")


def gelenarabalar():
    car2.color("blue")
    car2.width(20)
    car2.penup()
    car2.setheading(270)
    car2.goto(randx1, ykonum1)
    car2.speed(0)
    car2.shapesize(arabagenisligi, arabayuksekligi, 5)
    car2.shape("turtle")

def gelenarabalar2():
    car3.color("green")
    car3.width(20)
    car3.penup()
    car3.setheading(270)
    car3.goto(randx2, ykonum2)
    car3.speed(0)
    car3.shapesize(arabagenisligi, arabayuksekligi, 5)
    car3.shape("turtle")

def gelenarabalar3():
    car4.color("red")
    car4.width(20)
    car4.penup()
    car4.setheading(270)
    car4.goto(randx3, ykonum3)
    car4.speed(0)
    car4.shapesize(arabagenisligi, arabayuksekligi, 5)
    car4.shape("turtle")

def gelenarabalar4():
    car5.color("yellow")
    car5.width(20)
    car5.penup()
    car5.setheading(270)
    car5.goto(randx4, ykonum4)
    car5.speed(0)
    car5.shapesize(arabagenisligi, arabayuksekligi, 5)
    car5.shape("turtle")

def gelenarabalar5():
    car6.color("purple")
    car6.width(20)
    car6.penup()
    car6.setheading(270)
    car6.goto(randx5, ykonum5)
    car6.speed(0)
    car6.shapesize(arabagenisligi, arabayuksekligi, 5)
    car6.shape("turtle")

def gelenarabalar6():
    car7.color("orange")
    car7.width(20)
    car7.penup()
    car7.setheading(270)
    car7.goto(randx6, ykonum6)
    car7.speed(0)
    car7.shapesize(arabagenisligi, arabayuksekligi, 5)
    car7.shape("turtle")


def muzik():
    global m
    m += 1
    oldtown = "Sounds/oldtown.wav"
    gangsta = "Sounds/gangsta.wav"
    highway = "Sounds/highway.wav"
    risingsun = "Sounds/risingsun.wav"
    tokyo = "Sounds/tokyo.wav"
    crash = "Sounds/crash.wav"
    if m == 1:
        winsound.PlaySound(oldtown, winsound.SND_ASYNC)
    if m == 2:
        winsound.PlaySound(highway, winsound.SND_ASYNC)
    if m == 3:
        winsound.PlaySound(risingsun, winsound.SND_ASYNC)
    if m == 4:
        winsound.PlaySound(tokyo, winsound.SND_ASYNC)
    if m == 5:
        winsound.PlaySound(gangsta, winsound.SND_ASYNC)
        m = 0
    if m == 6:
        winsound.PlaySound(crash, winsound.SND_ASYNC)
        m = 1

def exit():
    screen.bye()

def oyundongusu():

    yukleniyor = turtle.Turtle()
    yukleniyor.penup()
    yukleniyor.setposition(-30, 0)
    yukleniyor.write("Yükleniyor...", align="center", font=("Arial", 50, "normal"))
    bizimaraba()
    gelenarabalar()
    gelenarabalar2()
    gelenarabalar3()
    gelenarabalar4()
    gelenarabalar5()
    gelenarabalar6()
    yukleniyor.clear()
    yukleniyor.hideturtle()

    ykonum1 = 400
    ykonum2 = 540
    ykonum3 = 680
    ykonum4 = 840
    ykonum5 = 980
    ykonum6 = 1090
    car1x = car1.xcor()
    car1y = car1.ycor()
    randx1 = random.randrange(car1x - 150, car1x + 150)
    randx2 = random.randrange(car1x - 150, car1x + 150)
    randx3 = random.randrange(car1x - 150, car1x + 150)
    randx4 = random.randrange(car1x - 150, car1x + 150)
    randx5 = random.randrange(car1x - 150, car1x + 150)
    randx6 = random.randrange(car1x - 150, car1x + 150)
    try:
        with open('score.dat', 'rb') as file:
            highskor = pickle.load(file)
    except:
        highskor = 0
    skor = 0
    yazi = turtle.Turtle()
    yazi2 = turtle.Turtle()
    yazi3 = turtle.Turtle()
    yazi4 = turtle.Turtle()
    yazi.speed(0)
    yazi2.speed(0)
    yazi3.speed(0)
    yazi4.speed(0)
    yazi.color("white")
    yazi.penup()
    yazi.pencolor("black")
    yazi.setposition(-40, 260)
    yazi2.color("white")
    yazi2.penup()
    yazi2.pencolor("black")
    yazi2.setposition(-40, 330)
    yazi3.color("white")
    yazi3.penup()
    yazi3.pencolor("black")
    yazi3.setposition(-560, 300)
    yazi4.color("white")
    yazi4.penup()
    yazi4.pencolor("black")
    yazi4.setposition(530, 275)
    yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
    yazi2.write("En İyi Skor: {}".format(highskor), align="center", font=("Arial", 40, "normal"))
    yazi3.write("Müzik Değiştirmek için M'ye\nOyundan Çıkmak için  E'ye\nBasın", align="center", font=("Arial", 20, "normal"))
    yazi4.write("Sağa hareket için →(d)\nSola hareket için ←(a)\nDurmak için ↓(s)\nTuşlarını kullanabilirsiniz", align="center", font=("Arial", 20, "normal"))
    yazi.hideturtle()
    yazi2.hideturtle()
    yazi3.hideturtle()
    yazi4.hideturtle()

    oyuncalisiyor = True
    while oyuncalisiyor:
        if solatrue:
            car1x -= 6
            car1.goto(car1x, car1y)
        if sagatrue:
            car1x += 6
            car1.goto(car1x, car1y)
        if skor < 3:
            ykonum1 -= 6
            ykonum2 -= 6
            ykonum3 -= 6
            ykonum4 -= 6
            ykonum5 -= 6
            ykonum6 -= 6
        elif skor < 7:
            ykonum1 -= 7
            ykonum2 -= 7
            ykonum3 -= 7
            ykonum4 -= 7
            ykonum5 -= 7
            ykonum6 -= 7
        elif skor < 15:
            ykonum1 -= 8
            ykonum2 -= 8
            ykonum3 -= 8
            ykonum4 -= 8
            ykonum5 -= 8
            ykonum6 -= 8
        elif skor < 30:
            ykonum1 -= 9
            ykonum2 -= 9
            ykonum3 -= 9
            ykonum4 -= 9
            ykonum5 -= 9
            ykonum6 -= 9
        elif skor < 50:
            ykonum1 -= 10
            ykonum2 -= 10
            ykonum3 -= 10
            ykonum4 -= 10
            ykonum5 -= 10
            ykonum6 -= 10
        elif skor < 70:
            ykonum1 -= 11
            ykonum2 -= 11
            ykonum3 -= 11
            ykonum4 -= 11
            ykonum5 -= 11
            ykonum6 -= 11
        elif skor < 100:
            ykonum1 -= 12
            ykonum2 -= 12
            ykonum3 -= 12
            ykonum4 -= 12
            ykonum5 -= 12
            ykonum6 -= 12
        elif skor < 150:
            ykonum1 -= 12.5
            ykonum2 -= 12.5
            ykonum3 -= 12.5
            ykonum4 -= 12.5
            ykonum5 -= 12.5
            ykonum6 -= 12.5
        elif skor < 200:
            ykonum1 -= 12.8
            ykonum2 -= 12.8
            ykonum3 -= 12.8
            ykonum4 -= 12.8
            ykonum5 -= 12.8
            ykonum6 -= 12.8
        car2.goto(randx1, ykonum1)
        car3.goto(randx2, ykonum2)
        car4.goto(randx3, ykonum3)
        car5.goto(randx4, ykonum4)
        car6.goto(randx5, ykonum5)
        car7.goto(randx6, ykonum6)

        if ((-285 > ykonum1 > -292) and skor < 7) or ((-285 > ykonum1 > -294) and 7 <= skor < 70) or ((-285 > ykonum1 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum2 > -292) and skor < 7) or ((-285 > ykonum2 > -294) and 7 <= skor < 70) or ((-285 > ykonum2 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum3 > -292) and skor < 7) or ((-285 > ykonum3 > -294) and 7 <= skor < 70) or ((-285 > ykonum3 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum4 > -292) and skor < 7) or ((-285 > ykonum4 > -294) and 7 <= skor < 70) or ((-285 > ykonum4 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum5 > -292) and skor < 7) or ((-285 > ykonum5 > -294) and 7 <= skor < 70) or ((-285 > ykonum5 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum6 > -292) and skor < 7) or ((-285 > ykonum6 > -294) and 7 <= skor < 70) or ((-285 > ykonum6 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))

        if skor == highskor:
            with open('score.dat', 'wb') as file:
                pickle.dump(skor, file)

        if -170 < car1x < 130:
            if ykonum1 < -400:
                ykonum1 = 500
                randx1 = random.randrange(car1x - 150, car1x + 150)
            if ykonum2 < -400:
                ykonum2 = 500
                randx2 = random.randrange(car1x - 150, car1x + 150)
            if ykonum3 < -400:
                ykonum3 = 500
                randx3 = random.randrange(car1x - 150, car1x + 150)
            if ykonum4 < -400:
                ykonum4 = 500
                randx4 = random.randrange(car1x - 150, car1x + 150)
            if ykonum5 < -400:
                ykonum5 = 500
                randx5 = random.randrange(car1x - 150, car1x + 150)
            if ykonum6 < -400:
                ykonum6 = 500
                randx6 = random.randrange(car1x - 150, car1x + 150)

        elif not -170 < car1x < 130:
            if ykonum1 < -400:
                ykonum1 = 500
                randx1 = random.randrange(-320, 280)
            if ykonum2 < -400:
                ykonum2 = 500
                randx2 = random.randrange(-320, 280)
            if ykonum3 < -400:
                ykonum3 = 500
                randx3 = random.randrange(-320, 280)
            if ykonum4 < -400:
                ykonum4 = 500
                randx4 = random.randrange(-320, 280)
            if ykonum5 < -400:
                ykonum5 = 500
                randx5 = random.randrange(-320, 280)
            if ykonum6 < -400:
                ykonum6 = 500
                randx6 = random.randrange(-320, 280)

        car1x = car1.xcor()
        car1y = car1.ycor()
        car2x = car2.xcor()
        car3x = car3.xcor()
        car4x = car4.xcor()
        car5x = car5.xcor()
        car6x = car6.xcor()
        car7x = car7.xcor()

        if not -320 < car1x < 280:
            global m
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum1 < car1y < ykonum1 + 50) or (ykonum1 < car1y + 50 < ykonum1 + 50)) and ((car2x < car1x < car2x + 50) or (car2x < car1x + 50 < car2x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum2 < car1y < ykonum2 + 50) or (ykonum2 < car1y + 50 < ykonum2 + 50)) and ((car3x < car1x < car3x + 50) or (car3x < car1x + 50 < car3x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum3 < car1y < ykonum3 + 50) or (ykonum3 < car1y + 50 < ykonum3 + 50)) and ((car4x < car1x < car4x + 50) or (car4x < car1x + 50 < car4x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum4 < car1y < ykonum4 + 50) or (ykonum4 < car1y + 50 < ykonum4 + 50)) and ((car5x < car1x < car5x + 50) or (car5x < car1x + 50 < car5x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum5 < car1y < ykonum5 + 50) or (ykonum5 < car1y + 60 < ykonum5 + 50)) and ((car6x < car1x < car6x + 50) or (car6x < car1x + 50 < car6x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()
        if ((ykonum6 < car1y < ykonum6 + 50) or (ykonum6 < car1y + 60 < ykonum6 + 50)) and ((car7x < car1x < car7x + 50) or (car7x < car1x + 50 < car7x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            oyundongusu()


muzik()
oyundongusu()













