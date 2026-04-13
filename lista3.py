import random
from datetime import datetime
from util import inputint, inputfloat, gerar_palavra

'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''

# def exemploPara(): # Quando se sabe a qtde de repetições
#     for c in range(10): #0-9 Baseado em intervalo (inicio e fim)
#         print(c)
#     for c in range(1,10): #1-9
#         print(c)
#     for c in range(1,10,2): #1,3,5,7,9

# def exemploEnquanto(): # Quando não se sabe quantas iterações serão necessárias
#     opcao=-1
#     while opcao != 0: #baseado em uma condição (True|False)
#         opcao = int(input('Opção: '))

#1.Faça um programa que imprima todos os números de 1 até 100.

def questao_1():
    print("\nTodos os números de 1 até 100: \n")
    for num in range(1,101):
        print(num, end=" ")

#2. Faça um programa que imprima todos os números pares de 100 até 1.

def questao_2():
    print("\nTodos os pares de 100 até 1: \n")
    for num in range(101, 1, -1): # 100,1,-2
        if (num % 2 == 0):
            print(num, end=" ")

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.

def questao_3():
    print("\nTodos os múltiplos de 1 até 500: \n")
    for num in range(1,501):
        if (num % 5 == 0):
            print(num, end=" ")

#4. Faça um programa que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.

def questao_4():
    print("\n")
    for _ in range(20):
        nome = str = gerar_palavra()
        idade = int = random.randrange(1,121)
        sexo = str = random.choice(("Masculino", "Feminino"))
        if (sexo == "Masculino") and (idade > 21):
            print(f"A pessoa {nome:10} do sexo {sexo} tem {idade} anos de idade.")

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.

def questao_5():
    num1 = inputint("\nDigite o primeiro número (multiplicando): ")
    num2 = inputint("Digite o segundo número (multiplicador): ")

    produto = 0
    contador = 0

    while contador < num2:
        produto = produto + num1
        contador = contador + 1

    print(f"\nO produto de {num1} x {num2} através de somas sucessivas é: {produto}")

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21

def questao_6():  
    anterior = 1
    atual = 1

    print(f"\n1º termo: {anterior}")
    print(f"2º termo: {atual}")

    for i in range(3, 21):
        proximo = anterior + atual
        print(f"{i}º termo: {proximo}")
        
        anterior = atual
        atual = proximo

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.

# def questao_7():
#     soma_geral = 0

#     for i in range(1,16):
#         aluno = input(f"\n{i}º Aluno: ").title().strip()
#         nota_1 = inputfloat("Nota da prova 1: ", min=0, max=10)
#         nota_2 = inputfloat("Nota da prova 2: ", min=0, max=10)
#         m_aluno = (nota_1 + nota_2) / 2
#         soma_geral += m_aluno

#         print(f"\nNome do {i}º Aluno: {aluno}\nNota da prova 1: {nota_1}\nNota da prova 2: {nota_2}\nMédia do Aluno: {m_aluno}")

#     print(f"\nMédia geral: {(soma_geral / 15):.2f}")

def questao_7():
    soma_medias_turma = 0
    total_alunos = 15

    for i in range(1, total_alunos + 1):
        aluno = input(f"\nNome do {i}º Aluno: ").title().strip()
        n1 = inputfloat(f"Nota da Prova 1 de {aluno}: ", min=0, max=10)
        n2 = inputfloat(f"Nota da Prova 2 de {aluno}: ", min=0, max=10)
        
        media_aluno = (n1 + n2) / 2
        soma_medias_turma += media_aluno 

        print("-" * 30)
        print(f"Aluno: {aluno}")
        print(f"Notas 1 e 2: {n1} | {n2}")
        print(f"Média: {media_aluno:.2f}")
        print("-" * 30)

    media_geral = soma_medias_turma / total_alunos
    print(f"\n{'='*30}")
    print(f"Média Geral: {media_geral:.2f}")
    print(f"{'='*30}")

#8. Faça um programa que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRPF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto

def questao_8():
    for i in range(1,11):
        nome = input("\nInforme seu nome: ").title().strip()
        salario_irpf = inputfloat("Informe seu salário: ", min=0)

        if (salario_irpf < 1300):
            print(f"\n{i}º Caso:\n\n{nome} | Isento")
        elif (salario_irpf >= 1300) and (salario_irpf < 2300):
            print(f"\n{i}º Caso:\n\n{nome} | 10% do salário bruto: {(salario_irpf * 0.10):.2f}")
        else:
            print(f"\n{i}º Caso:\n\n{nome} | 15% do salário bruto: {(salario_irpf * 0.15):.2f}")

