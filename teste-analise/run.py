import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

# instâncias de teste
testes = ['Esse governo está no início, vamos ver o que vai dar',
          'Estou muito feliz com o governo de Minas esse ano',
          'Penso em destruir esse país por inteiro, essa merda',
          'Eu quero que Lula se foda, esse merda',
          'Minha família ama o PT, eu não',
          'Vão todos se fuder!',
          'Eu amo o Moro, quero casar com ele',
          'Gosto do Bolsonaro, ele é um gênio',
          'O estado de Minas Gerais decretou calamidade financeira!!!',
          'A segurança desse país está deixando a desejar',
          'O governador de Minas é do PT',
          'Eu adoro este governo, ele está indo muito bem']

sentimento = ['Positivo', 'Negativo', 'Neutro']

# leitura do csv base, pode ser uma lista
dataset = pd.read_csv('tweets_tests.csv', encoding='utf-8')

# visualização das colunas e seus values, para isso tire o comentário
# print(dataset.count())

# instâncias com os textos dos tweets e seus sentimentos classificados
tweets = dataset['Text'].values
print(tweets)
classes = dataset['Classificacao'].values
print(classes)

# objeto responsável pela criação do bag of words e sua contagem
# vectorizer = CountVectorizer(analyzer="word")

# usando bigrams
vectorizer = CountVectorizer(ngram_range=(1, 2))

# preenchimento do objeto
freq_tweets = vectorizer.fit_transform(tweets)

# objeto responsável pelo treinamento e usado como modelo
modelo = MultinomialNB()
modelo.fit(freq_tweets, classes)

# inicio dos testes a partir do modelo
freq_testes = vectorizer.transform(testes)

# classificação com o modelo treinado
print(modelo.predict(freq_testes))

# cross validation
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

print(metrics.accuracy_score(classes, resultados))

# medindo a acurácia média
print(metrics.classification_report(classes, resultados, sentimento), '')

# matriz de visualização
print(pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True), '')
