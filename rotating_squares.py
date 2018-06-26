#length of one square#
SQUARE = 300
#format#
CANVAS = 600
NUMSQUARE = 1
NUMFRAMES = 150

#create Animation
for frame in range(NUMFRAMES):
    newPage(CANVAS, CANVAS)
    frameDuration(1/15)
    NUMSQUARE = frame + 1
    (print (frame))

    for square in range(NUMSQUARE):
        fill(1)
        stroke(0)
        rect((CANVAS/2)-(SQUARE/2),(CANVAS/2)-(SQUARE/2),SQUARE,SQUARE)
        rotate((2), center=(CANVAS/2,CANVAS/2))
        save()


saveImage("Test.gif")
