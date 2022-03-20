#Basic Python Course - Star turtle
import turtle
import random

tao = turtle.Pen()
tao.shape('turtle')

taosc = turtle.Screen()
taosc.bgcolor('black')


color = ['red','blue','green','yellow','orange','purple']
random_size = [10,20,30,40,50,60,70,80,90,100]

def Star_Shape(size=50):
    for i in range(5):
        tao.forward(size)
        tao.right(144)

for i in range(100):
    x = random.randint(-400,400)
    y = random.randint(-300,300)
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    colors = random.choice(color)
    tao.color(colors)
    randomsizes = random.choice(random_size)
    Star_Shape(randomsizes)
