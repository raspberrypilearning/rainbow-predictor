#!/bin/python3

from sense_hat import SenseHat
import time

()sense = SenseHat
()sense.clear

R = [255، 0، 0] # أحمر
O = [255، 165، 0] # برتقالي
Y = [255 ، 255 ، 0] # أصفر
G = [0 ، 255 ، 0] # أخضر
B = [0 ، 55 ، 155] # أزرق
I = [25، 0، 255] # نيلي
V = [255 ، 0 ، 255] # بنفسجي
X= [0، 0، 0] # مطفئ


]=rainbow
,R, R, R, R, R, R, R, R
,R, O, O, O, O, O, O, O
,R, O, Y, Y, Y, Y, Y, Y
,R, O, Y, G, G, G, G, G
,R, O, Y, G, B, B, B, B
,R, O, Y, G, B, I, I, I
,R, O, Y, G, B, I, V, V                                                                   
R, O, Y, G, B, I, V, X
[

while True:
  ()t = time.localtime 
  h = t.tm_hour

  :if sense.humidity > 80 and sense.temp > 20
    sense.set_pixels(rainbow)
  :elif sense.humidity > 80 and sense.temp < 0 
    sense.clear([255, 255, 255]) # أبيض ثلجي
  :elif sense.humidity <= 80 and sense.temp > 20 
    sense.clear([255, 255, 0]) # أصفر مثل لون الشمس
  else:
    ()sense.clear
    
