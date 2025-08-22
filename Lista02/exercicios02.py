#Questão 01: mostrar os números de 0 a 100

lista_numeros = []
contador = 0
while contador < 100:
    contador += 1
    lista_numeros.append(contador)

print(lista_numeros)

#Questão 02: mostrar na tela numeros de 0 até n

lista_numeros_02 = []
contador_02 = 0
limite = int(input("Informe até onde você quer incrementar\n"))
while contador_02 < limite:
    contador_02 += 1
    lista_numeros_02.append(contador_02)

print(lista_numeros_02)

#Questão 03: Permitir que o usuario realize quantas somas quiser

print("Operação - Adição\n")

while True: 
    primeiro_numero = int(input("Digite um número: "))
    segundo_numero = int(input("Digite outro número: "))

    print(f"{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")

    continuar = input("Deseja realizar mais uma soma? [S ou N]\n")
    if continuar.lower() == "s":
        continue
    else:
        break








