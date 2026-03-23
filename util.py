def inputint(msg, min=None, max=None):
    erro = True
    while (erro == True):
        try:
            valor = int(input(msg))
            if min!=None and valor < min:
                raise Exception(f"ERRO: Valor informado é menor do que o permitido de {min}!")
            if max!=None and valor > max:
                raise Exception(f"ERRO: Valor informado é maior do que o permitido de {max}!")
            erro = False
            return valor
        except ValueError:
            print("Erro: Valor informado não é inteiro!")
        except Exception as erro:
            print(erro)
    
def inputfloat(msg, min=None, max=None):
    erro = True
    while (erro == True):
        try:
            valor = float(input(msg))
            if min!=None and valor < min:
                raise Exception(f"ERRO: Valor informado é menor do que o permitido de {min}!")
            if max!=None and valor > max:
                raise Exception(f"ERRO: Valor informado é maior do que o permitido de {max}!")
            erro = False
            return valor
        except ValueError:
            print("Erro: Valor informado não é real!")
        except Exception as erro:
            print(erro)