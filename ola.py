from rich.console import Console

console = Console()

def diga_ola():
    nome = input("\nDigite seu nome: ")
    console.print (f"\n[blue]Olá {nome}, seja bem-vindo(a)![/blue]")
    
    idade = int(input("\nDigite sua idade: "))
    console.print (f"\n[yellow]Perfeito {nome}. Você tem {idade} anos.[/yellow]\n")

diga_ola()