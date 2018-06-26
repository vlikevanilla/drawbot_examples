#find which variable fonts are installed
for fontName in installedFonts():
    variations = listFontVariations(fontName)
    if variations: 
        print(fontName)
        for axis_name, dimensions in variations.items():
            print (axis_name, dimensions)
        print ()
        
#set variables for min and max weight     
MINSIZE = listFontVariations('.SFNSDisplay')['wght']['minValue']
MAXSIZE = listFontVariations('.SFNSDisplay')['wght']['maxValue']

#number of frames
NUMFRAMES = 60
#text 
PRINTTEXT = 'Banananananana Batman'

STEPSIZE = (MAXSIZE - MINSIZE) / (NUMFRAMES-1)

for frame in range(NUMFRAMES):
    
    newPage(1400, 200)
    frameDuration(1/20)
    font(".SFNSDisplay")
    fontSize(120)
    #calculate sin curve from 0 to 1 to 0 to loop gif
    curr_value = sin(2 * pi * frame/NUMFRAMES)
    print (curr_value)
    fontVariations(wght= curr_value )
    text(PRINTTEXT, (70, 70))
    
    fontSize(20)
    fontVariations(wght= 1)
    saveImage("VariableFont2.gif")
    
    
    
