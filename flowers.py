from turtle import *
from colorsys import *

bgcolor('black')
speed(0)
h = 0

# Ajustar la posición vertical del texto
up()
setpos(0, 400)  # Ajusta este valor según sea necesario
down()

# Configurar el estilo del texto
style = ('Courier', 30, 'italic')
color('white')

# Escribir el texto en la parte superior de la ventana
write("11/07/20", move=False, align="center", font=style)

# Mover a la posición inicial para el dibujo
up()
setpos(0, 0)
down()

for i in range(500):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    circle(-i  * 0.68, 200)
    right(80)

print("Finished")
done()
