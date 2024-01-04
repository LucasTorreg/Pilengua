consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "ll", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

paresConsonantes = ["bl", "cl", "fl", "gl", "kl", "pl", "tl", "br", "cr", "dr" ,"fr", "gr", "kr", "pr", "tr", "ch", "ll", "rr"]

vocales = ["a", "e","i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]

vocales_abiertas = ["a", "e", "o", "á", "é", "ó", "ú"]

vocales_cerradas = ["i", "u", "ü"]


def silabeo(palabra):
    protoSilaba=[]
    sinUsar=""
    par=""
    actual=0

    for l in palabra:
        
        if l in vocales:
            
            if actual != 0:
                anterior = palabra[actual-1]
                
                if anterior in consonantes:
                    if par in paresConsonantes:
                        silaba = par + l
                    else:    
                        silaba = anterior+l

                    protoSilaba.append(silaba)
                   
                
                if l in vocales_abiertas:
                    if actual < len(palabra)-1:
                        posterior = palabra[actual+1]
                        if posterior in consonantes:
                            sinUsar += posterior
                            protoSilaba[-1]+=posterior

                elif l in vocales_cerradas:
                    protoSilaba[-1]+=l

                
        else:
            
            if actual != 0 and actual < len(palabra)-1:
                anterior = palabra[actual-1]
                posterior = palabra[actual+1]
                if anterior in consonantes and posterior in consonantes:
                    sinUsar += l
                    protoSilaba[-1]+=l

                elif anterior in vocales and posterior in consonantes:
                    par+= l+posterior
                    
        
        actual+=1
        print(par)
        print(sinUsar)



    return protoSilaba

    


"""
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
"""