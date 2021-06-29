from mc_colors import McColors
from PIL import Image
import requests
import numpy as np
import eel

def create_map_art(altura,largura,url,name,dither):
    map_size = (largura*128,altura*128)
    im = Image.open(requests.get(url, stream=True).raw)
    im.save("original.png")
    width, height = im.size
    mc_colors = McColors()
    if altura*im.size[0] > largura*im.size[1]:
        rate = im.size[0]/map_size[0]
        val = int(height/rate)
        new_img = im.resize((map_size[0],val))
    else:
        rate = im.size[1]/map_size[1]
        val = int(width/rate)
        new_img = im.resize((val,map_size[1]))
    width, height = new_img.size

    block_pixels = []
    pixel_number = width*height
    processed_pixels = 0

    new_img = mc_colors.image_in_palette(new_img, dither)
    new_img.save(name+".png")
    eel.setPercentageHidden(False)
    for i in range(height):
        linha = []
        for j in range(width):
            bloco = mc_colors.colors[new_img.getpixel((j,i))]
            linha.append(bloco)
            processed_pixels = processed_pixels+1
            percentage = processed_pixels/pixel_number * 100
            eel.setPercentageValue("{:.2f}%".format(percentage))
            
        block_pixels.append(linha)
    
    datapack_function = ""
    datapack_file = open(name+".mcfunction", "w")

    block_pixels = np.transpose(block_pixels)

    for i in range(len(block_pixels)):
        y = 128

        for j in range(len(block_pixels[0])):
            x = int(j/128)*largura*128 + i
            z = j%128
                
            if z == 0:
                y = 128 - block_pixels[i][j]['heigh']
                command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(x,y,z-1,x,y,z-1,'grass_block')
                datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)

            y = y + block_pixels[i][j]['heigh']

            block = block_pixels[i][j]['block']
            command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(x,y,z,x,y,z,block)
            datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)
    
    eel.setPercentageHidden(True)
    datapack_file.write(datapack_function)
