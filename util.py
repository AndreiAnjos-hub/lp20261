# def inputint(msg, min=None, max=None):
#     erro = True
#     while (erro == True):
#         try:
#             valor = int(input(msg))
#             if min!=None and valor < min:
#                 raise Exception(f"ERRO: Valor informado é menor do que o permitido de {min}!")
#             if max!=None and valor > max:
#                 raise Exception(f"ERRO: Valor informado é maior do que o permitido de {max}!")
#             erro = False
#             return valor
#         except ValueError:
#             print("Erro: Valor informado não é inteiro!")
#         except Exception as erro:
#             print(erro)

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
    
# def inputfloat(msg, min=None, max=None):
#     erro = True
#     while (erro == True):
#         try:
#             valor = float(input(msg))
#             if min!=None and valor < min:
#                 raise Exception(f"ERRO: Valor informado é menor do que o permitido de {min}!")
#             if max!=None and valor > max:
#                 raise Exception(f"ERRO: Valor informado é maior do que o permitido de {max}!")
#             erro = False
#             return valor
#         except ValueError:
#             print("Erro: Valor informado não é real!")
#         except Exception as erro:
#             print(erro)