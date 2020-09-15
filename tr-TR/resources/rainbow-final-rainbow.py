#!/bin/python3

sense_hat ithalat SenseHat
import time

sense = SenseHat()
sense.clear()

K = [255, 0, 0] # kırmızı
T = [255, 165, 0] # turuncu
S = [255, 255, 0] # sarı
Y = [0, 255, 0] # yeşil
MA = [0, 55, 155] # mavi
L = [25, 0, 255] # lacivert
MO = [255, 0, 255] # mor
X = [0, 0, 0] # kapalı


gokkusagi = [
K, K, K, K, K, K, K, K,
K, T, T, T, T, T, T, T,
K, T, S, S, S, S, S, S,
K, T, S, Y, Y, Y, Y, Y,
K, T, S, Y, MA, MA, MA, MA,
K, T, S, Y, MA, L, L, L,
K, T, S, Y, MA, L, MO, MO,                                                                   
K, T, S, Y, MA, L, MO, X
]

while True:
  t = time.localtime() 
  h = t.tm_hour

  if sense.humidity > 80 and sense.temp > 20:
    sense.set_pixels(gokkusagi)
  elif sense.humidity > 80 and sense.temp < 0 :
    sense.clear([255, 255, 255]) # kar beyazı
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # güneş sarısı
  else:
    sense.clear()
    
