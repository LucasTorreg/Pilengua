def letraActualAnterior(palabra):
    letras = list(palabra)
    pos=0
    for letra in letras:
        print ("Letra actual: ", letra)
        if pos != 0:
            print ("Letra anterior: ", letras[pAnterior])
        
        pos += 1
        pAnterior = pos - 1
        

letraActualAnterior("constante")
           