from mc_colors import McColors
from PIL import Image
import requests
import numpy as np

def create_map_art(altura,largura,url,name,slice):
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
        rate = im.size[1]/map_size[0]
        val = int(width/rate)
        new_img = im.resize((val,map_size[1]))
    width, height = new_img.size
    pixels = np.asarray(new_img)

    new_pixels = []
    block_pixels = []
    pixel_number = width*height
    processed_pixels = 0
    for i in range(width):
        linha = []
        linha_new_pixels = []
        for j in range(height):
            bloco = mc_colors.cor_mais_proxima(pixels[i][j])
            linha.append(bloco)
            linha_new_pixels.append(bloco['rgb'])
            processed_pixels = processed_pixels+1
            print('progresso = {}/{}'.format(processed_pixels,pixel_number))

        new_pixels.append(linha_new_pixels)
        block_pixels.append(linha)
    
    array = np.array(new_pixels)
    new_img = Image.fromarray(array.astype(np.uint8))
    new_img.save(name+".png")
    
    datapack_function = ""
    datapack_file = open(name+".mcfunction", "w")

    block_pixels = np.transpose(block_pixels)

    for i in range(len(block_pixels)):
        y = 128
        for j in range(len(block_pixels)):
            x = int(j/128)*largura*128 + i
            z = j%128
            
            if z != 0:
                y = y + block_pixels[i][j]['heigh']
            else:
                y = 128

            block = block_pixels[i][j]['block']
            command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(x,y,z,x,y,z,block)
            datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)
    
    datapack_file.write(datapack_function)
