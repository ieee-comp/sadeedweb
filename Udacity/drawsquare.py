import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("red")
    brad.speed(5)

    #circle using squares
    counter = 0
    while counter < 36:
        
        #draw square
        
        count = 0
        while count < 4:
                
            brad.forward(100)
            brad.right(90)
            count = count + 1
            #end of square

        counter = counter + 1
        brad.right(10)
            
    window.exitonclick()
"""
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    sarah = turtle.Turtle()
    sarah.shape("turtle")
    sarah.color("orange")
    sarah.speed(3)

    count = 0
    while count < 3:
        
        sarah.forward(160)
        sarah.left(120)
        count = count + 1
        
"""


draw_shape()    


