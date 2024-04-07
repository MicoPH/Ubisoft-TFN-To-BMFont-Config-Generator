import json, pathlib
from tkinter import filedialog
from tkinter import *

print('''   Welcome to Ubisoft FNT To BMFC Generator v0.1.0
     Please select The Cooked Font...''')
print("\n   Run Tkinter:\n")
openwindow=Tk()
openwindow.title('')
streamfontfile = filedialog.askopenfilename(initialdir=pathlib.Path,title="Browse the cooked fonts", filetypes=(("UbiArt Font",'.tfn.ckd'),('allfiles','*.*')))
openwindow.destroy()
selectidchar = 0
lastchar = 1
jsonload1 = json.load(open(streamfontfile,'r'))
bfmcwriter = open('open.bmfc','w')
bfmcwriter.write('''# AngelCode Bitmap Font Generator configuration file
fileVersion=1

# font settings
fontName=Noto Sans CJK Bold
fontFile=New folder/Font/JustDance-Bold.otf
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
addchar = 0
selectidchar = jsonload1["chars"][0]["id"]
log=""
print("Generating Fonts...")
for id in jsonload1["chars"]:
    selectidchar+=1
    mainchar = id["id"]
    if id["id"] == selectidchar:
        if addchar == 0:
            domainchar = id["id"]
        addchar+=1
        log = log+'1 addchar:'+ str(addchar)+' mainchar: '+ str(mainchar)+' lastchar '+ str(lastchar)+' selected char: '+ str(selectidchar)+'\n'
    else:
        selectidchar = id["id"]
        if addchar == 0:
            if selectidchar == id["id"]:
                domainchar = id["id"]
            bfmcwriter.write(str(id["id"])+",")
            addchar = 0
            log = log+'2 addchar:'+ str(addchar)+' mainchar: '+ str(mainchar)+' lastchar '+ str(lastchar)+' selected char: '+ str(selectidchar)+'\n'
        else:
            bfmcwriter.write(str(domainchar)+"-"+str(mainchar)+',')
            addchar = 0
            log = log+'3 addchar:'+ str(addchar)+' mainchar: '+ str(mainchar)+' lastchar '+ str(lastchar)+' selected char: '+ str(selectidchar)+'\n'
    lastchar+=1
logs=open('logs.txt','w')
logs.write(log)
bfmcwriter.write('''

# imported icon images''')
print('\n   Done!\n')
input('Press enter to exit')
    