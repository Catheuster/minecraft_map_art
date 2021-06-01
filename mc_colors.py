class McColors():
    def __init__(self):
        self.colors = []
        self.blocks = [
            ('grass_block',(127, 178, 56)),
            ('sandstone', (247,233,163)),
            ('cobweb',(199,199,199)),
            ('redstone_block',(255,0,0)),
            ('ice',(160,160,255)),
            ('iron_block',(167,167,167)),
            ('melon',(0,124,0)),
            ('snow_block',(255,255,255)),
            ('clay',(164,168,184)),
            ('jukebox',(151,109,77)),
            ('stone',(122,122,122)),
            ('oak_planks',(143,119,72)),
            ('quartz_block',(255,252,245)),
            ('acacia_planks',(216,127,51)),
            ('magenta_wool',(178,76,216)),
            ('light_blue_wool',(102,153,216)),
            ('sponge',(229,229,51)),
            ('lime_wool',(127,204,25)),
            ('pink_wool',(242,127,165)),
            ('gray_wool',(76,76,76)),
            ('light_gray_wool',(153,153,153)),
            ('cyan_wool',(76,127,153)),
            ('purple_wool',(127,63,178)),
            ('blue_wool',(51,76,178)),
            ('dark_oak_planks',(102,76,51)),
            ('green_wool',(102,127,51)),
            ('red_wool',(153,51,51)),
            ('black_wool',(25,25,25)),
            ('gold_block',(250,238,77)),
            ('diamond_block',(92,219,213)),
            ('lapis_block',(74,128,255)),
            ('emerald_block',(0,217,58)),
            ('spruce_planks',(129,86,49)),
            ('netherrack',(122,2,0)),
            ('white_terracotta',(209,177,161)),
            ('orange_terracotta',(159,82,36)),
            ('magenta_terracotta',(149,87,108)),
            ('light_blue_terracotta',(112,108,138)),
            ('yellow_terracotta',(186,133,36)),
            ('lime_terracotta',(103,117,53)),
            ('pink_terracotta',(160,77,78)),
            ('gray_terracotta',(57,41,35)),
            ('light_gray_terracotta',(135,107,98)),
            ('cyan_terracotta',(87,92,92)),
            ('purple_terracotta',(122,73,88)),
            ('blue_terracotta',(76,62,92)),
            ('brown_terracotta',(76,50,35)),
            ('green_terracotta',(76,82,42)),
            ('red_terracotta',(142,60,46)),
            ('black_terracotta',(37,22,16)),
            ('crimson_nylium',(189,48,49)),
            ('crimson_stem',(148,63,97)),
            ('crimson_hyphae',(92,25,29)),
            ('warped_nylium',(22,126,134)),
            ('warped_stem',(58,142,140)),
            ('warped_hyphae',(86,44,62)),
            ('warped_wart_block',(20,180,133))
        ]

        for block in self.blocks:
            bright_rgb = block[1]
            dark_rgb = (int(bright_rgb[0]*180/255),int(bright_rgb[1]*180/255),int(bright_rgb[2]*180/255))
            neutral_rgb = (int(bright_rgb[0]*220/255),int(bright_rgb[1]*220/255),int(bright_rgb[2]*220/255))
            color = {
                'block': block[0],
                'rgb': dark_rgb,
                'heigh': -1
            }
            self.colors.append(color)
            color = {
                'block': block[0],
                'rgb': neutral_rgb,
                'heigh': 0
            }
            self.colors.append(color)
            color = {
                'block': 'minecraft:'+block[0],
                'rgb': bright_rgb,
                'heigh': 1
            }
            self.colors.append(color)
    
    @staticmethod
    def dist(cor1, cor2):
        r_linha = cor1[0] - cor2[0]
        r = cor1[0] - cor2[0]
        g = cor1[1] - cor2[1]
        b = cor1[2] - cor2[2]
        return ((2 + r_linha/256) * r**2) +( 4 * g**2) + ((2 + (255-r_linha)/256) * b**2)


    def cor_mais_proxima(self, cor):
        menor_distancia = -1
        cor_mais_proxima = None
        for color in self.colors:
            distancia = McColors.dist(cor,color['rgb'])
            if cor_mais_proxima is None:
                cor_mais_proxima = color
                menor_distancia = distancia
                continue
            
            if distancia < menor_distancia:
                menor_distancia = distancia
                cor_mais_proxima = color

        return cor_mais_proxima
