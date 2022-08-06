from mc_colors import McColors
from PIL import Image
from math import ceil
import requests
import numpy as np
import eel

def create_map_art(altura,largura,url,name,dither):
    map_size = (largura*128,altura*128)
    im = Image.open(requests.get(url, stream=True).raw)
    im.save("original.png")

    new_img = prepare_image(map_size,dither, im)
    new_img.save(name+".png")

    width, height = new_img.size
    altura = ceil(height/128)
    largura = ceil(width/128)


    processed_pixels = 0
    pixel_number = width*height
    eel.setPercentageHidden(False)

    for linha_mapa in range(altura):
        for coluna_mapa in range(largura):
            numero_mapa = largura * linha_mapa + coluna_mapa
            map_name = name + '_' + str(numero_mapa)

            range_x,range_y = 128,128
            if(coluna_mapa == largura-1 and width%128 != 0):
                range_x = width%128            
            if(linha_mapa == altura-1 and height%128 != 0):
                range_y = height%128

            cropped_image = new_img.crop((coluna_mapa*128, linha_mapa*128, coluna_mapa*128+range_x, linha_mapa*128+range_y))
            cropped_image.save(map_name+ ".png")
            block_pixels, processed_pixels = get_block_pixels(cropped_image, range_x, range_y, processed_pixels, pixel_number)

            write_mcfunction(block_pixels, map_name)

    eel.setPercentageHidden(True)


def prepare_image(map_size,dither,im):
    mc_colors = McColors()
    width, height = im.size
    if map_size[1]*im.size[0] > map_size[0]*im.size[1]:
        rate = im.size[0]/map_size[0]
        val = int(height/rate)
        new_img = im.resize((map_size[0],val))
    else:
        rate = im.size[1]/map_size[1]
        val = int(width/rate)
        new_img = im.resize((val,map_size[1]))

    new_img = mc_colors.image_in_palette(new_img, dither)
    return new_img


def get_block_pixels(cropped_image,range_x,range_y, processed_pixels, pixel_number):
    mc_colors = McColors()
    block_pixels = []
    for i in range(range_y):
        linha = []
        for j in range(range_x):
            bloco = mc_colors.colors[cropped_image.getpixel((j,i))]
            linha.append(bloco)
            processed_pixels = processed_pixels+1
            percentage = processed_pixels/pixel_number * 100
            eel.setPercentageValue("{:.2f}%".format(percentage))
            
        block_pixels.append(linha)

    block_pixels = np.transpose(block_pixels)
    return block_pixels ,processed_pixels

def write_mcfunction(block_pixels, map_name):
    datapack_function = ""
    datapack_file = open(map_name+".mcfunction", "w")
    for i in range(len(block_pixels)):
        y = 128

        for j in range(len(block_pixels[0])):
            x = i
            z = j

            if z == 0:
                y = 128 - block_pixels[i][j]['heigh']
                command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(x,y,z-1,x,y,z-1,'grass_block')
                datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)

            y = y + block_pixels[i][j]['heigh']

            block = block_pixels[i][j]['block']
            command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(x,y,z,x,y,z,block)
            datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)
    
    datapack_file.write(datapack_function)
