import requests
import json
import pandas as pd
import decimal


def exportar_csv(cat, tit, lin, hor, nome):
        df = pd.DataFrame({'Categoria': cat, 'Título': tit, 'Link': lin, 'Hora': hor})
        df.to_csv("%s.csv" % nome, index=False, sep=";", encoding='utf-8-sig')
        print("")
        print("Arquivo *.csv exportado com sucesso, para a pasta do projeto!")   
        print("")


def buscar_tudo(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            categoria.append(posicao['pillarName'])
            hora.append(posicao['webPublicationDate'])
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
        exportar_csv(categoria, titulo, link, hora,"Tudo")    


def buscar_opinion(dados):
        categoria = []     
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Opinion':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Opiniões neste momento. Tente mais tarde, por favor!")
            print("")
        else:
            exportar_csv(categoria, titulo, link, hora,"Opinião")


def buscar_sport(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Sport':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Esportes neste momento. Tente mais tarde, por favor!")
            print("")
        else:   
            exportar_csv(categoria, titulo, link, hora,"Esportes")    


def buscar_news(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'News':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre News neste momento. Tente mais tarde, por favor!")
            print("")
        else:
            exportar_csv(categoria, titulo, link, hora,"Notícias")


def buscar_arts(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Arts':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Artes neste momento. Tente mais tarde, por favor!")
            print("")
        else:
            exportar_csv(categoria, titulo, link, hora,"Artes")

def buscar_plot(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            categoria.append(posicao['pillarName'])
            hora.append(posicao['webPublicationDate'])
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    
            print("Categoria:", posicao['pillarName'])
            print("Hora:", posicao['webPublicationDate'])
            print("Título:", posicao['webTitle'])
            print("Link: ", posicao['webUrl'])
            print("---------------------")
            print("")




def main():
    # THE GUARDIAN
    # Objetivo: criação um programa que consume a API do jornal The Guardian, mostrando o título e o link das notícas do dia: https://open-plataform.theguardian.com/ tomando cuidado para o email de informação da API não ir para a caixa de spam

    print("")
    print("")
    print("### THE GUARDIAN ###")
    print("")

    url = "https://content.guardianapis.com/search?api-key=781f8c4e-ce6d-4c05-a546-38c28353b9ce"

    response = requests.get(url)

    if response.status_code == 200:
        
        print("Acessando base de dados do The Guardian...")
        print("")
        print("NOTÍCIAS RECENTES:")
        print("---------------------")
        print("")
        dados = response.json()
        

        escolha = 4
        while escolha != 0:
            print("1 = Opinião")
            print("2 = Esportes")
            print("3 = Notícias")
            print("4 = Artes")
            print("5 = Tudo")
            print("6 = Plotar aqui")
            print("0 = Para SAIR")
            print("")
        
            try:
                escolha = int(input("Digite o número referente à notícia que deseja baixar arquivo: "))
                print("")
            except:
                print("Por favor, digite apenas números...")
                print("")
            if escolha > 6 or escolha < 0:
                print("Por favor digite números entre 0 e 4")
                print("")
            elif escolha == 1:
                buscar_opinion(dados)
            elif escolha == 2:
                buscar_sport(dados)
            elif escolha == 3:
                buscar_news(dados)
            elif escolha == 4:
                buscar_arts(dados)
            elif escolha == 5:
                buscar_tudo(dados)
            elif escolha == 6:
                buscar_plot(dados)
            elif escolha == 0:
                print("")
                print("Obrigado por utilizar o programa.")
                print("")
             
    else:
        print("Não foi possível acessar a base de dados do The Guardian!")
        print("")

if __name__ == "__main__":
    main()

print("F I M  !!!")  