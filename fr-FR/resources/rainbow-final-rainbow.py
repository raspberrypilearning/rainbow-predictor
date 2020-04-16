#!/bin/python3

from sense_hat import SenseHat
import time

capteur = SenseHat()
capteur.clear()

R = [255, 0, 0]  # rouge
O = [255, 165, 0]  # orange
J = [255, 255, 0] # jaune
V = [0, 255, 0] # vert
B = [0, 55, 155] # bleu
I = [25, 0, 255] # indigo
M = [255, 0, 255] # mauve
X = [0, 0, 0]  # éteint


arcenciel = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, J, J, J, J, J, J,
R, O, J, V, V, V, V, V,
R, O, J, V, B, B, B, B,
R, O, J, V, B, I, I, I,
R, O, J, V, B, I, M, M,                                                                   
R, O, J, V, B, I, M, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if capteur.humidity > 80 and capteur.temp > 20:
    capteur.set_pixels(arcenciel)
  elif capteur.humidity > 80 and capteur.temp < 0 :
    capteur.clear([255, 255, 255]) # neige blanc
  elif capteur.humidity <= 80 and capteur.temp > 20 :
    capteur.clear([255, 255, 0]) # soleil jaune
  else:
    capteur.clear()
    
