import turtle

# Crear una ventana de turtle
ventana = turtle.Screen()
ventana.bgcolor("white")

# Crear una tortuga
t = turtle.Turtle()
t.color("red")
t.pensize(3)

# Dibujar el corazón
t.up()
t.goto(-50,0)
t.down()
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Finalizar el programa
turtle.done()
