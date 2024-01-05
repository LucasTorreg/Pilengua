import pyphen

def separar_silabas(palabra):
    
    dic = pyphen.Pyphen(lang='es_ES')
    silabas = dic.inserted(palabra)

    return silabas



