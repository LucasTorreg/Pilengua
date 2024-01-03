consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

vocales_abiertas = ["a", "e", "o", "á", "é", "ó", "ú"]

vocales_cerradas = ["i", "u", "ü"]

semivocales = ["y"]


def separarSilabas(palabra):
    letras = list(palabra)
    grupos_vocales=[]
    consonante_izquierda=[]
    
    
    pos=0
    for letra in letras:
        if letra in vocales_abiertas:
            grupos_vocales.append(letra)
            if pos != 0 and letras[pAnterior] in consonantes:
                union = letras[pAnterior]+letra
                consonante_izquierda.append(union)

        pos += 1
        pAnterior = pos - 1

    return consonante_izquierda
