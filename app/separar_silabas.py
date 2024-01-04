consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

vocales = ["a", "e","i", "o", "u", "á", "é", "í", "ó", "ú"]

vocales_abiertas = ["a", "e", "o", "á", "é", "ó", "ú"]

vocales_cerradas = ["i", "u", "ü"]

semivocales = ["y"]


def separarSilabas(palabra):
    silabas = []

    usadas=[]
    consonante_izquierda=[]
    
    for l in palabra:
        if l in vocales:
            actual = palabra.index(l)
            if actual != 0:
                anterior = palabra[actual-1]

            if anterior in vocales and l in vocales:
                if len(palabra)<actual+1:
                    silabas[-1] += l


            if palabra[actual] in vocales:
                silaba = palabra[: actual+1]

                silabas.append(silaba)
                palabra = palabra.split(silaba)
                print(palabra, silaba)
                palabra = palabra[1]



    return silabas
