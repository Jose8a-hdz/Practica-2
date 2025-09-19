import turtle

# Configurar ventana
ventana = turtle.Screen()
ventana.setup(width=600, height=600)

# Crear turtle para dibujar
t = turtle.Turtle()
t.hideturtle()  # Ocultar el turtle, solo veremos el circulo
t.penup()
t.speed(0)

# Posición inicial
x, y = 0, 0

# Función para dibujar el circulo
def circulo():
    t.clear()  # Borrar el circulo anterior
    t.goto(x, y)
    t.pendown()
    t.circle(50)
    t.penup()

# Dibujar circulo inicial
circulo()

# Funciones de movimiento
def arriba():
    global y
    y += 10
    circulo()

def abajo():
    global y
    y -= 10
    circulo()

def izquierda():
    global x
    x -= 10
    circulo()

def derecha():
    global x
    x += 10
    circulo()

# Enlazar teclas
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

ventana.mainloop()