#9. No dia da estreia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.

def questao_9():
    qnt_exce = 0
    qnt_bom = 0
    qnt_regular = 0
    soma_idade = 0

    print("\n", end= "=" * 30)
    print('\nCrítica do filme "Procurando Dory"')
    print("=" * 30)

    print("\nExcelente - 3")
    print("Bom - 2")
    print("Regular - 1")

    for i in range(1,21):
        idade = inputint("\nInforme sua idade: ", min=1, max=120)
        opiniao = inputint("Qual sua opinião sobre o filme: ", min=1, max=3)

        if (opiniao == 3):
            qnt_exce += 1
            soma_idade += idade
        if (opiniao == 2):
            qnt_regular += 1
        if (opiniao == 1):
            qnt_bom += 1

    try:
        print(f"\nMédia das idades das pessoas que responderam excelente: {(soma_idade / qnt_exce):.2f}")
    except ZeroDivisionError:
        print(f"\nMédia das idades das pessoas que responderam excelente: 0")
    print(f"Quantidade de pessoas que responderam Regular: {qnt_regular}")
    porcen_bom = (qnt_bom / (qnt_exce + qnt_bom + qnt_regular)) * 100
    print(f"Porcentagem de pessoas que responderam bom entre todos os expectadores analisados: {porcen_bom}%")

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.

# def questao_10():
#     print("\n", end= "=" * 30)
#     print('\nCampeonato Europeu de Volleyball')
#     print("=" * 30)

#     soma_peso_equipe = 0
#     soma_idade_equipe = 0

#     for i in range(1,3):
#         for j in range(1,2):
#             peso = inputfloat(f"\nPeso do {j} jogador da equipe {i}: ", min=50, max=100)
#             idade = inputint(f"Idade do {j} jogador da equipe {i}: ", min=1, max=120)

#             mais_pesado = peso
#             mais_jovem = idade

#             if (peso > mais_pesado):
#                 mais_pesado = peso
#                 atleta_pesado = j
#             if (idade < mais_jovem):
#                 mais_jovem = idade
#                 atleta_jovem = j
                
#             print("=" * 30)
#             print("Informações Equipe")
#             print("=" * 30)

#             soma_peso_equipe += peso
#             soma_idade_equipe += idade

#             media_peso_equipe = soma_peso_equipe / j
#             media_idade_equipe = soma_idade_equipe / j

#         print(f"\nMédia de peso da equipe: {media_peso_equipe:.2f}")
#         print(f"Média de idade da equipe: {media_idade_equipe:.2f}")
#         print(f"Atleta mais pesado da equipe {i}: atleta {atleta_pesado}")
#         print(f"Atleta mais jovem da equipe {i}: atleta {atleta_jovem}")
    
#     print("=" * 30)
#     print("Informações Geral")
#     print("=" * 30)

#     media_peso = soma_peso_equipe / i
#     media_idade = soma_idade_equipe / i

#     print(f"\nMédia do peso geral: {media_peso:.2f}")
#     print(f"Média da idade geral: {media_idade:.2f}")

def questao_10():
    print("\n" + "=" * 30)
    print('Campeonato Europeu de Volleyball')
    print("=" * 30)

    soma_peso_geral = 0
    soma_idade_geral = 0
    total_atletas_campeonato = 0

    num_equipes = 2
    atletas_por_equipe = 3

    for i in range(1, num_equipes + 1):
        soma_peso_equipe = 0
        soma_idade_equipe = 0
        
        mais_pesado = 0
        mais_jovem = 999
        atleta_pesado = 0
        atleta_jovem = 0

        print(f"\n--- Equipe {i} ---")

        for j in range(1, atletas_por_equipe + 1):
            peso = inputfloat(f"Peso do {j}º jogador da equipe {i}: ", min=50, max=150)
            idade = inputint(f"Idade do {j}º jogador da equipe {i}: ", min=1, max=120)

            if peso > mais_pesado:
                mais_pesado = peso
                atleta_pesado = j
            
            if idade < mais_jovem:
                mais_jovem = idade
                atleta_jovem = j

            soma_peso_equipe += peso
            soma_idade_equipe += idade
            
            soma_peso_geral += peso
            soma_idade_geral += idade
            total_atletas_campeonato += 1

        media_p_equipe = soma_peso_equipe / atletas_por_equipe
        media_i_equipe = soma_idade_equipe / atletas_por_equipe

        print("-" * 30)
        print(f"Média de peso da equipe {i}: {media_p_equipe:.2f} kg")
        print(f"Média de idade da equipe {i}: {media_i_equipe:.2f} anos")
        print(f"Atleta {atleta_pesado} é o mais pesado ({mais_pesado} kg)")
        print(f"Atleta {atleta_jovem} é o mais jovem ({mais_jovem} anos)")

    print("\n" + "=" * 30)
    print("Informações gerais do campeonato")
    print("=" * 30)
    
    media_peso_geral = soma_peso_geral / total_atletas_campeonato
    media_idade_geral = soma_idade_geral / total_atletas_campeonato

    print(f"Média de peso geral: {media_peso_geral:.2f} kg")
    print(f"Média de idade geral: {media_idade_geral:.2f} anos")

