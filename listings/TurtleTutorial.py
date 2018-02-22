#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:04:59 2017

@author: Vincent Gregoire

# Turtle tutorial

Prepared by [Vincent Grégoire](http://www.vincentgregoire.com), 
Department of Finance, The University of Melbourne. 

This is a sample code to illustrate some basic features of the Python language.
This notebook was created as supplemental material to a Python for 
financial research bootcamp for finance honours and PhD students at 
the University of Melbourne in March of 2017.

Last update: March 24, 2017.

**Contact**: <vincent.gregoire@unimelb.edu.au>

Latest version: <http://www.vincentgregoire.com/python-bootcamp/>
"""

import turtle

# Let's create our turtle. We'll call it Bob

bob = turtle.Turtle()

# He doesn't look much like a turtle, but we can fix that.
bob.shape(name='turtle')


# We can move Bob different ways.

bob.forward(100)
bob.backward(100)
bob.left(45)

# We can draw with Bob
bob.pendown()
bob.pencolor('red')
bob.forward(100)

# Let's start again
bob.reset()

# Let's draw a square the hard way.

bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)

# That's no good. We can use loops for that (Exercise!)

bob.reset()

for i in range(4):
    bob.forward(100)
    bob.right(90)

# Now let's write a function to draw a square of any size

def drawSquare(size):
    for i in range(4):
        bob.forward(size)
        bob.right(90)

drawSquare(50)
drawSquare(200)

# We can even add an optional color argument, and take any turtle!

def drawSquare(turt, size, color=None):
    if color is not None:
        # Save current pen details
        old_color = turt.getpen().color()[0]
        turt.pencolor(color)
    
    for i in range(4):
        turt.forward(size)
        turt.right(90)
        
    if color is not None:
        # Reset  pen details
        turt.pencolor(old_color)
        
drawSquare(bob, 200)
drawSquare(bob, 200, 'red')

# Say we want to draw squares of squares size (!?!?!)

bob.reset()

squares = [x*x for x in range(1,21)]

for x in squares:
    drawSquare(bob, x)
    

# Say we wanted a function to draw any Shape?

def drawShape(turt, size, sides):
    # First, we need the angle. A full loop is 360 degrees, each angle is
    # a fraction of that. We have the same number of angles as sides.
    angle = 360.0/sides
    for i in range(sides):
        turt.forward(size)
        turt.right(angle)

drawShape(bob, 100,10)

drawShape(bob, 10,30)

bob.reset()

# We can draw more complex shapes by combining them
# Say we want a house

def drawHouse(turt, size):
    drawSquare(turt, size)
    turt.left(60)
    drawShape(turt, size, 3)
    turt.right(60)
    turt.penup()
    turt.right(45)
    turt.forward(size/5.0)
    turt.left(45)
    turt.pendown()
    drawSquare(turt, size/2.5)
    turt.penup()
    turt.right(45)
    turt.backward(size/5.0)
    turt.left(45)
    turt.pendown()

drawHouse(bob, 100)


# Now we can draw a full neighborhood... but it's a lot of work deciding where
# to place the house. Let's leave it to chance.

bob.reset()

from numpy.random import random

# random() will return a number between 0 and 1.
random()

# We can generate many at a time
random(5)

def drawNeigborhood(turt, houses=10):
    # In this case, we need 3 numbers: size, x and y coordinates.
    # But it looks better if size is a function of the y coordinate
    # (close == looks bigger).
    rnd = random((houses, 2))
    # Size is between 10 and 80, x and y between -200 and +200
    rnd = (rnd * (200 - (-200))) -200
    
    for i in range(houses):
        turt.penup()
        turt.setposition(rnd[i,0], rnd[i, 1])
        turt.pendown()
        y = rnd[i, 1]
        # For size, we want to smooth it, bigger at -200 (80) at smallest at
        # back (10)
        size = 80 - (((y + 200) / 400) * (80 - 10))
        drawHouse(turt, size)

drawNeigborhood(bob, 5)

turtle.done()