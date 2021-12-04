import base64
# import numpy as np
# from PIL import Image

file = open("/home/razerz/Documents/i3/textTv/data.txt", "r")
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

gif = open("/home/razerz/Documents/i3/textTv/100.png", "wb")
gif.write(decoded)
gif.close()

# im = Image.open("100.png")
# im = im.convert("RGBA")

# data = np.array(im)

# red,green,blue,alpha = data.T

# blue_areas = (red==0) & (blue==255) & (green==0)
# white_areas = (red == 255) & (blue == 255) & (green == 255)
# data[..., :-1][blue_areas.T] = (0,0,0)
# data[..., :-1][white_areas] = (255,0,255)

# resultedImage = Image.fromarray(data)
# resultedImage.show()
