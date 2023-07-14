from PIL import Image
import numpy as np

#Extract RGB of some pixels in image 
def skin_extractor(input):
    skin_palette = []
    img = Image.open(input)
    pix = np.array(img)
    for i in range(0, img.size[0], 10):
        skin_palette.append(pix[20][i].tolist())
    return skin_palette

#Concatenate all results of images and write output file
def skin_extractor_con(input1, input2, input3, output):
    skin_palette_1 = skin_extractor(input1)
    skin_palette_2 = skin_extractor(input2)
    skin_palette_3 = skin_extractor(input3)
    skin_palette = skin_palette_1 + skin_palette_2 + skin_palette_3

    #Remove duplications
    temp = []
    for c in skin_palette:
        if c not in temp:
            temp.append(c)
    skin_palette = temp

    #Remove last element(255)
    for i in range(len(skin_palette)):
        del skin_palette[i][3]

    #Remove white colors
    temp = []
    for i in range(len(skin_palette)):
        if skin_palette[i][0]>=240 and skin_palette[i][1]>=240 and skin_palette[i][2]>=240:
            temp.append(skin_palette[i])
    skin_palette = [i for i in skin_palette if i not in temp]

    #Write txt file
    sep = ','
    temp = ''
    with open(output, 'w') as f:
        for a in skin_palette:
            for b in a:
                temp = temp + str(b) + sep
            temp = temp.rstrip(sep)
            temp = temp + '\n'
        f.writelines(temp)    
    f.close()

#Extract RGB of some pixels in image 
def color_extractor(input):
    color_palette = []
    img = Image.open(input)
    pix = np.array(img)
    for i in range(0, img.size[0], 15):
        for j in range(0, img.size[1], 15):
            color_palette.append(pix[j][i].tolist())
    return color_palette

#Concatenate all results of images and write output file
def color_extractor_con(input1, input2, input3, output):
    color_palette_1 = color_extractor(input1)
    color_palette_2 = color_extractor(input2)
    color_palette_3 = color_extractor(input3)
    color_palette = color_palette_1 + color_palette_2 + color_palette_3

    #Remove duplications
    temp = []
    for c in color_palette:
        if c not in temp:
            temp.append(c)
    color_palette = temp

    #Remove last element(255)
    for i in range(len(color_palette)):
        del color_palette[i][3]

    #Remove white colors
    temp = []
    for i in range(len(color_palette)):
        if color_palette[i][0]>=250 and color_palette[i][1]>=250 and color_palette[i][2]>=250:
            temp.append(color_palette[i])
    color_palette = [i for i in color_palette if i not in temp]
    
    #Write txt file
    sep = ','
    temp = ''
    with open(output, 'w') as f:
        for a in color_palette:
            for b in a:
                temp = temp + str(b) + sep
            temp = temp.rstrip(sep)
            temp = temp + '\n'
        f.writelines(temp)    
    f.close()

skin_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_skin_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_skin_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_skin_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_skin.txt")

color_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_color_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_color_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_color_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_color.txt")

skin_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_skin_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_skin_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_skin_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_skin.txt")

color_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_color_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_color_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_color_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_color.txt")

skin_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_skin_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_skin_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_skin_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_skin.txt")

color_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_color_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_color_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_color_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_color.txt")

skin_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_skin_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_skin_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_skin_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_skin.txt")

color_extractor_con("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_color_1.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_color_2.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_color_3.png",
                   "C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_color.txt")