import turtle

# Crear una ventana de turtle
ventana = turtle.Screen()
ventana.bgcolor("white")

# Crear una tortuga
t = turtle.Turtle()
t.color("purple")
t.pensize(3)

# Dibujar el trisquel
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.right(60)
t.forward(100)
t.left(120)
t.forward(100)

# Finalizar el programa
turtle.done()
