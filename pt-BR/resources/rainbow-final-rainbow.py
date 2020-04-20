#!/bin/python3

from sense_hat import SenseHat
import time

sensor = SenseHat()
sensor.clear()

R = [255, 0, 0] # red / vermelho
O = [255, 165, 0]  # orange / laranja
Y = [255, 255, 0] # yellow / amarelo
G = [0, 255, 0] # green / verde
B = [0, 55, 155] # blue / azul
I = [25, 0, 255] # indigo / índigo
V = [255, 0, 255] # violet / violeta
X = [0, 0, 0]  # off / apagado


arcoiris = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, Y, Y, Y, Y, Y, Y,
R, O, Y, G, G, G, G, G,
R, O, Y, G, B, B, B, B,
R, O, Y, G, B, I, I, I,
R, O, Y, G, B, I, V, V,                                                                   
R, O, Y, G, B, I, V, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sensor.humidity > 80 and sensor.temp > 20:
    sensor.set_pixels(arcoiris)
  elif sensor.humidity > 80 and sensor.temp < 0 :
    sensor.clear([255, 255, 255]) # white snow / branco neve
  elif sensor.humidity <= 80 and sensor.temp > 20 :
    sensor.clear([255, 255, 0]) # yellow sun / amarelo sol
  else:
    sensor.clear()
    
