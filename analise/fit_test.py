import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

sentimento = ['Positivo', 'Negativo', 'Neutro']


"""leitura do csv base, pode ser uma lista"""
dataset = pd.read_csv('tweets_base.csv', encoding='utf-8')


"""visualização das colunas e seus values, para isso tire o comentário"""
# print(dataset.count())

"""instâncias com os textos dos tweets e seus sentimentos classificados"""

tweets = dataset['Text'].values
array_text = list(tweets)
classes = dataset['Classificacao'].values
array_class = list(classes)

"""
Vectorizer é o objeto responsável pela criação do bag of words e sua contagem
essa contagem pode ser feita somente através de palavras passando como argumento
o termo 'analyzer="word"' para o objeto. Neste momentousando bigrams, um agrupamento
de palavras, de 1 a 2 palavras consecutivas.
"""

vectorizer = CountVectorizer(ngram_range=(1, 2))

"""preenchimento do objeto"""

freq_tweets = vectorizer.fit_transform(array_text)

"""objeto responsável pelo treinamento e usado como modelo"""

modelo = MultinomialNB()
modelo.fit(freq_tweets, array_class)

"""cross validation"""

resultados = cross_val_predict(modelo, freq_tweets, array_class, cv=10)

"""precisão do modelo"""

print("Prediction:")
print(metrics.accuracy_score(array_class, resultados))
print("\n")

"""acurácia média e matriz de representação"""

print("Accuracy: ")
print(metrics.classification_report(array_class, resultados, sentimento))
print("\n")

# erro nessa matriz da confusão, ainda não resolvido
# print(pd.crosstab(array_class, resultados, rownames=['Real'], colnames=['Predito'], margins=True))
