import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('/home/chico/Documentos/UFRPE/projeto-bd/freely/analise/plot/testes.csv', encoding='utf-8')

hashtags = dataset['Hashtag'].values
valores = dataset['Tweets'].values

dic = {'tags' : hashtags, 'val' : valores }

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

# plotGraficoBarras('/home/chico/Documentos/UFRPE/projeto-bd/freely/analise/plot/testes.csv')

df = pd.Series.to_frame(dataset['Hashtag'].value_counts())
print(df)
# df.set_index('tags', inplace=True)
# ax = df.plot.pie(subplots=True, autopct='%1.1f%%', legend=False, figsize=(8, 8))
# plt.show()

labels = list(hashtags)
vals = list(valores)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

fig1, ax1 = plt.subplots()

ax1.pie(vals, colors = colors, labels=labels, 
        autopct='%1.1f%%', startangle=90)

centre_circle = plt.Circle((0,0),0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax1.axis('equal')
plt.tight_layout()
# plt.show()