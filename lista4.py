import random
from datetime import datetime
from rich.console import Console
from util import inputint, inputfloat, gerar_palavra, gerar_letra

'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

console = Console()

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
        console.print(f"Posição: [cyan]{i + 1}[/cyan] | Número: [blue]{numero}[/blue]")
    
    n_busca = inputint("\nInforme o número a ser localizado: ")
    try:
        posicao = numeros.index(n_busca) + 1
    except ValueError:
        print("\nValor não encontrado!")
    else:
        console.print(f"\nNúmero [blue]{n_busca}[/blue] localizado na posição: [green]{posicao}[/green]")

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)

def questao_2():
    letras = []

    for _ in range(10):
        letra_gerada = gerar_letra(1)
        letras.append(letra_gerada)

    print("\nLetras enumeradas: \n")
    for i, letra in enumerate(letras):
        console.print(f"{i + 1} - [yellow]{letra}[/yellow]")

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)

def questao_21():
    qnt_caracters = inputint("\nInforme a quantidade de caracteres para a geração de uma senha aleatória: ", min=6)
    caracteres = [chr(random.randrange(40, 127)) for _ in range(qnt_caracters)]

    console.print(f"\nSenha sugerida: [orange1]{''.join(caracteres)}[/orange1]")

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

def questao_3():
    numeros = [random.randrange(200) for _ in range(15)]

    for i, numero in enumerate(numeros):
        if (numero % 2 == 0):
            console.print(f"[white]{i + 1} número: {numero} |[/white] ", end="")
            console.print("Par", style="#d9ffa9")
        else:
            console.print(f"[white]{i + 1} número: {numero} |[/white] ", end="")
            console.print("Ímpar", style="#f1555a")

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.

def questao_4():
    numeros = [random.randrange(200) for _ in range(8)]

    multiplos_6 = 0

    for i, numero in enumerate(numeros):
        if (numero % 6 == 0):
            multiplos_6 += 1
            console.print(f"[white]{i + 1} número: {numero} |[/white] [bright_cyan]Múltiplo de 6[/bright_cyan]") 
        else:
            print(f"{i + 1} número: {numero}") 
            
    console.print(f"\nQuantidade de números múltiplos de seis: [bright_green]{multiplos_6}[/bright_green]")

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.

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
    console.print(f"[bold cyan]{'Nº':<4}[/bold cyan] | [bright_green]{'Nota 1':<8}[/bright_green] | ", end="")
    console.print(f"[bright_green]{'Nota 2':<8}[/bright_green] | [purple]{'Média':<6}[/purple] | [gold1]{'Situação':<10}[/gold1]")
    print("-" * 60)

    for i in range(15):
        if (situacoes[i] == "Aprovado"):
            console.print(f"[white]{i+1:<4} | {notas_1[i]:<8.1f} | {notas_2[i]:<8.1f} | {medias[i]:<6.1f} |[/white] [bright_green]{situacoes[i]:<10}[/bright_green]")
        else:
            console.print(f"[white]{i+1:<4} | {notas_1[i]:<8.1f} | {notas_2[i]:<8.1f} | {medias[i]:<6.1f} |[/white] [bright_red]{situacoes[i]:<10}[/bright_red]")
    print("="*60)

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.

def questao_6():
    print("\n" + "="*50)
    console.print("[bold white on bright_black]ATUALIZAÇÃO SALARIAL - REAJUSTE 8%[/bold white on bright_black]")
    print("="*50, "\n")

    salarios = [round(random.uniform(1412.0, 8000.0), 2) for _ in range(20)]
    novos_salarios = [round(salario * 1.08, 2) for salario in salarios]

    console.print(f"[bright_cyan]{'Nº':<4}[/bright_cyan] | [gold1]{'Salário Antigo':<15}[/gold1] | [spring_green2]{'Novo Salário':<15}[/spring_green2]")
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

def questao_7():
    compras = []
    vendas = []
    lucros = []

    lucro_menor_10 = 0
    lucro_entre_10_20 = 0
    lucro_maior_20 = 0

    for _ in range(100):
        compra = random.uniform(10.0, 500.0) 
        venda = random.uniform(10.0, 600.0)

        compras.append(compra)
        vendas.append(venda)

    for i in range(100):
        lucro_percentual = round(((vendas[i] - compras[i]) / compras[i]) * 100, 2)
        lucros.append(lucro_percentual)

        if lucro_percentual < 10:
            lucro_menor_10 += 1
        elif 10 <= lucro_percentual <= 20:
            lucro_entre_10_20 += 1
        else:
            lucro_maior_20 += 1

    console.print(f"[bright_cyan]{'Nº':<4}[/bright_cyan] | [gold1]{'Preço de Compra':<15}[/gold1] | ", end="")
    console.print(f"[spring_green2]{'Preço de Venda':<15}[/spring_green2] | [dodger_blue1]{'Lucro Percentual':<5}[/dodger_blue1]")
    print("-" * 50)
    
    for i in range(100):
        if (lucros[i] > 0):
            console.print(f"[white]{i+1:<4} | R$ {compras[i]:<12.2f} | R$ {vendas[i]:<12.2f} |[/white] [bright_green]{lucros[i]:<5}%[/bright_green]")
        else:
            console.print(f"[white]{i+1:<4} | R$ {compras[i]:<12.2f} | R$ {vendas[i]:<12.2f} |[/white] [bright_red]{lucros[i]:<5}%[/bright_red]")
    print("="*50)

    console.print(f"[grey50]{'FAIXA DE LUCRO':<25}[/grey50] | [bright_white]{'QUANTIDADE':<10}[/bright_white]")
    print("-" * 40)
    console.print(f"[white]Lucro < 10%               |[/white] [bright_red]{lucro_menor_10}[/bright_red]")
    console.print(f"[white]10% <= Lucro <= 20%       |[/white] [bright_yellow]{lucro_entre_10_20}[/bright_yellow]")
    console.print(f"[white]Lucro > 20%               |[/white] [bright_green]{lucro_maior_20}[/bright_green]")
    print("=" * 40)

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

