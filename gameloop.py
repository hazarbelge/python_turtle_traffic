import pickle
import turtle
import random
import winsound
import time


# degiskenleri tanimliyoruz
arabagenisligi = 1
arabayuksekligi = 1
screen = turtle.Screen()
screen.title("Turtle Traffic")
screen.setup(1.0, 0.95)
background = "GIFs/arkaplan.gif"
araba1 = "GIFs/araba1.gif"
araba2 = "GIFs/araba2.gif"
araba3 = "GIFs/araba3.gif"
araba4 = "GIFs/araba4.gif"
araba5 = "GIFs/araba5.gif"
araba6 = "GIFs/araba6.gif"
araba7 = "GIFs/araba7.gif"
bosses = "Sounds/bosses.wav"
screen.addshape(araba1)
screen.addshape(araba2)
screen.addshape(araba3)
screen.addshape(araba4)
screen.addshape(araba5)
screen.addshape(araba6)
screen.addshape(araba7)
screen.bgcolor("grey")
screen.bgpic(background)
screen.update()
renkler = ["red", "blue", "green", "black", "purple", "yellow", "orange", "pink"]
car1 = turtle.Turtle()
car1x = -30
car1y = -290
car2 = turtle.Turtle()
car3 = turtle.Turtle()
car4 = turtle.Turtle()
car5 = turtle.Turtle()
car6 = turtle.Turtle()
car7 = turtle.Turtle()
yazi = turtle.Turtle()
yazi2 = turtle.Turtle()
yazi3 = turtle.Turtle()
yazi4 = turtle.Turtle()
yukleniyor = turtle.Turtle()
skor = 0
highskor = 0
m = 0
ykonum1 = 500
ykonum2 = 540
ykonum3 = 680
ykonum4 = 840
ykonum5 = 980
ykonum6 = 1090
randx1 = random.randrange(-250, 250)
randx2 = random.randrange(-250, 250)
randx3 = random.randrange(-250, 250)
randx4 = random.randrange(-250, 250)
randx5 = random.randrange(-250, 250)
randx6 = random.randrange(-250, 250)
solatrue = False
sagatrue = False


# hareketleri tanimliyoruz
def sola():
    global solatrue
    solatrue = True


def soladur():
    global solatrue
    solatrue = False


def saga():
    global sagatrue
    sagatrue = True


def sagadur():
    global sagatrue
    sagatrue = False

# kontrol ettigimiz araba
def bizimaraba():
    car1.color("black")
    car1.width(20)
    car1.penup()
    car1.setheading(90)
    car1.goto(car1x, car1y)
    car1.speed(0)
    car1.shapesize(arabagenisligi, arabayuksekligi, 5)
    car1.shape(araba1)

    turtle.listen()
    turtle.onkeypress(saga, "Right")
    turtle.onkeyrelease(sagadur, "Right")
    turtle.onkeypress(sola, "Left")
    turtle.onkeyrelease(soladur, "Left")
    turtle.onkeypress(saga, "d")
    turtle.onkeyrelease(sagadur, "d")
    turtle.onkeypress(sola, "a")
    turtle.onkeyrelease(soladur, "a")
    turtle.onkey(exitgame, "e")
    turtle.onkey(muzik, "m")


# ekranin yukarisindan gelen arabalar
def gelenarabalar():
    car2.width(20)
    car2.penup()
    car2.speed(0)
    car2.shapesize(arabagenisligi, arabayuksekligi, 1)
    car2.shape(araba2)


def gelenarabalar2():
    car3.width(20)
    car3.penup()
    car3.speed(0)
    car3.shapesize(arabagenisligi, arabayuksekligi, 1)
    car3.shape(araba3)


def gelenarabalar3():
    car4.width(20)
    car4.penup()
    car4.speed(0)
    car4.shapesize(arabagenisligi, arabayuksekligi, 1)
    car4.shape(araba4)


def gelenarabalar4():
    car5.width(20)
    car5.penup()
    car5.speed(0)
    car5.shapesize(arabagenisligi, arabayuksekligi, 1)
    car5.shape(araba5)


def gelenarabalar5():
    car6.width(20)
    car6.penup()
    car6.speed(0)
    car6.shapesize(arabagenisligi, arabayuksekligi, 1)
    car6.shape(araba6)


def gelenarabalar6():
    car7.width(20)
    car7.penup()
    car7.speed(0)
    car7.shapesize(arabagenisligi, arabayuksekligi, 1)
    car7.shape(araba7)


# m tusuna bastikca muzigi degistiriyoruz
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
        m = 0


# e tusu ile oyundan cikis
def exitgame():
    winsound.PlaySound(bosses, winsound.SND_ASYNC)
    global oyuncalisiyor
    oyuncalisiyor = False
    turtle.bye()


