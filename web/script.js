function callPython(){
    eel.hello()
}

function callPythonMakeArt(){
    var loader = document.getElementById("loader")
    loader.hidden = false
    var text = document.getElementById("url").value
    var a = document.getElementById("altura").value
    var l = document.getElementById("largura").value
    var nome = document.getElementById("nome").value
    var dither = document.getElementById("dithering").checked

    eel.call_create_map(a,l,text,nome,dither)
}

eel.expose(hideLoader)
function hideLoader(){
    var loader = document.getElementById("loader")
    loader.hidden = true
}

eel.expose(setPercentageHidden)
function setPercentageHidden(value){
    document.getElementById("percentage").hidden = value
}

eel.expose(setPercentageValue)
function setPercentageValue(value){
    document.getElementById("percentage").innerHTML = value
}