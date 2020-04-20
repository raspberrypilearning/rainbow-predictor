#!/bin/python3

from sense_hat import SenseHat
import time

Sensor = SenseHat()
Sensor.clear()

R = [255, 0, 0]  # Rot
O = [255, 165, 0]  # Orange
Gb = [255, 255, 0] # Gelb
Gn = [0, 255, 0] # Grün
B = [0, 55, 155] # Blau
I = [25, 0, 255] # Indigo
V = [255, 0, 255] # Violett
X = [0, 0, 0] # aus


Regenbogen = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, Gb, Gb, Gb, Gb, Gb, Gb,
R, O, Gb, Gn, Gn, Gn, Gn, Gn,
R, O, Gb, Gn, B, B, B, B,
R, O, Gb, Gn, B, I, I, I,
R, O, Gb, Gn, B, I, V, V,                                                                   
R, O, Gb, Gn, B, I, V, X
]

while True:
  z = time.localtime() 
  s = z.tm_hour

  if Sensor.humidity > 80 and Sensor.temp > 20:
    Sensor.set_pixels(Regenbogen)
  elif Sensor.humidity > 80 and Sensor.temp < 0 :
    Sensor.clear([255, 255, 255]) # weißer Schnee
  elif Sensor.humidity <= 80 and Sensor.temp > 20 :
    Sensor.clear([255, 255, 0]) # gelbe Sonne
  else:
    Sensor.clear()
    
