#!/bin/python3

from sense_hat import SenseHat
import time

sensor = SenseHat()
sensor.clear()

R = [255, 0, 0]  # Rojo
N = [255, 165, 0]  # Naranja
AM = [255, 255, 0] # AMarillo
V = [0, 255, 0] # Verde
A = [0, 55, 155] # Azul
AN = [25, 0, 255] # AÑil
VI = [255, 0, 255] # VIoleta
X = [0, 0, 0]  # Apagado


arco_iris = [
R, R, R, R, R, R, R, R,
R, N, N, N, N, N, N, N,
R, N, AM, AM, AM, AM, AM, AM,
R, N, AM, V, V, V, V, V,
R, N, AM, V, A, A, A, A,
R, N, AM, V, A, AN, AN, AN,
R, N, AM, V, A, AN, VI, VI,                                                                   
R, N, AM, V, A, AN, VI, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sensor.humidity > 80 and sensor.temp > 20:
    sensor.set_pixels(arco_iris)
  elif sensor.humidity > 80 and sensor.temp < 0 :
    sensor.clear([255, 255, 255]) # Nieve: blanco
  elif sensor.humidity <= 80 and sensor.temp > 20 :
    sensor.clear([255, 255, 0]) # Sol: amarillo
  else:
    sensor.clear()
    
