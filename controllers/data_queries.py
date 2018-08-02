import csv
from collections import OrderedDict

from dao.hashtag_dao import search_hashtag_by_id
from dao.tweet_dao import n_tweets_feeling
from dao.tweet_hash_dao import n_tweets_hash


def save_data(data):
    with open('data.csv', 'w') as new_file:
        fieldnames = ['Hashtag', 'Tweets', 'Positivo', 'Negativo', 'Neutro']

        csv_writer = csv.writer(new_file, delimiter=',')

        csv_writer.writerow('Hashtag' + "," + 'Tweets' + " ," + 'Positivo' + "," + 'Negativo' + "," + 'Neutro')
        for x in data:
            csv_writer.writerow(x)


def get_data():
    arq = open('hashtags.txt', 'r')
    lines = arq.readlines()
    output = []
    for n in range(1,len(lines)+1):
        n_tweets = n_tweets_hash(n)
        positive_tweets = n_tweets_feeling(1, n)
        neg_tweets = n_tweets_feeling(2, n)
        neutral_tweets = n_tweets_feeling(3, n)
        hash_name = search_hashtag_by_id(n)

        line = str(hash_name) + "," + str(n_tweets) + "," + str(positive_tweets) + "," + str(neg_tweets) + "," + str(neutral_tweets)
        output.append(line)

    arq.close()
    return output