def oyundongusu():
    # oyunun baslangic sekansi
    muzik()
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

    # yukaridan gelen arabalarin y konumlari belirleyip x konumlarini random atiyoruz.
    ykonum1 = 410
    ykonum2 = 550
    ykonum3 = 690
    ykonum4 = 850
    ykonum5 = 990
    ykonum6 = 1120
    car1x = car1.xcor()
    car1y = car1.ycor()
    randx1 = random.randrange(car1x - 150, car1x + 150)
    randx2 = random.randrange(car1x - 150, car1x + 150)
    randx3 = random.randrange(car1x - 150, car1x + 150)
    randx4 = random.randrange(car1x - 150, car1x + 150)
    randx5 = random.randrange(car1x - 150, car1x + 150)
    randx6 = random.randrange(car1x - 150, car1x + 150)

    # score.dat dosyasindan highscore bakiyor. Eger olusturulmamis ise 0 kabul ediyor.
    try:
        with open('score.dat', 'rb') as file:
            highskor = pickle.load(file)
    except:
        highskor = 0

    skor = 0

    # Ekrandaki bilgi yazilari
    yazi.speed(0)
    yazi2.speed(0)
    yazi3.speed(0)
    yazi4.speed(0)
    yazi.penup()
    yazi.pencolor("black")
    yazi.setposition(-40, 270)
    yazi2.penup()
    yazi2.pencolor("black")
    yazi2.setposition(-40, 345)
    yazi3.penup()
    yazi3.pencolor("black")
    yazi3.setposition(-560, 300)
    yazi4.penup()
    yazi4.pencolor("black")
    yazi4.setposition(530, 300)
    yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
    yazi2.write("En İyi Skor: {}".format(highskor), align="center", font=("Arial", 40, "normal"))
    yazi3.write("Müzik Değiştirmek için M'ye\nOyundan Çıkmak için  E'ye\nBasın", align="center",
                font=("Arial", 20, "normal"))
    yazi4.write("Sağa hareket için →(d)\nSola hareket için ←(a)\nTuşlarını kullanabilirsiniz", align="center",
                font=("Arial", 20, "normal"))
    yazi.hideturtle()
    yazi2.hideturtle()
    yazi3.hideturtle()
    yazi4.hideturtle()

    oyuncalisiyor = True
    while oyuncalisiyor:
        # saga ve sola hareketler
        if solatrue:
            car1x -= 7
            car1.goto(car1x, car1y)
        if sagatrue:
            car1x += 7
            car1.goto(car1x, car1y)

        # skor arttikca arabalarin hizini arttiriyoruz.
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

        # Arabalari gectikce skoru arttiriyoruz. Ardindan skoru (ve gerekirse highscore) tekrardan yazdiriyoruz.
        if ((-285 > ykonum1 > -292) and skor < 7) or ((-285 > ykonum1 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum1 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum2 > -292) and skor < 7) or ((-285 > ykonum2 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum2 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum3 > -292) and skor < 7) or ((-285 > ykonum3 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum3 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum4 > -292) and skor < 7) or ((-285 > ykonum4 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum4 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum5 > -292) and skor < 7) or ((-285 > ykonum5 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum5 > -296) and skor >= 70):
            skor += 1
            yazi.clear()
            yazi.write("Skor: {}".format(skor), align="center", font=("Arial", 38, "normal"))
            if skor > highskor:
                highskor += 1
                yazi2.clear()
                yazi2.write("En İyi Skor: {}".format(skor), align="center", font=("Arial", 40, "normal"))
        if ((-285 > ykonum6 > -292) and skor < 7) or ((-285 > ykonum6 > -294) and 7 <= skor < 70) or (
                (-285 > ykonum6 > -296) and skor >= 70):
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

        # Kontrol ettigimiz arabanin konumuna göre arabalari gönderiyor(oyunu zorlastirmak adina)
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

        # Carpma durumlari
        # Ekrandaki sag ve sol bariyerlere carpma durumu
        if not -320 < car1x < 280:
            global m
            m = 5
            yazi.clear()
            yazi2.clear()
            screen.delay()
            muzik()
            time.sleep(2.2)
            oyundongusu()
        # Arabalara carpma durumu
        if ((ykonum1 < car1y < ykonum1 + 90) or (ykonum1 < car1y + 90 < ykonum1 + 90)) and (
                (car2x < car1x < car2x + 50) or (car2x < car1x + 50 < car2x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()
        if ((ykonum2 < car1y < ykonum2 + 90) or (ykonum2 < car1y + 90 < ykonum2 + 90)) and (
                (car3x < car1x < car3x + 50) or (car3x < car1x + 50 < car3x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()
        if ((ykonum3 < car1y < ykonum3 + 90) or (ykonum3 < car1y + 90 < ykonum3 + 90)) and (
                (car4x < car1x < car4x + 50) or (car4x < car1x + 50 < car4x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()
        if ((ykonum4 < car1y < ykonum4 + 90) or (ykonum4 < car1y + 90 < ykonum4 + 90)) and (
                (car5x < car1x < car5x + 50) or (car5x < car1x + 50 < car5x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()
        if ((ykonum5 < car1y < ykonum5 + 90) or (ykonum5 < car1y + 90 < ykonum5 + 90)) and (
                (car6x < car1x < car6x + 50) or (car6x < car1x + 50 < car6x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()
        if ((ykonum6 < car1y < ykonum6 + 90) or (ykonum6 < car1y + 90 < ykonum6 + 90)) and (
                (car7x < car1x < car7x + 50) or (car7x < car1x + 50 < car7x + 50)):
            m = 5
            muzik()
            yazi.clear()
            yazi2.clear()
            screen.delay()
            time.sleep(2.2)
            oyundongusu()


oyundongusu()














