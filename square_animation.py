#length of one square#
SQUARE = 300
#format#
CANVAS = 600
NUMSQUARE = 1
NUMFRAMES = 50
    
def create_square(myrange):
    for frame in myrange:
        newPage(CANVAS, CANVAS)
        frameDuration(1/15)
        NUMSQUARE = frame + 1
        print (frame)

        for square in range(NUMSQUARE):
            fill(1)
            stroke(0)
            rect((CANVAS/2)-(SQUARE/2),(CANVAS/2)-(SQUARE/2),SQUARE,SQUARE)
            rotate((2), center=(CANVAS/2,CANVAS/2))

forward_range = range(NUMFRAMES)
reverse_range = reversed(range(NUMFRAMES))
        
for rng in [forward_range, reverse_range]:
    create_square(rng)

saveImage("square.gif")
