"""
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
"""
import pyphen

def pi(palabra):
    lista =[]
    dic = pyphen.Pyphen(lang='es_ES')
    silabas = dic.inserted(palabra)
    #lista=list(silabas)
    
    for i in silabas:
        actual = silabas.index(i)
        if i == "-" or actual == len(silabas)-1:
            silaba = silabas[: actual]
            lista.append("pi"+silaba)
            silaba = silabas.split(silaba+"-")
            print(palabra, silaba)
            silaba = silaba[1]

            

    return lista

print(pi("prueba"))
           