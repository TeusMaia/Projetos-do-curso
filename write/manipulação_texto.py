def main ():
    print("digite as frases. Digite 'sair' para encerrar")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == 'sair':
            break
        frases.append(entrada)

    with open('dados_writelines.txt', 'w', encoding='utf-8') as arquivo:
        for frase in frases:
            arquivo.write(frase + '\n')

    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open('dados_writelines.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper()) # Exemplo de manipulação: converter para maiúsculas

    with open("dados_writelines.txt", 'w', encoding='utf-8') as arquivo:
        for linha in dados_modificados:
         arquivo.write(linha + '\n')
    
    print("Manipulação concluída. Dados salvos no arquivo.")

if __name__ == "__main__":
    main()

