import os 
arquivo = open ("exemplo_bd.docx", "r", encoding = 'utf-8;')

conteudo = arquivo.readline()

print("conteudo retornado pelo readline")
print(repr(conteudo))


proxima_linha = arquivo.readline()
print("proxima linha retornada pelo readline")  
print(repr(proxima_linha))


arquivo.close()