## Desenhando um arco-íris

Primeiro, vamos desenhar um arco-íris usando a Matriz de LEDs no Sense HAT. As cores são Vermelho (red = R), Laranja (orange = O), Amarelo (yellow = Y), Verde (green = G), Azul (blue = B), Índigo (indigo = I) e Violeta (violet = V).

Para definir a cor de um LED individual, precisamos dizer quanto vermelho, verde e azul ele deve ter de 0 a 255.

+ Abra o Trinket 'Previsor de Arco-íris' versão inicial: <a href="http://jumpto.cc/rainbow-go" target="_blank">jumpto.cc/rainbow-go</a>.
    
    **O código para configurar o Sense HAT foi incluído para você.**

+ Adicione o código destacado para configurar uma variável para a cor Vermelho e depois torne todos os pixels vermelhos usando `sensor.clear(R)` (R = red = vermelho):
    
    ![screenshot](images/rainbow-red.png)
    
    Certifique-se de usar a letra maiúscula `R`.

+ A cor Laranja é a próxima. Laranja é vermelho misturado com verde. You can adjust the numbers until you get an orange that you like. Use `sense.clear(O)` this time to test the new colour, making sure to use a capital letter `O` in the brackets.
    
    ![screenshot](images/rainbow-orange.png)

+ Now add variables `Y`, `G`, `B`, `I`, `V` so that you have the seven colours of the rainbow. You can look up RGB colours at <a href="http://jumpto.cc/colours" target="_blank">jumpto.cc/colours</a>
    
    You can test your colours using `sense.clear()`.
    
    ![screenshot](images/rainbow-colours.png)

+ Add a variable `X` for setting pixels to off (no red, green or blue):
    
    ![screenshot](images/rainbow-off.png)

+ Now it's time to draw a rainbow. You need to set up a list containing the colour of each pixel and then call `set_pixels` with the list of colours. To save typing you can copy the rainbow from `snippets.py` in your project.
    
    ![screenshot](images/rainbow-rainbow.png)