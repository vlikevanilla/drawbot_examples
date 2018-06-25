CANVAS = 500
SQUARESIZE = 158
NUMSQUARES = 99
SQUAREDIST = 3

width = NUMSQUARES * SQUAREDIST

NUMFRAMES = 50

for frame in range(NUMFRAMES):
    newPage(CANVAS, CANVAS)
    frameDuration(1/25)
    
    phase = 2 * pi * frame / NUMFRAMES
    startAngle = 90 * sin(phase)
    endAngle = 90 * sin(phase + 0.5 * pi)
    print (sin(phase))

    translate(CANVAS/2 - width/2 , CANVAS/2)

    fill(1)
    stroke(0)





    for i in range(NUMSQUARES):
    
        f = i / NUMSQUARES
    
        save()
        translate(i*SQUAREDIST)
        scale(0.9, 1)
        rotate(startAngle + f * (endAngle - startAngle))

        rect(-SQUARESIZE/2, -SQUARESIZE/2, SQUARESIZE, SQUARESIZE)

        restore()
        
saveImage("Animation2.gif")
