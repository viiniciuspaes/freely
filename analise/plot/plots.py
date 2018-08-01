import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gerarGraficoBarras(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')

    hashtags = dataset['Hashtag'].values
    valores = dataset['Tweets'].values

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

    plt.show()


def gerarGraficoPizza(pathData):
    dataset = pd.read_csv(pathData, encoding='utf-8')

    hashtags = dataset['Hashtag'].values
    valores = dataset['Tweets'].values

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
    
    plt.show()


# gerarGraficoBarras('/home/chico/Documentos/UFRPE/projeto-bd/freely/analise/plot/testes.csv')
# gerarGraficoPizza('/home/chico/Documentos/UFRPE/projeto-bd/freely/analise/plot/testes.csv')