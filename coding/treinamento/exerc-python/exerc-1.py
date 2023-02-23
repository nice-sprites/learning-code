#Exercício 1: Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

#definições
def space():
    print("")
    print("")

def pattern(n = int(input("Defina um valor: "))):
    for i in range(1,n+1):
        space()
        for j in range(1,i+1):
            print(i, end=" ")

#função
mostrafunc = input('mostrar o valor da função? (S/N): ')

if(mostrafunc == "s"):
    space()
    print("você aceitou a função")
    space()
    pattern()

elif(mostrafunc == "n"):
    space()
    print("você não aceitou a função, mas eu vou te mostrar do mesmo jeito")
    space()
    pattern()

else:
    print("erro")

#sucesso