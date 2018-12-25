from PIL import Image
import PIL.ImageOps


def create_templates(list_of_images):
    # This loop creates the correct number of 'templates'
    list_templates = []
    for i in range(len(list_of_images)):
        if i % 8 == 0:
            t_blank = Image.new("RGB", (850*3, 1100*3), color=(255, 255, 255))
            list_templates.append(t_blank)


def create_collages(list_of_images, list_templates):
    # this loop does the inverting, resizing, and saving of the images.
    gap_w = 43 * 3
    gap_h = 40 * 3
    i_width = 350*3
    i_height = 218*3

    for i in list_of_images:
        index = list_of_images.index(i)
        indexDiv8 = index // 8
        indexM8Div2 = ((index % 8) // 2)
        newImage = Image.open(i)
        invImage = PIL.ImageOps.invert(newImage)
        invImage = invImage.resize((i_width, i_height))
        if (index % 2) == 0:
            template_image = list_templates[indexDiv8].paste(invImage, (
                gap_w, gap_h * (indexM8Div2+1) + (indexM8Div2*i_height)))
        if (index % 2) == 1:
            template_image = list_templates[indexDiv8].paste(invImage, (
                2 * gap_w + i_width, gap_h * (indexM8Div2+1) + (indexM8Div2*i_height)))
        if (((index + 1) % 8) == 0) and (index != 0):
            list_templates[indexDiv8].save("collage_" + str(indexDiv8 + 1) + ".png",
                                           dpi=(300, 300))
# this if statement is for if there is a non-multiple of 8 images in the folder
    length = len(list_of_images)
    if length % 8 != 0:
        list_templates[length // 8].save("collage_" + str(length // 8 + 1) + ".png",
                                         dpi=(300, 300))
