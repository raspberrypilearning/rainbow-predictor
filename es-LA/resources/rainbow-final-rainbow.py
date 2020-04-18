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
X = [0, 0, 0]  # desactivado


arcoiris = [
R, R, R, R, R, R, R, R,
R, N, N, N, N, N, N, N,
R, N, A, A, A, A, A, A,
R, N, A, G, G, G, G, G,
R, N, A, G, B, B, B, B,
R, N, A, G, B, I, I, I,
R, N, A, G, B, I, V, V,                                                                   
R, N, A, G, B, I, V, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sensor.humidity > 80 and sensor.temp > 20:
    sensor.set_pixels(arcoiris)
  elif sensor.humidity > 80 and sensor.temp < 0 :
    sensor.clear([255, 255, 255]) # nieve blanca
  elif sensor.humidity <= 80 and sensor.temp > 20 :
    sensor.clear([255, 255, 0]) # sol amarillo
  else:
    sensor.clear()
    
