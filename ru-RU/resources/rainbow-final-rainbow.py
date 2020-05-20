#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0]  # красный
O = [255, 165, 0]  # оранжевый
Y = [255, 255, 0] # желтый
G = [0, 255, 0] # зеленый
B = [0, 55, 155] # темно-синий
I = [25, 0, 255] # синий
V = [255, 0, 255] # фиолетовый
X = [0, 0, 0]  # выключить


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
    
