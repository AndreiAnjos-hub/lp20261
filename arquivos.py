# import os
# import re

# def agrupar_lista_em_um_txt(nome_arquivo_py):
#     # Verifica se o arquivo .py realmente existe na pasta
#     if not os.path.exists(nome_arquivo_py):
#         print(f"⚠️ Arquivo {nome_arquivo_py} não encontrado. Pulando...")
#         return

#     # Define o nome do arquivo de saída (ex: lista4.py -> lista4.txt)
#     nome_arquivo_txt = nome_arquivo_py.replace(".py", ".txt")

#     with open(nome_arquivo_py, "r", encoding="utf-8") as f:
#         linhas = f.readlines()

#     bloco_comentarios = []
#     codigo_funcao = []
#     capturando_funcao = False
#     nome_funcao = ""
    
#     # Regex para detectar as funções de questões (ex: def questao_1(): )
#     regex_def = re.compile(r"def\s+(questao_\d+)\s*\(")

#     # Criamos ou limpamos o arquivo txt de saída antes de começar a escrever
#     with open(nome_arquivo_txt, "w", encoding="utf-8") as f_out:
#         f_out.write("=" * 60 + "\n")
#         f_out.write(f"          ARQUIVO CONSOLIDADO: {nome_arquivo_txt.upper()}\n")
#         f_out.write("=" * 60 + "\n\n")

#     for linha in list(linhas):
#         # Captura os comentários (enunciados) que antecedem a função
#         if linha.strip().startswith("#") and not capturando_funcao:
#             bloco_comentarios.append(linha)
#             continue

#         match = regex_def.search(linha)
#         if match:
#             # Se já estávamos em uma função e achamos outra, salva a anterior primeiro
#             if capturando_funcao and nome_funcao:
#                 salvar_no_txt_unico(nome_arquivo_txt, nome_funcao, bloco_comentarios, codigo_funcao)
#                 bloco_comentarios = []
#                 codigo_funcao = []

#             capturando_funcao = True
#             nome_funcao = match.group(1)
#             codigo_funcao.append(linha)
#             continue

#         if capturando_funcao:
#             # Identifica se a função terminou (linha sem recuo que não é comentário/vazia)
#             # ou se esbarrou no menu principal (ex: e = True ou while)
#             if linha.strip() and not linha.startswith(" ") and not linha.startswith("\t") and not linha.startswith("#"):
#                 salvar_no_txt_unico(nome_arquivo_txt, nome_funcao, bloco_comentarios, codigo_funcao)
#                 bloco_comentarios = []
#                 codigo_funcao = []
#                 capturando_funcao = False
#                 nome_funcao = ""
#                 if linha.strip().startswith("#"):
#                     bloco_comentarios.append(linha)
#             else:
#                 codigo_funcao.append(linha)
#         else:
#             if not linha.strip().startswith("#") and linha.strip():
#                 bloco_comentarios = []

#     # Salva a última questão caso o arquivo termine dentro dela
#     if capturando_funcao and nome_funcao:
#         salvar_no_txt_unico(nome_arquivo_txt, nome_funcao, bloco_comentarios, codigo_funcao)
        
#     print(f"✅ Todas as questões do '{nome_arquivo_py}' foram unificadas em '{nome_arquivo_txt}'!")


# def salvar_no_txt_unico(arquivo_destino, nome_questao, enunciados, codigos):
#     # Abre no modo 'a' (append) para adicionar o conteúdo ao final do arquivo sem apagar o que já está lá
#     with open(arquivo_destino, "a", encoding="utf-8") as f:
#         f.write("\n💻 CÓDIGO FONTE:\n")
#         f.write("".join(codigos))
#         f.write("\n\n" + "_"*50 + "\n\n")


# # --- MAPEAR E RODAR EM TODAS AS LISTAS EXISTENTES ---
# # Adicione aqui o nome de todos os arquivos de lista que você possui na pasta
# arquivos_para_processar = ["lista1.py", "lista2.py", "lista3.py", "lista4.py"]

# for arquivo in arquivos_para_processar:
#     agrupar_lista_em_um_txt(arquivo)

import os
import re

def agrupar_lista_em_um_txt(nome_arquivo_py):
    if not os.path.exists(nome_arquivo_py):
        print(f"⚠️ Arquivo {nome_arquivo_py} não encontrado. Pulando...")
        return

    nome_arquivo_txt = nome_arquivo_py.replace(".py", ".txt")

    with open(nome_arquivo_py, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Cria o cabeçalho do arquivo
    with open(nome_arquivo_txt, "w", encoding="utf-8") as f_out:
        f_out.write("=" * 60 + "\n")
        f_out.write(f"          ARQUIVO CONSOLIDADO: {nome_arquivo_txt.upper()}\n")
        f_out.write("=" * 60 + "\n\n")

    # Essa Regex mágica já encontra o bloco de comentários (#) + o código completo da função
    # Ela para assim que encontra a próxima questão ou o início do menu final
    padrao_questao = re.compile(
        r"((?:^[ \t]*#.*$\n)+^[ \t]*def\s+questao_\d+\s*\(.*?\n)(?=^[ \t]*#|^e\s*=|^while)", 
        re.MULTILINE | re.DOTALL
    )

    blocos = padrao_questao.findall(conteudo)

    # Escreve cada bloco direto no arquivo .txt
    with open(nome_arquivo_txt, "a", encoding="utf-8") as f_out:
        for bloco in blocos:
            f_out.write(bloco.strip() + "\n")
            f_out.write("\n" + "_" * 50 + "\n\n")

    print(f"✅ Todas as questões do '{nome_arquivo_py}' foram unificadas em '{nome_arquivo_txt}'!")


# --- EXECUÇÃO EM MASSA ---
arquivos_para_processar = ["lista1.py", "lista2.py", "lista3.py", "lista4.py"]

for arquivo in arquivos_para_processar:
    agrupar_lista_em_um_txt(arquivo)