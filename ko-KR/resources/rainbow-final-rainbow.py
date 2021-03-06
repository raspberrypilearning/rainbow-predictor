#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0]  # 빨강
O = [255, 165, 0]  # 주황
Y = [255, 255, 0] # 노랑
G = [0, 255, 0] # 녹색
B = [0, 55, 155] # 파랑
I = [25, 0, 255] # 남색
V = [255, 0, 255] # 보라색
X = [0, 0, 0]  # 끄기


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
    sense.clear([255, 255, 255]) # 흰눈
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # 노란 해
  else:
    sense.clear()
    
