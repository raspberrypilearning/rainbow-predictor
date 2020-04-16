## Dibuixant un arc de Sant Martí

Primer, dibuixa un arc de Sant Martí mitjançant la matriu de LEDS de la placa Sense HAT. Els colors són Vermell, Taronja, Groc, Verd, Blau, Indi i Violeta.

Per definir el color d’un LED individual, hem de dir quina quantitat de vermell, verd i blau ha de tenir de 0 a 255.

+ Obre el Trinket d'Inici del Predictor de l'Arc de Sant Martí: <a href="http://jumpto.cc/rainbow-go" target="_blank">jumpto.cc/rainbow-go</a>.
    
    **S'ha inclòs el codi per configurar la placa Sense HAT.**

+ Afegeix el codi ressaltat per configurar una variable pel color Vermell i, a continuació, converteix tots els píxels en vermell mitjançant `sense.clear(R)`:
    
    ![captura de pantalla](images/rainbow-red.png)
    
    Assegura't que utilitzes la lletra majúscula `R`.

+ El Taronja és el següent. El Taronja és una barreja de vermell amb verd. Pots ajustar els números fins a obtenir un taronja que t'agradi. Aquest cop, fes servir `sense.clear(O)` per provar el nou color, assegura't d’utilitzar la majúscula `O` en els parèntesis.
    
    ![captura de pantalla](images/rainbow-orange.png)

+ Ara afegeix les variables `Y`, `G`, `B`, `I`, `V` de manera que tinguis els set colors de l'arc de Sant Martí. Pots buscar colors RGB a <a href="http://jumpto.cc/colours" target="_blank">jumpto.cc/colours</a>
    
    Pots provar els teus colors mitjançant `sense.clear()`.
    
    ![captura de pantalla](images/rainbow-colours.png)

+ Afegeix una variable `X` per a desactivar els píxels (sense vermell, verd o blau):
    
    ![captura de pantalla](images/rainbow-off.png)

+ Ara toca dibuixar un arc de Sant Martí. Has de configurar una llista que contingui el color de cada píxel i, a continuació, crida a `set_pixels` amb la llista de colors. Per estalviar-te teclejar pots copiar l'arc de Sant Martí de `snippets.py` al teu projecte.
    
    ![captura de pantalla](images/rainbow-rainbow.png)