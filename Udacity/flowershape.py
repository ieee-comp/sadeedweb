import turtle

def draw_shape():

    window = turtle.Screen()
    window.bgcolor("white")

    kait = turtle.Turtle()
    kait.shape("triangle")
    kait.color("blue")
    kait.speed(15)

    kait.right(-90)
    kait.forward(300)

    counter = 0
    while counter < 36:
     
        #create a triangle
        count = 0
        while count < 4:
            kait.forward(120)
            kait.right(120)
            count = count + 1
        #end of triangle


        counter = counter + 1
        kait.forward(120)
        kait.right(10)
        
    window.exitonclick()

draw_shape()
