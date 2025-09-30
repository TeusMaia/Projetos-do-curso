import os
arquivo1 = open ("exemplo_bd.docx", "r", encoding='utf-8')

conteudo = arquivo1.read()
print("conteudo retornado pelo read")
print(repr(conteudo))


arquivo1.close()    
