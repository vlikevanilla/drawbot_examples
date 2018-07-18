##############################
# Draw Wiggles using Drawbot #
##############################

"""
Script by Roberto Arista, you can find the related tutorial here: https://medium.com/@roberto_arista/how-to-draw-a-wiggle-between-two-points-with-python-and-drawbot-788006c18fb0
You can find drawbot here: http://www.drawbot.com/
Code distributed with no guarantee, use at your own risk
"""

### Modules
from math import radians, atan2, sqrt, sin, cos
from collections import namedtuple


### Constants
BLACK = (0, 0, 0)
Point = namedtuple('Point', ['x', 'y'])


### Function & procedures
def calcAngle(pt1, pt2):
    return atan2((pt2.y - pt1.y), (pt2.x - pt1.x))


def calcDistance(pt1, pt2):
    return sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)


def calcWiggle(pt1, pt2, waveLength, waveHeight, curveSquaring=.57, polarity=1):
    assert 0 <= curveSquaring <= 1, 'curveSquaring should be a value between 0 and 1: {}'.format(curveSquaring)
    assert waveLength > 0, 'waveLength smaller or equal to zero: {}'.format(waveLength)

    diagonal = calcDistance(pt1, pt2)
    angleRad = calcAngle(pt1, pt2)

    howManyWaves = diagonal//int(waveLength)
    waveInterval = diagonal/float(howManyWaves)
    maxBcpLength = sqrt((waveInterval/4.)**2+(waveHeight/2.)**2)
    bcpLength = maxBcpLength*curveSquaring
    bcpInclination = calcAngle(Point(0,0), Point(waveInterval/4., waveHeight/2.))

    wigglePoints = [pt1]
    prevFlexPt = pt1
    for waveIndex in range(0, int(howManyWaves*2)):
        bcpOutAngle = angleRad+bcpInclination*polarity
        bcpOut = Point(prevFlexPt.x+cos(bcpOutAngle)*bcpLength, prevFlexPt.y+sin(bcpOutAngle)*bcpLength)

        flexPt = Point(prevFlexPt.x+cos(angleRad)*waveInterval/2., prevFlexPt.y+sin(angleRad)*waveInterval/2.)

        bcpInAngle = angleRad+(radians(180)-bcpInclination)*polarity
        bcpIn = Point(flexPt.x+cos(bcpInAngle)*bcpLength, flexPt.y+sin(bcpInAngle)*bcpLength)

        wigglePoints.append((bcpOut, bcpIn, flexPt))

        polarity *= -1
        prevFlexPt = flexPt

    return wigglePoints


def drawCurvesSequence(wigglePoints):
    myBez = BezierPath()
    myBez.moveTo(wigglePoints[0])
    for eachBcpOut, eachBcpIn, eachAnchor in wigglePoints[1:]:
        myBez.curveTo(eachBcpOut, eachBcpIn, eachAnchor)
    myBez.endPath()
    drawPath(myBez)

def invertPoints(pt1, pt2):
    newPt1 = Point((canvasSize-pt2.x), pt2.y)
    newPt2 = Point((canvasSize-pt1.x), pt1.y)
    return newPt1, newPt2

def createXSlider():
    """made this double the length because I can't think of a better way now"""
    xSlider = []
    for i in range(int(nFrames/4)):
        xSlider.append(i)
    for i in reversed(range(int(nFrames/4))):
        xSlider.append(i)
    for i in range(int(nFrames/4)):
        xSlider.append(-i)
    for i in reversed(range(int(nFrames/4))):
        xSlider.append(-i)
    for i in range(int(nFrames/4)):
        xSlider.append(i)
    for i in reversed(range(int(nFrames/4))):
        xSlider.append(i)
    for i in range(int(nFrames/4)):
        xSlider.append(-i)
    for i in reversed(range(int(nFrames/4))):
        xSlider.append(-i)

    return xSlider


# variables
waveLength = 16
waveHeight = 75
curveSquaring = .5
polarity = 1

### Instructions
canvasSize = 400
nFrames = 100

# create the invidividual frame adjustments before we apply them to each frame
xSlider = createXSlider()

for frame in range(nFrames):
    newPage(canvasSize, canvasSize)
    frameDuration(1/20)
    fill(0)
    rect(0, 0, canvasSize, canvasSize)
    strokeWidth(2)
    stroke(1)
    fill(None)
    
    # adjustments
    waveHeight += xSlider[frame]/20
    curveSquaring += (xSlider[frame]/5000)
    if curveSquaring > 1:
        curveSquaring = 1
    elif curveSquaring < 0:
        curveSquaring = 0
    
    for i in range(50, 400, 50):
        ### Variables
        # XXX Need to play with the (i/10) to and adjust the speed
        pt1 = Point(50-xSlider[frame]+(i/10), i)
        pt2 = Point(150-xSlider[frame]+(i/10), i+10)

        wigglePoints = calcWiggle(pt1, pt2, waveLength, waveHeight, curveSquaring, polarity)
        drawCurvesSequence(wigglePoints)
        invertPt1, invertPt2 = invertPoints(pt1, pt2)
        wigglePoints_inverted = calcWiggle(invertPt1, invertPt2, waveLength, waveHeight, curveSquaring, -polarity)
        drawCurvesSequence(wigglePoints_inverted)

saveImage("~/tmp/drawbot/lines40.gif")
