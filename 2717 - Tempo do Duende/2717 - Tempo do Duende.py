total = int(input())
brinquedos = input("").split(' ')
a = int(brinquedos[0])
b = int(brinquedos[1])

if total < (a+b):
    print("Deixa para amanha!")
else:
    print("Farei hoje!")