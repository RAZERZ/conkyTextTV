import base64
# import numpy as np
# from PIL import Image

file = open("~/Documents/i3/conkyTextTV/data.txt", "r")
data = file.read()
file.close()

result = data.find("Content_pageImage")

start = 0
stop = 0
aposIndex = 0
i = 1
while (aposIndex != 3):
    i+=1
    if(data[result+i] == '"'):
        aposIndex += 1
        if(aposIndex == 2):
            start = result+i+1
        elif(aposIndex == 3):
            stop = result+i

base64msg = data[start+22:stop]
decoded = base64.b64decode(base64msg)

gif = open("~/Documents/i3/conkyTextTV/100.png", "wb")
gif.write(decoded)
gif.close()
