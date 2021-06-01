function callPython(){
    eel.hello()
}

function callPythonMakeArt(){
    var loader = document.getElementById("loader")
    loader.hidden = false
    var text = document.getElementById("url").value
    var l = document.getElementById("altura").value
    var a = document.getElementById("largura").value
    var nome = document.getElementById("nome").value

    eel.call_create_map(a,l,text,nome,false)
}

eel.expose(hideLoader)
function hideLoader(){
    var loader = document.getElementById("loader")
    loader.hidden = true
}