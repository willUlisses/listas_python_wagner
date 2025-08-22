import math

# --> imprimir a série de Fibonacci até o valor ser maior que 500:

fibonacci = []
index = 0

while True:
    if(len(fibonacci) == 0):
        fibonacci.append(0)
        continue
    elif(len(fibonacci) == 1):
        fibonacci.append(1)
        continue
    elif fibonacci[len(fibonacci) - 1] > 500:
        break

    last_num = len(fibonacci) - 1
    next_num = fibonacci[last_num - 1] + fibonacci[last_num]
    fibonacci.append(next_num)

print(fibonacci)

# --> programa que retorna o min, max e sum

lista_valores = []
while True:
    escolha = input("Quer adicionar um número à lista? [S ou N]\n")
    if escolha.lower() == "s":
        numero = int(input("Digite o número que será adicioando: "))
        lista_valores.append(numero)
    else:
        break

if (len(lista_valores) == 0):
    print("Não foram adicionados os valores!")
else:
    print(f"valor mínimo: {min(lista_valores)}")
    print(f"valor máximo: {max(lista_valores)}")
    print(f"soma de todos os valores: {sum(lista_valores)}")


# --> Validação dos valores dos inputs do desafio acima:

lista_valores_02 = []
while True:
    escolha_02 = input("Quer adicionar um número à lista? [S ou N]\n")
    if escolha_02.lower() == "s":
        numero_validado = int(input("Digite o número que será adicioando: "))
        if numero_validado < 0 or numero_validado > 1000:
            print("O valor inserido é inválido, tente um número entre 0 e 1000")
        else:    
            lista_valores_02.append(numero_validado)
    else:
        break

if (len(lista_valores_02) == 0):
    print("Não foram adicionados os valores!")
else:
    print(f"valor mínimo: {min(lista_valores_02)}")
    print(f"valor máximo: {max(lista_valores_02)}")
    print(f"soma de todos os valores: {sum(lista_valores_02)}")

# --> Programa que leia e valide determinados inputs (não entendi muito bem se era pra validar a cada input ou se era pra validar no final):

respostas = []

while True:
    nome = input("Informe seu nome:\n")
    if len(nome) > 3:
        respostas.append(nome)
        break
    else:
        print("O nome deve conter mais de 3 letras")

while True:
    idade = int(input("informe sua idade:\n"))
    if idade >= 0 and idade <= 150:
        respostas.append(idade)
        break
    else:
        print("Informe uma idade entre 0 e 150")

while True: 
    salario = float(input("Informe seu salário:\n"))
    if salario > 0:
        respostas.append(salario)
        break
    else:
        print("informe um salário maior do que R$0")

while True: 
    sexo = input("Informe seu sexo [f ou m]:\n")
    if sexo.lower() == "f" or sexo.lower() == "m":
        respostas.append(sexo)
        break
    else:
        print("O sexo deve ser informado como uma letra singular [f ou m]")

while True:
    estado_civil = input("Informe seu estado civil: [s, c, v ou d]\n")
    if estado_civil.lower() in "scvd":
        respostas.append(estado_civil)
        break
    else:
        print("O estado civil deve ser informado como uma letra singular [s, c, v ou d]")

print(f"respostas já validadas: {respostas}")

# --> Verificar se um número é primo ou não

numero_para_verificar = int(input("Digite um número: "))

if numero_para_verificar < 2:
    print("O número não é primo!")
else: 
    for i in range(2, int(math.sqrt(numero_para_verificar))): #não sabia como pegar a raiz quadrada com a sintaxe basica bruta, então apelei
        if numero_para_verificar % i == 0:
            print("O número não é primo")
    
print("O número é primo")


    


