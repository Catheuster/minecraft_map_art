from map_art import create_map_art
import eel

@eel.expose
def hello():
    print("hello world")

@eel.expose
def call_create_map(altura,largura,url,nome,dither):
    altura = int(altura)
    largura = int(largura)
    create_map_art(altura=altura,largura=largura,url=url,name=nome,dither=dither)
    eel.hideLoader()

eel.init("web")
eel.start("index.html")