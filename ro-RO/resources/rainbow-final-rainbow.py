#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0]  # roșu
O = [255, 165, 0]  # oranj
G = [255, 255, 0] # galben
V = [0, 255, 0] # verde
A = [0, 55, 155] # albastru
I = [25, 0, 255] # indigo
M = [255, 0, 255] # mov
X = [0, 0, 0] # oprit


curcubeu = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, G, G, G, G, G, G,
R, O, G, V, V, V, V, V,
R, O, G, V, A, A, A, A,
R, O, G, V, A, I, I, I,
R, O, G, V, A, I, M, M,                                                                   
R, O, G, V, A, I, M, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(rainbow)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear([255, 255, 255]) # zăpadă albă
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # yellow sun
  else:
    sense.clear()
    
