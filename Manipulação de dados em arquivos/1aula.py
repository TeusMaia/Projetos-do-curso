import os

#abrindo os arquivos em modo de escrita
arquivo1 = open ("exemplo_bd.docx", "w", encoding='utf-8')

#exibindo os atributos do arquivo
print("nome do arquivo:", arquivo1.name)
print("modo de abertura:", arquivo1.mode)
print("O arquivo está fechado?", arquivo1.closed)
print(os.path.abspath(arquivo1.name))

#escrevendo no arquivo
arquivo1.write("Olá mundo!")

#fechando o arquivo 
arquivo1.close()

#verificando o fechamento do arquivo
print("O arquivo está fechado?", arquivo1.closed)


#exibindo o caminho absoluto e relativo do arquivo
relpath = os.path.relpath(arquivo1.name)
abspath = os.path.abspath(arquivo1.name)
print(relpath)
print(abspath)
print(arquivo1)

