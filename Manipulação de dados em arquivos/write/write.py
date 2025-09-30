import os

arquivo_escrita = open("dados_write.txt", "w", encoding="utf-8")
arquivo_escrita.write("conteudo da primeira linha")
arquivo_escrita.write("\nconteudo da segunda linha")

print("O caminho:", os.path.realpath("dados_write.txt"))

arquivo_escrita.close()


