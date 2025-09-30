print ("Iterando sobre o arquivo")

with open("dados_write.txt", "r") as arquivo:
    for linha in arquivo:
        print(repr(linha))

        print("fim do arquivo", arquivo.name)