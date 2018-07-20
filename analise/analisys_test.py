from analise.fit_test import vectorizer, modelo

"""instâncias de teste"""

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



# inicio dos testes a partir do modelo
def analize(tweet_text):
    freq_testes = vectorizer.transform([tweet_text])
    return modelo.predict(freq_testes)
# classificação com o modelo treinado


