#!/bin/python3

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

R = [255, 0, 0] # κόκκινο
O = [255, 165, 0] # πορτοκαλί
Y = [255, 255, 0] # κίτρινο
G = [0, 255, 0] # πράσινο
B = [0, 55, 155] # μπλε
I = [25, 0, 255] # λουλακί
V = [255, 0, 255] # βιολετί
R = [0, 0, 0] # σβηστό


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
    sense.clear([255, 255, 255]) # λευκό χιόνι
  elif sense.humidity <= 80 and sense.temp > 20 :
    sense.clear([255, 255, 0]) # κίτρινος ήλιος
  else:
    sense.clear()
    
