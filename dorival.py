
   # numero = int(input("Digite um número: "))
#if numero % 2 == 0:
  #  print("O número é par.")
#else:
  #  print("O número é ímpar.")

#********************

# = int(input("Digite um número: "))

#if numero > 10:
   # print("O número é maior que 10.")
#else:
   # print("O número não é maior que 10.")

#********************

#idade = int(input("Digite a sua idade: "))
#if idade >= 18:
    #print("Você é maior de idade.")
#else:
    #print("Você é menor de idade.")

#********************

#idade = int(input("Digite a sua idade: "))
#if idade < 16:
    #print("Você não tem voto.")
#elif idade < 18 or idade > 70:
    #print("Seu voto é opcional.")
#else:
    #print("Seu voto é obrigatório.")

#********************

#numero = float(input("Digite um número: "))
#if numero > 0:
    #print("O número é positivo.")
#elif numero < 0:
    #print("O número é negativo.")
#else:
    #print("O número é zero.")

#********************

#nota = float(input("Digite uma nota entre 0 e 10: "))

#if 9 <= nota <= 10:
   # print("Classificação: A")
#elif 7 <= nota < 9:
   # print("Classificação: B")
#elif 5 <= nota < 7:
   # print("Classificação: C")
#elif 3 <= nota < 5:
   # print("Classificação: D")
#elif 0 <= nota < 3:
  #  print("Classificação: E")
#else:
   # print("Nota inválida! A nota deve estar entre 0 e 10.")

#*******************

#valor_compra = float(input("Qual o valor total da sua compra? R$ "))

# valor_compra < 100:
   # desconto = valor_compra * 0.05
#elif valor_compra <= 500:
   # desconto = valor_compra * 0.10
#else:
  #  desconto = valor_compra * 0.15

#valor_final = valor_compra - desconto
#print(f"Você ganhou um desconto de R$ {desconto:.2f}.")
#print(f"O valor final da sua compra é: R$ {valor_final:.2f}.")


#********************

#lado1 = float(input("Digite o comprimento do primeiro lado: "))
#lado2 = float(input("Digite o comprimento do segundo lado: "))
#lado3 = float(input("Digite o comprimento do terceiro lado: "))

#if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    #if lado1 == lado2 == lado3:
       # print("O triângulo é equilátero.")
    #elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
      #  print("O triângulo é isósceles.")
    #else:
       # print("O triângulo é escaleno.")
#else:
    #print("Não é possível fazer um triângulo com esses lados.")

#********************

#ano = int(input("Digite um ano: "))
#if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    #print(f"O ano {ano} é bissexto.")
#else:
    #print(f"O ano {ano} não é bissexto.")

#*********************

#peso = float(input("Digite o seu peso (kg): "))
#altura = float(input("Digite a sua altura (m): "))

#imc = peso / (altura ** 2)

#if imc < 18.5:
   # print("Abaixo do peso")
#elif 18.5 <= imc <= 24.9:
   # print("Peso normal")
#elif 25 <= imc <= 29.9:
  #  print("Sobrepeso")
#else:
   # print("Obesidade")

#**********************

#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero3 = float(input("Digite o terceiro número: "))

#if numero1 < numero2 < numero3:
  #  print("Os números estão em ordem crescente.")
#elif numero1 > numero2 > numero3:
  #  print("Os números estão em ordem decrescente.")
#elif numero1 == numero2 == numero3:
  #  print("Os números são iguais.")
#else:
  #  print("Os números não estão em ordem crescente nem decrescente.")

#*************************

#temperatura = float(input("Digite a temperatura em Celsius: "))
#if temperatura < 10:
   # print("Frio")
#elif 10 <= temperatura <= 25:
   # print("Aconchegante")
#elif 25 < temperatura <= 40:
   # print("Quente")
#else:
   # print("Muito Quente")

#*************************

#temperatura = float(input("Digite a temperatura em Celsius: "))
#if temperatura < 10:
   # print("Frio")
#elif 10 <= temperatura <= 25:
   # print("Aconchegante")
#elif 25 < temperatura <= 40:
   # print("Quente")
#else:
  #  print("Muito Quente")

#*************************

#data = input("Digite uma data no formato dd/mm/aaaa: ")
#dia, mes, ano = data.split("/")
#nova_data = f"{ano}-{mes}-{dia}"
#print("A data no formato aaaa-mm-dd é:", nova_data)

#*************************

#import re
#senha = input("Digite a sua senha: ")

#if len(senha) < 8:
    #print("A senha deve ter pelo menos 8 caracteres.")
#elif not re.search("[a-z]", senha):
   # print("A senha deve ter pelo menos uma letra minúscula.")
#elif not re.search("[A-Z]", senha):
   # print("A senha deve ter pelo menos uma letra maiúscula.")
#elif not re.search("[0-9]", senha):
    #print("A senha deve ter pelo menos um número.")
#elif not re.search("[@#$%&]", senha):
  #  print("A senha deve ter pelo menos um caractere especial (@, #, $, %, &).")
#else:
    #print("Senha válida!")

#*************************

#import math
#numero = float(input("Digite um número: "))
#if numero < 0:
   # print("Não é possível calcular a raiz quadrada de um número negativo.")
#elif numero > 100:
    #print("Número muito grande, reduza para um valor abaixo de 100.")
#else:
   # raiz = math.sqrt(numero)
    #print(f"A raiz quadrada de {numero} é {raiz:.2f}.")

#*************************

#expressao = input("Digite qualquer expressão matemática: ")
#try:
   # resultado = eval(expressao)
   # print(f"O resultado da expressão escolhida é: {resultado}")
#except Exception as e:
   # print(f"Ocorreu um erro ao avaliar a expressão que voce passou: {e}")

#*************************

#cpf = input("Digite o número do CPF (XXX.XXX.XXX-XX): ").replace(".", "").replace("-", "")

#if len(cpf) != 11 or not cpf.isdigit():
   # print("CPF inválido")
#else:
   # peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
  #  peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

   # soma1 = 0
   # for i in range(9):
   #     soma1 += int(cpf[i]) * peso1[i]
   # resto1 = soma1 % 11
   # if resto1 < 2:
  #      digito1 = 0
  #  else:
  #      digito1 = 11 - resto1
#
  #  soma2 = 0
  #  for i in range(10):
  #      soma2 += int(cpf[i]) * peso2[i]
  #  resto2 = soma2 % 11
  #  if resto2 < 2:
  #      digito2 = 0
   # else:
    #    digito2 = 11 - resto2

    #if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
       # print("CPF Válido")
    #else:
        #print("CPF Inválido")

# ******************************

