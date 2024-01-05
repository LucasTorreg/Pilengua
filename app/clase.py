import pyphen

class Pi:

    def __init__(self) -> None:
        pass


    def separar_silabas(palabra):
    
        dic = pyphen.Pyphen(lang='es_ES')
        silabas = dic.inserted(palabra)

        return silabas
    
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
                palabra = silabas.split(silaba+"-")
                print(palabra, silaba)
                palabra = palabra[1]

                

        return lista


    def __str__(self) -> str:
        pass