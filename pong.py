import turtle

# Creamos una ventana
wn = turtle.Screen()
# wn por ventana en ingles
wn.title("Pong por Josema")
wn.bgcolor("black")
wn.setup(width=000, height=600)
wn.tracer(0)

# Jugador A
jugadorA= turtle.Turtle()
jugadorA.speed(0)
# Para que aparezca al toque nada mas empezar e; juego
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

# Jugador B
jugadorB= turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

# Pelota
Pelota = turtle.Turtle()
Pelota .speed(0)
Pelota.shape("circle")
Pelota.color("white")
Pelota.penup()
Pelota.goto(0,0)
Pelota.dx = 3
Pelota.dy = 3

# Funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

# Conectar teclado al programa
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")


while True:
    wn.update()

    Pelota.setx(Pelota.xcor() + Pelota.dx)
    Pelota.sety(Pelota.ycor() + Pelota.dy)