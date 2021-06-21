#KochDraw.py @shiqiang oct.2019 macOS python 2.7
# -*- coding: utf-8 -*-
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 90, -90, -90,90]:
           turtle.left(angle)
           koch(size/3, n-1)


def main():
    turtle.setup(1080,1080)
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    turtle.pensize(1)
    turtle.speed(0) #fastest
    turtle.pencolor('red')
    level =3   # 科赫雪花，阶数
    S=600
    koch(S,level)     
    turtle.right(180)
    koch(S,level)
#    turtle.right(120)
#    koch(S,level)
#    turtle.right(120)
#    koch(S,level)
    turtle.hideturtle()


main()
