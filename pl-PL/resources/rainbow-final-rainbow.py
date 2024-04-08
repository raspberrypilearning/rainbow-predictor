#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat ()
sense.clear()

R = [255, 0, 0] # czerwony
O = [255, 165, 0] # pomarańczowy
Y = [255, 255, 0] # żółty
G = [0, 255, 0] # "Z" jest zajęte więc użyjmy "G"(ang.
B = [0, 55, 155] # niebieski
I = [25, 0, 255] # indygo
V = [255, 0, 255] # fioletowy
X = [0, 0, 0] # wyłączony


tecza = [
C, P, P, P, P, P, P, P,
C, P, Z, Z, Z, Z, Z, Z,
R, O, Y, Y, Y, Y, Y, Y,
R, O, Y, G, G, G, G, G,
R, O, Y, G, B, B, B, B,
R, O, Y, G, B, I, I, I,
R, O, Y, G, B, I, V, V,                                                                   
C, P, Z, G, N, I, F, X
]

while True:
  c = time.localtime () 
  g = t.tm_hour

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(tecza)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear ([255, 255, 255]) # śnieg
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear ([255, 255, 0]) # słońce
  else:
    sense.clear()
    
