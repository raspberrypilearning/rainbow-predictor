#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat ()
sense.clear()

C = [255, 0, 0] # czerwony
P = [255, 165, 0] # pomarańczowy
Z = [255, 255, 0] # żółty
G = [0, 255, 0] # "Z" jest zajęte więc użyjmy "G"(ang. Green - zielony)
N = [0, 55, 155] # niebieski
I = [25, 0, 255] # indygo
F = [255, 0, 255] # fioletowy
X = [0, 0, 0] # wyłączony


tecza = [
C, C, C, C, C, C, C, C,
C, P, P, P, P, P, P, P,
C, P, Z, Z, Z, Z, Z, Z,
C, P, Z, G, G, G, G, G,
C, P, Z, G, N, N, N, N,
C, P, Z, G, N, I, I, I,
C, P, Z, G, N, I, F, F,                                                                   
C, P, Z, G, N, I, F, X
]

while True:
  c = time.localtime () 
  g = c.tm_hour

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(tecza)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear ([255, 255, 255]) # śnieg
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear ([255, 255, 0]) # słońce
  else:
    sense.clear()
    