def questao_8():
    produtos = {"código",
                "quantidade",
                "valor de compra",
                "valor de venda"
    }

    for _ in range(30):
        codigo = random.uniform(1000,9999)
        quantidade = random.uniform(1,500)
        valor_compra = random.uniform(10.0, 500.0)
        valor_venda = random.uniform(10.0, 500.0)

        produtos["código"] = codigo
        produtos["quantidade"] = quantidade
        produtos["valor de compra"] = valor_compra
        produtos["valor de venda"] = valor_venda

    for chave, valor in produtos.items():
        print(f"{chave} {valor}")

import random

def questao_8():
    estoque = {}

    for _ in range(30):
        codigo = random.randint(1000, 9999)
        quantidade = random.randint(1, 500)
        valor_compra = round(random.uniform(10.0, 500.0), 1)
        valor_venda = round(random.uniform(valor_compra, 700.0), 1)

        estoque[codigo] = {
            "quantidade": quantidade,
            "valor_compra": valor_compra,
            "valor_venda": valor_venda
        }

    while True:
        console.print("\n[green](1)[/green] - Listar todos os produtos")
        console.print("[yellow](2)[/yellow] - Buscar produto específico")
        console.print("[red](S)[/red] - Sair")
        
        opcao = input("\nDigite sua opção: ")
        
        if (opcao == '1'):
            console.print("\n            --- Listagem Completa ---\n")

            console.print(f"[bright_cyan]{'Código':<8}[/bright_cyan] | [gold1]{'Quantidade':<10}[/gold1] | ", end="")
            console.print(f"[spring_green2]{'Compra':<10}[/spring_green2] | [dodger_blue1]{'Venda':<5}[/dodger_blue1]")
            print("-" * 50)

            for codigo, dados in estoque.items():
                console.print(f"[white]{codigo:<8} | {dados['quantidade']:<10} | R${dados['valor_compra']:<10} | R${dados['valor_venda']:<5}[/white]")
                
        elif (opcao == '2'):
            try:
                cod_busca = inputint("\nInforme o código: ")
                if cod_busca in estoque:
                    produto = estoque[cod_busca]
                    console.print(f"\nProduto encontrado: [gold1]{cod_busca}[/gold1]")
                    console.print(f"Estoque: [green]{produto['quantidade']}[/green] | Preço Venda: [gold1]R${produto['valor_venda']}[/gold1]")
                else:
                    console.print("\n[bright_red]Código não encontrado.[/bright_red]")
            except ValueError:
                console.print("\n[red]Entrada inválida![/red]")
        
        elif (opcao.upper() == "S"):
            console.print("\n[orange1]Encerrando programa...[/orange1]")
            break

        else:
            console.print("\n[red]Opção inválida! Tente novamente.[/red]")

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

def questao_9():
    console.print("\n", 30 * "-", style="bright_black")
    console.print("[bold black on gold1]INTERSECÇÃO DE CONJUNTOS[/bold black on gold1]")
    console.print(30 * "-", style="bright_black")

    conjuntos_1 = [random.randrange(25) for _ in range(10)]
    conjuntos_2 = [random.randrange(25) for _ in range(10)]

    console.print(f"\n[bright_green]C1:[/bright_green] {conjuntos_1}")
    console.print(f"[bright_yellow]C2:[/bright_yellow] {conjuntos_2}\n")

    intercessao = sorted(list(set(conjuntos_1) & set(conjuntos_2)))
    contador = len(intercessao)

    console.print(30 * "-", style="bright_black")
    console.print(f"[bold]Elementos Comuns:[/bold] [gold1]{intercessao}[/gold1]")
    console.print(f"[bold]Quantidade de itens únicos em comum:[/bold] {contador}")

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

