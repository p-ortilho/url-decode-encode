import urllib.parse

from art import *

tprint("URL ENCODE/DECODE")

print("1.Encodar\n2.Decodar\n99.Sair\n")

funct = int(input("Digite um número: "))

if funct == 1:
    url = input("Digite a url ou codigo em JavaScript: ")
    encodar = urllib.parse.quote(url)
    print(encodar)
elif funct == 2:
    url = input("Digite a url JavaScript: ")
    decodar = urllib.parse.unquote(url)
    print(decodar)
elif funct == 99:
    print("Você saiu!")
    exit()
else:
    print("Entrada invalida!")