#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.

def questao_11():
    qnt_num = 0
    print("\n")

    while True:
        num = inputint("Informe um número: ")

        if (num >= 100) and (num <= 200):
            qnt_num += 1
        elif (num == 0):
            break
    
    print(f"\nQuantidade total de números informado entre 100 e 200: {qnt_num}")

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.

def questao_12():
    pop_pais_A = 5000000
    pop_pais_B = 7000000

    taxa_nat_A = 0.03
    taxa_nat_B = 0.02
    t_anos = 0

    while (pop_pais_A <= pop_pais_B):
        pop_pais_A += pop_pais_A * taxa_nat_A
        pop_pais_B += pop_pais_B * taxa_nat_B
        t_anos += 1

    print(f"\nSerão necessários {t_anos} anos para que a população do país A ultrapasse a do país B.")
    print(f"População final país A: {pop_pais_A:,.0f}")
    print(f"População final país B: {pop_pais_B:,.0f}")

#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• A média de consumo dos tipos 1 e 2

def questao_13():
    soma_kwh_1 = 0
    soma_kwh_2 = 0
    soma_kwh_3 = 0
    qtd_consumidores_1_2 = 0

    while True:
        num_consumidor = inputint("\nNúmero do consumidor (0 para sair): ", min=0)
        
        if num_consumidor == 0:
            break
            
        qnt_kwh = inputfloat("Quantidade de kWh consumidos no mês: ", min=0)
        codigo = inputint("Tipo (1-Residencial, 2-Comercial, 3-Industrial): ", min=1, max=3)

        if codigo == 1:
            custo_individual = qnt_kwh * 0.3
            soma_kwh_1 += qnt_kwh
            qtd_consumidores_1_2 += 1
            print(f"\nCusto para o consumidor {num_consumidor}: R$ {custo_individual:.2f}")
        elif codigo == 2:
            custo_individual = qnt_kwh * 0.5
            soma_kwh_2 += qnt_kwh
            qtd_consumidores_1_2 += 1
            print(f"\nCusto para o consumidor {num_consumidor}: R$ {custo_individual:.2f}")
        elif codigo == 3:
            custo_individual = qnt_kwh * 0.7
            soma_kwh_3 += qnt_kwh
            print(f"\nCusto para o consumidor {num_consumidor}: R$ {custo_individual:.2f}")
        else:
            print("Código inválido! Dados deste consumidor ignorados.")

    total_geral_kwh = soma_kwh_1 + soma_kwh_2 + soma_kwh_3
    
    if qtd_consumidores_1_2 > 0:
        media_1_2 = (soma_kwh_1 + soma_kwh_2) / qtd_consumidores_1_2
    else:
        media_1_2 = 0

    print("\n" + "="*40)
    print(f"Total de consumo Tipo 1: {soma_kwh_1:.2f} kWh")
    print(f"Total de consumo Tipo 2: {soma_kwh_2:.2f} kWh")
    print(f"Total de consumo Tipo 3: {soma_kwh_3:.2f} kWh")
    print(f"Média de consumo dos tipos 1 e 2: {media_1_2:.2f} kWh")
    print("="*40)

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n

def questao_14():
    while True:
        num = inputint("\nInforme um valor inteiro: ", min=0)

        if (num < 1):
            break

        fatorial = 1

        for i in range(1,num + 1):
            fatorial = fatorial * i

        print(f"\nFatorial de {num}: {fatorial}")

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos

def questao_15():
    qnt_menos_21 = 0
    qnt_mais_50 = 0

    while True:
        idade = inputint("\nInforme sua idade: ",min=0, max=121)

        if (idade == 0):
            break
        elif (idade < 21):
            qnt_menos_21 += 1
        elif (idade > 50 ):
            qnt_mais_50 += 1

    print(f"\nTotal de pessoas com menos de 21 anos: {qnt_menos_21}")
    print(f"Total de pessoas com mais de 50 anos: {qnt_mais_50}")

