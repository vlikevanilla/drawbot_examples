from random import randint
import random
CANVAS = 500
SIZE = 30
NUMSHAPES = 100
NUMFRAMES = 18


for frame in range(NUMFRAMES):
    newPage(CANVAS,CANVAS)
    rect(0,0,CANVAS,CANVAS)
    rotate(-(20*frame), center = (CANVAS/2 , CANVAS/2)) 
    

    for i in range(NUMSHAPES):
        """uncomment for random colors for every frame"""
        #r = random.uniform(0,0.2)
        #g = random.uniform(0,0.8)
        #b = random.uniform(0,1)
        #fill (r,g,b,(i/80) )
        fill (i/90,i/90,i/90)
        oval((CANVAS/2)+(i+60) , (CANVAS/2) - (SIZE/2) ,SIZE+i/3, SIZE+i/3)
        #translate((i+10), 0)
        rotate(18, center= (CANVAS/2 , CANVAS/2))
        
        
saveImage("spiraltest.gif")
         
       
    
