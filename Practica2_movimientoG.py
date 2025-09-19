import turtle

# Configurar ventana
ventana = turtle.Screen()
ventana.setup(width=600, height=600)

# Crear turtle para dibujar
t = turtle.Turtle()
t.hideturtle()  # Ocultar el turtle, solo veremos el cuadrado
t.penup()
t.speed(10)

# Posición inicial
x, y = 0, 0

# Función para dibujar el cuadrado
def cuadrado():
    t.clear()  # Borrar el cuadrado anterior
    t.goto(x, y)
    t.pendown()
    t.forward(30)  # Mover un poco para que el cuadrado no se dibuje en el centro
    t.right(90)
    t.forward(30)  # Mover un poco para que el cuadrado no se dibuje en el centro
    t.right(90)
    t.forward(30)  # Mover un poco para que el cuadrado no se dibuje en el centro
    t.right(90)
    t.forward(30)  # Mover un poco para que el cuadrado no se dibuje en el centro
    t.penup()

# Dibujar cuadrado inicial
cuadrado()

# Funciones de movimiento
def arriba():
    global y
    y += 10
    cuadrado()

def abajo():
    global y
    y -= 10
    cuadrado()

def izquierda():
    global x
    x -= 10
    cuadrado()

def derecha():
    global x
    x += 10
    cuadrado()

# Enlazar teclas
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

ventana.mainloop()