#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão

def questao_16():
    dividendo = inputint("\nInforme o dividendo (número a ser dividido): ", min=0)
    divisor = inputint("Informe o divisor (quem divide): ", min=0)

    resto = dividendo
    quociente = 0

    while resto >= divisor:
        resto = resto - divisor
        quociente += 1
    
    print("-" * 30)
    print(f"Dividendo: {dividendo}")
    print(f"Divisor: {divisor}")
    print(f"Quociente (inteiro): {quociente}")
    print(f"Resto da divisão: {resto}")
    print("-" * 30)

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.
 
def questao_17():
    while True:
        n_pedido = inputint("\nNúmero do pedido: ", min=0)

        if (n_pedido == 0):
            print("\nEncerrando pedidos...")
            break

        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        if {mes < 10}:
            data_pedido = f"{dia}/0{mes}/{ano}"
        else:
            data_pedido = f"{dia}/0{mes}/{ano}"
        preco = inputfloat("Preço unitário: ", min=1)
        quantidade = inputint("Quantidade: ", min=1)

        print("\n", 30 * "=")
        print(f"Nº Pedido: {n_pedido}\nData: {data_pedido}\nPreço unitário: R${preco:.2f}\nQuantidade: {quantidade}\nPreço total: R${(preco * quantidade):.2f}")
        print(30 * "=")

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça um programa que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

def questao_18():
    total_fatura = 0

    while True:
        print(30 * "=")
        print("POUSADA")
        print("\nValor da diária: R$30,00")
        print("Menos de 10 dias: R$15,00")
        print("10 dias ou mais: R$8,00")
        print(30 * "=")

        n_conta = inputint("\nNúmero da conta: ", min=0)

        if (n_conta == 0):
            print("\nEncerrando registros...")
            break
        
        nome = input("Nome: ").title().strip()
        dias = inputint("Quantidade de dias: ", min=1)
        if (dias < 10):
            taxa_servico = 15
        else:
            taxa_servico = 8

        conta = (30 + taxa_servico) * dias
        total_fatura += conta
    
        print("\n===== Extrato do Cliente =====")
        print(f"Nº Conta: {n_conta}\nNome: {nome}\nDias: {dias}\nValor total: R${conta:.2f}")
        print(30 * "=")
    
    print(30 * "=")
    print(f"Faturamento total da pousada: R${total_fatura:.2f}")
    print(30 * "=")

#19. Em uma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado com nota >= 7.0

def questao_19():
    print(30 * "-")
    print("Prova de Algoritmos")
    print(30 * "-")
    
    qnt_turmas = inputint("Quantidade de turmas: ", min=1)

    for i in range (1, qnt_turmas + 1):
        print(30 * "-")
        print(f"{i}º TURMA")
        print(30 * "-")

        qnt_aprovados = 0
        qnt_reprovados = 0
        soma_notas = 0

        qnt_alunos = inputint(f"Quantidade de alunos na {i}º turma: ", min=1)

        for j in range(1, qnt_alunos + 1):
            nota_aluno = inputfloat(f"\nNota do {j}º aluno: ", min=0, max=10)
            soma_notas += nota_aluno

            if (nota_aluno >= 7.0):
                qnt_aprovados += 1
            else:
                qnt_reprovados += 1

        media_turma = soma_notas / qnt_alunos
        percentual_repro = (qnt_reprovados / qnt_alunos) * 100

        print(30 * "-")
        print(f"RESULTADOS DA {i}º TURMA\n\nAprovados: {qnt_aprovados}\nMédia da turma: {media_turma:.2f}\nPercentual de reprovados: {percentual_repro:.2f}%")
        print(30 * "-")

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.

#21. Em uma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número de multas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir também o número da carteira do motorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexo masculino mais pesado;
#• a média de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores não negativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar um valor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça um programa que calcule o imposto de renda de um grupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito um abatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em um determinado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram 5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa um programa que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#• a quantidade de pessoas com idade superior a 50 anos;
#• a média das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em um determinado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, V-viúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• a média das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.


e = True
while (e == True):
    try:
        questao = int(input("Digite o número da questão: "))
        if questao < 1 or questao > 30:
            raise Exception("Questão inválida! Valores devem ser entre 1 e 30.")
        eval(f"questao_{questao}()")
        e = False
    except ValueError:
        print("Valor inválido! Apenas valor numérico inteiro.")
    except Exception as erro:
        print(erro)