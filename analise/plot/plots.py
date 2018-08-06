import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def gerar_grafico_barras(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)

    hashtags = dataset[colunas[0]].values
    valores = dataset[colunas[1]].values

    dic = {'Nome das hashtags' : hashtags, 'Número de tweets coletados' : valores }

    df = pd.DataFrame(data=dic)
    df = df.sort_values('Número de tweets coletados', ascending=False)
    df.set_index('Nome das hashtags', inplace=True)

    ax = df.plot.bar(y='Número de tweets coletados', legend=False)
    ax.set_ylabel('quantidade absoluta')
    ax.set_xlabel('nome das hashtags')

    plt.title('Quantidade de tweets coletados por hashtag')
    plt.xticks(np.arange(0, len(hashtags), step=1), rotation=30)
    plt.subplots_adjust(top=0.926, bottom=0.195, left=0.074, right=0.981, hspace=0.2, wspace=0.2)
    plt.savefig('imagem-um.png', bbox_inches='tight')

    plt.show()


def gerar_grafico_pizza(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)

    hashtags = dataset[colunas[0]].values
    valores = dataset[colunas[1]].values

    dic = {'tags' : hashtags, 'val' : valores }

    df = pd.DataFrame(data=dic)
    df = df.sort_values('val')
    df['percent'] = (df['val'] / df['val'].sum()) * 100
    df['outros'] = df['percent'].cumsum()

    outros = df[df.percent <= 5]
    outros = outros.append({'tags': 'outros',
                             'percent': outros['percent'].sum()}, ignore_index=True)
    df = df[df.percent > 5]
    df = df[['tags', 'percent']]
    df = df.append({'tags': outros['tags'][len(outros['tags'])-1],
                     'percent': outros['percent'][len(outros['tags'])-1]}, ignore_index=True)
    df = df.sort_values('percent')

    hashtags = df['tags'].values
    valores = df['percent'].values

    labels = list(hashtags)
    vals = list(valores)

    cores = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    figura, ax = plt.subplots()
    ax.pie(vals, colors = cores, labels=labels, 
            autopct='%1.1f%%', startangle=90)

    centre_circle = plt.Circle((0,0),0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax.axis('equal')
    plt.tight_layout()
    plt.savefig('imagem-dois.png', bbox_inches='tight')
    
    plt.show()


def gerar_grafico_sentimento(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')
    colunas = list(dataset)

    hashtags = dataset[colunas[0]].values
    valores = dataset[colunas[1]].values
    pos = dataset[colunas[2]].values
    neg = dataset[colunas[3]].values
    neut = dataset[colunas[4]].values

    dic = {'val': valores, 'pos': pos, 'neg': neg, 'neut':neut}

    df = pd.DataFrame(data=dic)
    df = df.sort_values('val', ascending=False)

    ind = np.arange(len(hashtags))
    largura = 0.30

    fig, ax = plt.subplots()
    rect_um = ax.bar(ind, pos, largura, color='#ff9999')
    rect_dois = ax.bar(ind+largura, neg, largura, color='#66b3ff')
    rect_tres = ax.bar(ind-largura, neut, largura, color='#99ff99')

    ax.set_ylabel('quantidade absoluta')
    ax.set_xlabel('nome das hashtags')
    ax.legend((rect_um[0], rect_dois[0], rect_tres[0]), ('Positivo', 'Negativo', 'Neutro'))

    plt.title('Quantidade de tweets por sentimento')
    plt.xticks(np.arange(0, len(hashtags), step=1), hashtags, rotation=30)
    plt.subplots_adjust(top=0.926, bottom=0.195, left=0.074, right=0.981, hspace=0.2, wspace=0.2)
    plt.savefig('imagem-tres.png', bbox_inches='tight')

    plt.show()


gerar_grafico_barras(r'C:\Users\vinic\OneDrive\workspace\PytonProjects\freely\data.csv')
gerar_grafico_pizza(r'C:\Users\vinic\OneDrive\workspace\PytonProjects\freely\data.csv')
gerar_grafico_sentimento(r'C:\Users\vinic\OneDrive\workspace\PytonProjects\freely\data.csv')
