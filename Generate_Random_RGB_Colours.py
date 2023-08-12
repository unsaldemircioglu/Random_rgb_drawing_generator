import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r , g , b)
    return  random_color

#colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0, 90, 180, 270] # her bir rakam pusuladaki değerlerle eşşittir.
tim.pensize(15)

for _ in range(1200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
