#OBS: os arquivos serão mesclados na ordem que estiverem dispostos na pasta!!!!!

import PyPDF2                                #importa a biblioteca apos intalar com o pip
import os                                    #blbioteca responsavel por manipulacao de arquivos

merger =  PyPDF2.PdfMerger()                 #criando a ferramenta pra juntar os pdf's

lista_arquivos = os.listdir("arquivos")      #lista os arquivos que estao dentro do diretorio "arquivos"

for arquivo in lista_arquivos:               #percorre a lista de arquivos
    if ".pdf" in arquivo:                    #verifica se o formato do arquivo eh pdf
        merger.append(f"arquivos/{arquivo}") #cria um nome dinamico para os arquivos e junta eles

merger.write("teste.pdf")                    #salva o pdf final 