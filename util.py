import random

def inputint(msg, min=None, max=None):
    while True: 
        try:
            valor = int(input(msg))
            
            if min is not None and valor < min:
                print(f"ERRO: O valor {valor} é menor que o permitido ({min})!")
                continue 
            
            if max is not None and valor > max:
                print(f"ERRO: O valor {valor} é maior que o permitido ({max})!")
                continue 
            
            return valor
            
        except ValueError:
            print("ERRO: Valor informado não é um número inteiro!")


def inputfloat(msg, min=None, max=None):
    while True: 
        try:
            valor = float(input(msg))
            
            if min is not None and valor < min:
                print(f"ERRO: O valor {valor} é menor que o permitido ({min})!")
                continue 
            
            if max is not None and valor > max:
                print(f"ERRO: O valor {valor} é maior que o permitido ({max})!")
                continue 
            
            return valor
            
        except ValueError:
            print("ERRO: Valor informado não é um número inteiro!")


def gerar_palavra(min=4, max=10):
    qnt_letras = random.randrange(min,max+1)
    palavra = ""
    for _ in range(random.randrange(qnt_letras)):
        palavra += chr(random.randrange(65, 91))
    return palavra
