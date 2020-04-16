#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0] # rosso
A = [255, 165, 0] # arancione
G = [255, 255, 0] # giallo
V = [0, 255, 0] # verde
B = [0, 55, 155] # blu
I = [25, 0, 255] # indaco
W = [255, 0, 255] # viola
X = [0, 0, 0] # spento


arcobaleno = [
R, R, R, R, R, R, R, R,
R, A, A, A, A, A, A, A,
R, A, G, G, G, G, G, G,
R, A, G, V, V, V, V, V,
R, A, G, V, B, B, B, B,
R, A, G, V, B, I, I, I,
R, A, G, V, B, I, W, W,                                                                   
R, A, G, V, B, I, W, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(arcobaleno)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear([255, 255, 255]) # neve bianca
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # sole giallo
  else:
    sense.clear()
    
