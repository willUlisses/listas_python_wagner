#Questão 01: pegar um int e verificar se é par ou impar

print("é par" if int(input("digite um numero inteiro\n")) % 2 == 0 else "é impar")


#Questão 02: pedir dois numeros e imprimir o maior
numero1 = int(input("Digite o primeiro numero\n"))
numero2 = int(input("Digite o segundo numero\n"))
lista_maior_numero = [numero1, numero2]
print(f"O maior número é: {max(lista_maior_numero)}")

#Questão 03: verificar se uma letra é vogal ou consoante
letra = input("digite uma letra\n")
print("é vogal" if letra.lower() in "aeiou" else "é consoante")

#Questão 04: Ler duas notas de um aluno e calcular a média do aluno
nota01 = float(input("Informe a primeira nota\n"))
nota02 = float(input("Informe a segunda nota\n"))
media = (nota01 + nota02) / 2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#Questão 05: Ler 3 números e mostrar o maior deles (igual a segunda)
lista_maior_final = []
for i in range(3):
    numero_input = int(input(f"Digite o {i+1}º valor\n"))
    lista_maior_final.append(numero_input)

print(f"O maior valor é: {max(lista_maior_final)}")

#Questão 06: inputar um turno e retornar a respectiva mensagem de bom dia/tarde/noite
turno = input("Digite uma letra maiúscula correspondente ao seu turno!\n")
match turno:
    case "M":
        print("Bom dia!")
    case "V":
        print("Boa tarde!")
    case "N":
        print("Boa noite!")
    case _:
        print("valor inválido!")

#Questão 07: 5 perguntas sobre um crime
lista_perguntas = ["Telefonou para a vítima?\n", "Esteve no local do crime?\n", "Mora perto da vítima?\n", "Devia para a vítima?\n",
                   "Já trabalhou com a vítima?\n"]
contador_respostas_suspeitas = 0
for pergunta in lista_perguntas:
    resposta = input(pergunta)
    if resposta.lower() == "sim":
        contador_respostas_suspeitas += 1

if contador_respostas_suspeitas == 5:
    print("Assassino")
elif contador_respostas_suspeitas >= 3:
    print("Cúmplice")
elif contador_respostas_suspeitas == 2:
    print("Suspeito")
else: 
    print("Inocente")







