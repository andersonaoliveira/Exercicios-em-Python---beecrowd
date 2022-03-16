def binarioparainteiro(binario):
    contador = 0
    global inteiro
    inteiro = 0 
    
    while(binario != 0):
        a = binario % 10
        inteiro = inteiro + a *pow(2, contador)
        binario = binario // 10
        contador += 1 
    return inteiro
    
binario = 0
x = 0
inteiroFinal = 0
contador = 1
a = 0
b = 0
c = 0

while x != "saida":
    x = input()
    SubZero = x.replace("-","0")
    SubUm = SubZero.replace("*","1")
    x = SubUm
    if x != "caw caw":
        binarioparainteiro(int(x))
        inteiroFinal += inteiro
    elif x == "caw caw":
        if contador == 1:
            a = inteiroFinal
            inteiroFinal = 0
            contador += 1
        elif contador == 2:
            b = inteiroFinal
            inteiroFinal = 0
            contador += 1
        elif contador == 3:
            c = inteiroFinal
            x = "saida"
print (a)
print (b)
print (c)