def questao_10():
    elementos = [random.randint(1, 10) for _ in range(10)]
    fatoriais = []
    
    for num in elementos:
        fatorial = 1
        for j in range(1, num + 1):
            fatorial *= j
        fatoriais.append(fatorial)

    console.print(f"\n[bold white on purple] LISTAGEM DE RESULTADOS [/bold white on purple]\n")
    console.print(f"[bright_cyan]{'Índice':<8}[/bright_cyan] | [gold1]{'Num':<6}[/gold1] | [spring_green2]{'Fatorial':<10}[/spring_green2]")
    console.print("-" * 35)

    qtd_pares = 0
    for i in range(10):
        console.print(f"[bright_white]{i + 1:<8} | {elementos[i]:<6} | {fatoriais[i]:<10}[/bright_white]")
        
        if fatoriais[i] % 2 == 0:
            qtd_pares += 1

    maior = max(fatoriais)
    menor = min(fatoriais)
    percentual_pares = (qtd_pares / len(fatoriais)) * 100
    media = sum(fatoriais) / len(fatoriais)

    console.print(f"\n" + 35 * "-")
    console.print(f"[bold green]▶ Maior:[/bold green] [bright_white]{maior}[/bright_white]")
    console.print(f"[bold red]▶ Menor:[/bold red] [bright_white]{menor}[/bright_white]")
    console.print(f"[bold yellow]▶ Percentual de Pares:[/bold yellow] [bright_white]{percentual_pares:.2f}%[/bright_white]")
    console.print(f"[bold cyan]▶ Média dos Fatoriais:[/bold cyan] [bright_white]{media:.2f}[/bright_white]")
    console.print(35 * "-" + "\n")

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

# def questao_12():
#     casa_espetaculo = [[0 for _ in range(5)] for _ in range(30)]

#     while True:
#         console.print("[bright_green](1)[/bright_green] - Listar todo os lugares")
#         console.print("[bright_yellow](2)[/bright_yellow] - Realizar reserva de um lugar")
#         console.print("[bright_red](S)[/bright_red] - Sair")

#         opcao = input("Escolha a opçaõ desejada: ")

#         if (opcao == "1"):
#             for i in range(30):
#                 print(casa_espetaculo[i])

def questao_12():
    mesas = [[5] for _ in range(30)]
    total_ocupado = 0
    limite_total = 150

    while total_ocupado < limite_total:
        console.print(f"\n[bold blue]Vagas totais ocupadas:[/bold blue] {total_ocupado}/{limite_total}")
        try:
            codigo = inputint("Digite o código da mesa (1-30) ou 0 para sair: ")
            
            if codigo == 0:
                break
            
            if 1 <= codigo <= 30:
                mesa_indice = codigo - 1
                vagas_na_mesa = mesas[mesa_indice][0]

                if vagas_na_mesa == 0:
                    console.print(f"[bold red]Mesa {codigo} está lotada![/bold red]")
                    continue

                quantidade = inputint(f"Quantos lugares deseja (Disponível: {vagas_na_mesa})? ")

                if 0 < quantidade <= vagas_na_mesa:
                    mesas[mesa_indice][0] -= quantidade
                    total_ocupado += quantidade
                    console.print(f"[bold green]Reserva confirmada na mesa {codigo}![/bold green]")
                else:
                    console.print(f"[bold yellow]Não foi possível. Essa mesa só tem {vagas_na_mesa} vagas.[/bold yellow]")
            else:
                console.print("[red]Código de mesa inválido![/red]")

        except ValueError:
            console.print("[red]Por favor, digite apenas números![/red]")

    console.print("\n[orange1]Sistema encerrado. Obrigado![/orange1]")

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

def questao_13():
    voos = []

    for i in range(10):
        voos.append(random.randint(1, 10))

    while True:
        console.print("\n[bright_green](1)[/bright_green] - Listar todos os voos")
        console.print("[bright_yellow](2)[/bright_yellow] - Realizar uma reserva")
        console.print("[bright_red](S)[/bright_red] - Sair")

        opcao = input("\nEscolha uma opção: ")

        if (opcao == "1"):
            console.print(f"\n[bold white on purple] VOOS DISPONÍVEIS [/bold white on purple]\n")
            console.print(f"[bright_cyan]{'Número do Voo':<15}[/bright_cyan] | [gold1]{'Lugares disponíveis':<12}[/gold1]")
            console.print("-" * 35)

            for i in range(10):
                console.print(f"[bright_white]{i + 1:<15} | {voos[i]:<12}[/bright_white]")

        elif (opcao == "2"):
            n_carteira_id_cliente = inputint("\nInforme o número da carteira de identidade: ")
            n_voo = inputint("Informe o número do voo desejado: ", min=0)

            if (voos[n_voo - 1] == 0):
                console.print(f"\n[bold red]O voo {n_voo} está lotado![/bold red]")
                continue
            
            voos[n_voo - 1] -= 1
            console.print(f"\n[gold1]Parabéns {n_carteira_id_cliente}. Voo {n_voo} reservado com sucesso![/gold1]")

        elif (opcao.upper() == "S"):
            console.print("\n[orange1]Encerrando programa...[/orange1]")
            break
        
        else:
            console.print("\n[bright_red]Opção inválida[/bright_red]")
 
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