while True:
    try:
        entradaInicial = input("").split(' ')
        casos = int(entradaInicial[0])
        identificador = int(entradaInicial[1])

        soma = 0

        for i in range (casos):
            entradaTeste = input("").split(' ')
            identificadores = int(entradaTeste[0])
            jogo = int(entradaTeste[1])
    
            if jogo == 0 and identificadores == identificador:
                soma += 1
        
        print(soma)
    except EOFError:
        break