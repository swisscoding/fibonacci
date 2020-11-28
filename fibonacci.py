#!/usr/local/bin/python3

import colored
import turtle
import math

print(colored.stylize("\n---- | Plotting Fibonacci Series | ----\n",
      colored.fg("red")))

def fibonacciPlot(n):
    x = 0
    y = 1
    square_x = x
    square_y = y

    t1.pencolor("black")
    t1.pensize(3)

    # 1. square
    for i in range(3):
        t1.forward(y * factor)
        t1.left(90)
    t1.forward(y * factor)

    # fibonacci series
    temp = square_y
    square_y = square_y + square_x
    square_x = temp

    # rest squares
    for i in range(1, n):
        t1.backward(square_x * factor)
        t1.right(90)
        t1.forward(square_y * factor)
        t1.left(90)
        t1.forward(square_y * factor)
        t1.left(90)
        t1.forward(square_y * factor)

        # fibonacci series
        temp = square_y
        square_y = square_y + square_x
        square_x = temp

    t1.penup()
    t1.setposition(factor, 0)
    t1.seth(0)
    t1.pendown()

    t1.pencolor("green")

    # fibonacci plotting
    t1.left(90)
    for i in range(n):
        print(y)
        angle = math.pi*y*factor/ 2
        angle /= 90
        for j in range(90):
            t1.forward(angle)
            t1.left(1)

        temp = x
        x = y
        y = temp + y

factor = 6

number_of_iterations = int(input("Number of iterations: "))
print()

if number_of_iterations > 0:
    print("Fibonacci series for", number_of_iterations, "elements:")
    t1 = turtle.Turtle()
    t1.speed(1000)
    fibonacciPlot(number_of_iterations)
    t1.ht()
    turtle.done()
else:
    print("error")
print()
