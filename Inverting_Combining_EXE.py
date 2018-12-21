from PIL import Image
import PIL.ImageOps

listOfImages = []
errorLimit = 20


# This loop creates a list of all of the images in the folder
for i in range(100):
    try:
        fp = open("scope_" + str(i) + ".png", 'r')
        listOfImages.append("scope_" + str(i) + ".png")
        errorLimit = 20
    except FileNotFoundError:
        if errorLimit <= 0:
            # print(listOfImages)
            break
        else:
            errorLimit -= 1
            continue


# This loop creates the correct number of 'templates'
listOfTemplates = []
for i in range(len(listOfImages)):
    if i % 8 == 0:
        templateBlank = Image.new("RGB", (850*3, 1100*3), color=(255, 255, 255))
        listOfTemplates.append(templateBlank)


# this loop does the inverting, resizing, and saving of the images.
gapW = 43 * 3
gapH = 40 * 3
iWidth = 350*3
iHeight = 218*3

for i in listOfImages:
    index = listOfImages.index(i)
    indexDiv8 = index // 8
    indexM8Div2 = ((index % 8) // 2)
    newImage = Image.open(i)
    invImage = PIL.ImageOps.invert(newImage)
    invImage = invImage.resize((iWidth, iHeight))
    if (index % 2) == 0:
        templateImage = listOfTemplates[indexDiv8].paste(invImage, (
            gapW, gapH * (indexM8Div2+1) + (indexM8Div2*iHeight)))
        print(gapH + (((index % 8) // 2) * iHeight))
    if (index % 2) == 1:
        templateImage = listOfTemplates[indexDiv8].paste(invImage, (
            2 * gapW + iWidth, gapH * (indexM8Div2+1) + (indexM8Div2*iHeight)))
    if ((index % 8) == 0) and (index != 0):
        listOfTemplates[indexDiv8].save("collage_" + str(indexDiv8+1) + ".png",
                                        dpi=(300, 300))

# this if statement is for if there is a non-multiple of 8 images in the folder
if len(listOfImages) % 8 != 0:
    listOfTemplates[len(listOfImages) // 8].save("collage_" + str(1) + ".png",
                                                 dpi=(300, 300))
