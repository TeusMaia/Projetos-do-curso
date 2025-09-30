import os
arquivo = open("exemplo_bd.docx", "r", encoding='utf-8')

print ("Conteudo retornado pelo readlines usando for")
for linha in arquivo:
    print(repr(linha),)

arquivo.close()


reaberturaarquivo1 = open ("exemplo_bd.docx", "r", encoding='utf-8')

conteudo = reaberturaarquivo1.read()
 
print("Conteudo retornado pelo readlines")
print(repr(conteudo),)

reaberturaarquivo1.seek(8)
couteudo_seek = reaberturaarquivo1.read()
print("Conteudo retornado pelo read apos o seek")
print(repr(couteudo_seek))

reaberturaarquivo1.close()