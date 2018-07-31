import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data
dataset = pd.read_csv('/home/chico/Documentos/UFRPE/projeto-bd/freely/analise/plot/testes.csv', encoding='utf-8')
# print(dataset.count())

hashtags = dataset['hashtag'].values
# print(type(hashtags))

valores = dataset['tweets'].values
# print(valores)

dic = {'tag' : hashtags, 'val' : valores }

teste = pd.DataFrame(data=dic)
teste.sort_values('val')
teste.set_index('tag', inplace=True)
bar = teste.plot(kind='pie', subplots=True)
# plt.show()
var = teste.to_csv('new2.csv')
# y = np.arange(len(hashtags))
# er = np.arange(1,5)

# ax.barh(y, valores, align='center',
#         color='blue', ecolor='gray')
# ax.set_yticks(y)
# ax.set_yticklabels(hashtags)
# ax.invert_yaxis()
# ax.set_xlabel('Hashtags')
# ax.set_title('Hashtags e suas quantidades coletadas')

# fig, ax = plt.subplots()
# plt.bar(hashtags, valores)

# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center',
#         color='green', ecolor='black')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()