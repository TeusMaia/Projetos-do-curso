import os
linhas = ["conteudo da primeira linha", "\n conteudo da segunda linha"]

with open("dados_writelines.txt", "w") as arquivo_escrita:
    
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()