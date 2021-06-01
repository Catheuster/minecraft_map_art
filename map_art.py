from mc_colors import McColors
from PIL import Image
import requests

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
    new_img.save(name+".png")
    pixels = list(new_img.getdata())

    for i in range(len(pixels)):
        pixels[i] = mc_colors.cor_mais_proxima(pixels[i])
    
    datapack_function = ""
    datapack_file = open(name+".mcfunction", "w")

    for i in range(width):
        y = 128
        for j in range(height):
            y = y + pixels[width*i+j]['heigh']
            block = pixels[width*j+i]['block']
            command = "fill ~{} {} ~{} ~{} {} ~{} {}".format(i,y,j,i,y,j,block)
            datapack_function = datapack_function + "execute as @p at @p run {}\n".format(command)
    
    datapack_file.write(datapack_function)
