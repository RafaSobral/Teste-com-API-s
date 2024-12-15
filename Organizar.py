import os #blbioteca responsavel por manipulacao de arquivos
from tkinter.filedialog import askdirectory #biblioteca responsavel pela selecao de pasta

caminho = askdirectory(title="Selecione uma pasta") #abre um pop-up para selecionar a pasta que deseja organizar

lista_arquivos = os.listdir(caminho) #lista todos os arquivos dentro da pasta selecionada

locais = { #define quais arquivos vao ficar em quais pastas
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos: #percorre a lista de arquivos
    nome, extensao = os.path.sliptext(f"{caminho}/{arquivo}") #extrai a extensao do arquivo
    for pasta in locais: #para cada pasta dentro do local
        if extensao in locais[pasta]: #verifica se a extensao existe dentro da lista "local"
            if not os.path.exists(f"{caminho}/{pasta}"): #se nao existe 
                os.mkdir(f"{caminho}/{pasta}")           #cria a pasta
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") #muda o arquivo para a nova pasta






