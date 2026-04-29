import random
from datetime import datetime
from util import inputint, inputfloat, gerar_palavra, gerar_letra

'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".

def questao_1():
    numeros = []

    for _ in range(15):
        numeros.append(random.randrange(200))

    print("\n15 números inteiros: \n")
    for i, numero in enumerate(numeros):
        print(f"Posição: {i + 1} | Número: {numero}")
    
    n_busca = inputint("\nInforme o número a ser localizado: ")
    try:
        posicao = numeros.index(n_busca) + 1
    except ValueError:
        print("\nValor não encontrado!")
    else:
        print(f"\nNúmero {n_busca} localizado na posição: {posicao}")

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)

def questao_2():
    letras = []

    for _ in range(10):
        letra_gerada = gerar_letra(1)
        letras.append(letra_gerada)

    print("\nLetras enumeradas: \n")
    for i, letra in enumerate(letras):
        print(f"{i + 1} - {letra}")

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)

def questao_21():
    qnt_caracters = inputint("\nInforme a quantidade de caracteres para a geração de uma senha aleatória: ", min=6)

    caracteres = [chr(random.randrange(40, 127)) for _ in range(qnt_caracters)]

    print(f"\nSenha sugerida: {''.join(caracteres)}")

    # print("\nSenha sugerida:", end=" ")
    # for caracter in caracteres:
    #     print(caracter, end="")
    # print() 

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

def questao_3():
    numeros = [random.randrange(200) for _ in range(15)]

    for i, numero in enumerate(numeros):
        if (numero % 2 == 0):
            print(f"{i + 1} número: {numero} | Par") 
        else:
            print(f"{i + 1} número: {numero} | Ímpar") 

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.

def questao_4():
    numeros = [random.randrange(200) for _ in range(8)]

    multiplos_6 = 0

    for i, numero in enumerate(numeros):
        if (numero % 6 == 0):
            multiplos_6 += 1
            print(f"{i + 1} número: {numero} | Múltiplo de 6") 
        else:
            print(f"{i + 1} número: {numero}") 
            
    print(f"\nQuantidade de números múltiplos de seis: {multiplos_6}")

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.

# def questao_5():
#     notas_1 = [round(random.uniform(0.0, 10.0), 1) for _ in range(15)]
#     notas_2 = [round(random.uniform(0.0, 10.0), 1) for _ in range(15)]

#     for nota_1 in notas_1:
#         print(nota_1) 

#     for nota_1 in notas_1:
#         print(nota_1) 

#     for i, nota_1 in enumerate(notas_1):
#         for nota_2 in notas_2:
#             media_aluno = (nota_1 + nota_2) / 2
#             if (media_aluno >= 6.0):
#                 print(f"{i + 1}º aluno | Nota 1 : {nota_1} | Nota 2 : {nota_2} | Média : {media_aluno:.2f} | APROVADO")
#             else:
#                 print(f"{i + 1}º aluno | Nota 1 : {nota_1} | Nota 2 : {nota_2} | Média : {media_aluno:.2f} | REPROVADO")

def questao_5():
    notas_1 = [round(random.uniform(0.0, 10.0), 1) for _ in range(15)]
    notas_2 = [round(random.uniform(0.0, 10.0), 1) for _ in range(15)]
    
    medias = []
    situacoes = []

    for i in range(15):
        media = round((notas_1[i] + notas_2[i]) / 2) 
        medias.append(media)
        
        if media >= 6:
            situacoes.append("Aprovado")
        else:
            situacoes.append("Reprovado")

    print("\n" + "="*60)
    print(f"{'Nº':<4} | {'Nota 1':<8} | {'Nota 2':<8} | {'Média':<6} | {'Situação':<10}")
    print("-" * 60)

    for i in range(15):
        print(f"{i+1:<4} | {notas_1[i]:<8.1f} | {notas_2[i]:<8.1f} | {medias[i]:<6.1f} | {situacoes[i]:<10}")
    print("="*60)

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.

def questao_6():
    print("\n" + "="*50)
    print("ATUALIZAÇÃO SALARIAL - REAJUSTE 8%")
    print("="*50)

    salarios = [round(random.uniform(1412.0, 8000.0), 2) for _ in range(20)]
    
    novos_salarios = [round(salario * 1.08, 2) for salario in salarios]

    print(f"{'Nº':<4} | {'Salário Antigo':<15} | {'Novo Salário':<15}")
    print("-" * 50)

    for i in range(20):
        print(f"{i+1:<4} | R$ {salarios[i]:<12.2f} | R$ {novos_salarios[i]:<12.2f}")
    print("="*50)

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#uma lista e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

e = True
while (e == True):
    try:
        questao = inputint("Digite o número da questão: ")
        if questao < 1 or questao > 30:
            raise Exception("Questão inválida! Valores devem ser entre 1 e 30.")
        eval(f"questao_{questao}()")
        e = False
    except ValueError:
        print("Valor inválido! Apenas valor numérico inteiro.")
    except Exception as erro:
        print(erro)