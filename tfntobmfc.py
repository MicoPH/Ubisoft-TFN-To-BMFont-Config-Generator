import json,pathlib
from tkinter import filedialog
from tkinter import *

print('''   Welcome to Ubisoft FNT To BMFC Generator v0.1.0
     Please select The Cooked Font...''')
print("\n   Run Tkinter:\n")
openwindow=Tk()
openwindow.title('')
streamfontfile = filedialog.askopenfilename(initialdir=pathlib.Path,title="Browse the cooked fonts", filetypes=(("UbiArt Font",'.tfn.ckd'),('allfiles','*.*')))
openwindow.destroy()
jsonload1 = json.load(open(streamfontfile,'r'))
bfmcwriter = open('bmfont.bmfc','w')
bfmcwriter.write('''# AngelCode Bitmap Font Generator configuration file
fileVersion=1

# font settings
fontName=
fontFile=
charSet=0
fontSize=250
aa=1
scaleH=100
useSmoothing=1
isBold=0
isItalic=0
useUnicode=1
disableBoxChars=1
outputInvalidCharGlyph=0
dontIncludeKerningPairs=0
useHinting=1
renderFromOutline=0
useClearType=1
autoFitNumPages=0
autoFitFontSizeMin=0
autoFitFontSizeMax=0

# character alignment
paddingDown=6
paddingUp=6
paddingRight=6
paddingLeft=6
spacingHoriz=2
spacingVert=2
useFixedHeight=0
forceZero=0
widthPaddingFactor=0.00

# output file
outWidth=4096
outHeight=2048
outBitDepth=32
fontDescFormat=1
fourChnlPacked=0
textureFormat=dds
textureCompression=3
alphaChnl=1
redChnl=4
greenChnl=4
blueChnl=4
invA=0
invR=0
invG=0
invB=0

# outline
outlineThickness=0

# selected chars
chars=''')
addchar = 0 # overall character
selectidchar = jsonload1["chars"][0]["id"]
log=""
nextcharac = 0
ckecker = 0
for id2 in jsonload1["chars"]:
    ckecker+=1
print("Loading Id's")
logs=open('logs.txt','w')
countchars=0
print("Writing...")
for id in jsonload1["chars"]:
    nextcharac+=1 # integer next value
    maincharacter=id["id"] # main character value
    if ckecker == nextcharac:
        if countchars==13:
            bfmcwriter.write('\nchars=')
            bfmcwriter.write(str(maincharacter)) # if last list chars and end of value
            logs.write("chars added")
            countchars=0
        else:
            bfmcwriter.write(str(maincharacter)) # if end of value
        logs.write(str(maincharacter)+": End Value\n")
    else:
        nextcharacter=jsonload1["chars"][nextcharac]["id"] # next charcter value
        if addchar == 0:
            if int(maincharacter+1) == nextcharacter:
                if countchars==13:
                    bfmcwriter.write('\nchars=')
                    bfmcwriter.write(str(maincharacter)+"-") # if last list chars and new increase of value
                    logs.write("\nChars list added\n")
                    countchars=0
                else:
                    bfmcwriter.write(str(maincharacter)+"-") # if new increase in next value
                addchar+=1
                logs.write(str(maincharacter)+": New Increase Value\n")
            else:
                if countchars==13:
                    bfmcwriter.write('\nchars=')
                    bfmcwriter.write(str(maincharacter)+",") # if end of value
                    logs.write("\nChars list added\n")
                    countchars=0
                else:
                    if countchars==12:
                        bfmcwriter.write(str(maincharacter)) # if last list chars and not same number in next value
                    else:
                        bfmcwriter.write(str(maincharacter)+",") # if not same number in next value
                addchar=0
                logs.write(str(maincharacter)+": New Value\n")
                countchars+=1
        else:
            if int(maincharacter+1) == nextcharacter: 
                addchar+=1 # if same value again
                logs.write(str(maincharacter)+": Next Value\n")
            else:
                if countchars==12:
                    bfmcwriter.write(str(maincharacter)) # if last list chars and last overall value
                else:
                    bfmcwriter.write(str(maincharacter)+",") # if last overall value
                countchars+=1
                addchar=0
                logs.write(str(maincharacter)+": Last Value\n")
    logs.write('\nIds :'+str(maincharacter)+"\n ")
bfmcwriter.write('''

# imported icon images''')
print('\n   Done!\n')
input('Press enter to exit')


    