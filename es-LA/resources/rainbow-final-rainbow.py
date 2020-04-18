#!/bin/python3

from sense_hat import SenseHat
import time

sensor = SenseHat()
sensor.clear()

R = [255, 0, 0]  # rojo
N = [255, 165, 0]  # naranja
A = [255, 255, 0] # amarillo
G = [0, 255, 0] # verde
B = [0, 55, 155] # azul
I = [25, 0, 255] # indigo
V = [255, 0, 255] # violeta
X = [0, 0, 0]  # off


rainbow = [
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

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(rainbow)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear([255, 255, 255]) # white snow
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # yellow sun
  else:
    sense.clear()
    
