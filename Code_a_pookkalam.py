import turtle
import math
import random
t = turtle.Turtle()
screen=turtle.Screen()
screen.title("Pookkalam demo")
pen=turtle.Turtle()
t.width(1)

def draw_flower(x, y, petal_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(petal_color)

    for _ in range(6):
        t.speed(0)
        turtle.begin_fill()
        turtle.circle(20, 60)  # Draw a petal
        turtle.left(120)
        turtle.circle(20, 60)  # Draw a petal
        turtle.left(120)
        turtle.end_fill()
        turtle.left(60)  # Position for next petal

def draw_pookkalam():
    colors = ["white"]
    
    # Draw flowers in a circular pattern
    for i in range(12):
        angle = 360 / 12 * i
        x = 200 * math.cos(math.radians(angle))
        y = 200 * math.sin(math.radians(angle))
        draw_flower(x, y+15, random.choice(colors))
    
    # Draw the center of the pookkalam
    turtle.penup()

def draw_triangles():
    turtle.penup()
    turtle.goto(0, 15)
    turtle.setheading(90)  # Start facing up
    for i in range(12):
        turtle.pendown()
        turtle.color("orange")
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.end_fill()
        turtle.penup()
        turtle.right(30)

def smallCircle1(a,b,c,z,fillColor):
    original_pos=t.pos()
    original_heading=t.heading()
    t.color("black")
    t.speed(0)
    
    for i in range(b):
        center_x = a*math.cos(math.radians(z))
        center_y = a*math.sin(math.radians(z))
        z+=30
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.fillcolor(fillColor)
        t.begin_fill()
        t.circle(c)
        t.end_fill()
    
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)
    t.pendown()


def smallCircle2(a,b,c,z,fillColor):
    original_pos=t.pos()
    original_heading=t.heading()
    t.color("black")
    t.speed(0)
    
    for i in range(b):
        center_x = a*math.cos(math.radians(z))
        center_y = a*math.sin(math.radians(z))
        z+=30
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.fillcolor(fillColor)
        t.begin_fill()
        t.circle(c)
        t.end_fill()
    
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)
    t.pendown()

def FillCircle(color, radius):
    t.speed(0)
    t.penup()
    t.color(color)
    t.setheading(270)
    t.forward((radius-15))
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.forward(radius-15)
    t.setheading(0)

def SmallSquare(a,b,c,z,fillColor):
    original_pos=t.pos()
    original_heading=t.heading()
    t.color("black")
    t.speed(0)
    
    for i in range(b):
        center_x = a*math.cos(math.radians(z))
        center_y = a*math.sin(math.radians(z))
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(math.radians(z))
        z+=30
        t.pendown()
        t.fillcolor(fillColor)
        t.begin_fill()
        t.circle(c,360,4)
        t.end_fill()
    
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)

def draw_colored_circle():
    turtle.speed(0)  
   
    colors = ['red', 'green', 'blue', 'yellow']
    
    for i in range(4):
        turtle.fillcolor(colors[i])  
        turtle.begin_fill() 
        turtle.goto(0, 15)
        turtle.circle(55, 90) 
        turtle.goto(0, 15)
        turtle.setheading(90 - (i + 1) * 90) 
        turtle.end_fill() 

def draw_filled_wavy_circle(radius, wave_amplitude, wave_frequency, thickness, fill_color):
    turtle.speed(0)  
    turtle.hideturtle() 

    turtle.pensize(thickness)
    turtle.pencolor("orange")
    
    turtle.fillcolor(fill_color)

    turtle.penup()
    turtle.goto(radius, 15) 
    turtle.pendown()

    turtle.begin_fill()
  
    for angle in range(0, 360, 1): 
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        wave_offset = wave_amplitude * math.sin(wave_frequency * math.radians(angle))

        normal_x = math.cos(math.radians(angle))
        normal_y = math.sin(math.radians(angle))

        new_x = x + normal_x * wave_offset
        new_y = y + normal_y * wave_offset

        turtle.goto(new_x, new_y+15) 

radius = 135
wave_amplitude = 10 
wave_frequency = 10  
thickness = 5      
fill_color = "lightblue"


turtle.speed(0)
FillCircle("orange", 220)
turtle.speed(0)
draw_pookkalam()
FillCircle("red", 180)
FillCircle("white", 150)
SmallSquare(165, 12, 15,15, "orange")
SmallSquare(165, 12, 15,0, "white")
FillCircle("pink", 120)
draw_triangles()
draw_colored_circle()
draw_filled_wavy_circle(radius, wave_amplitude, wave_frequency, thickness, fill_color)

screen.exitonclick()