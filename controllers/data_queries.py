import csv
from collections import OrderedDict

from dao.hashtag_dao import search_hashtag_by_id
from dao.tweet_dao import n_tweets_feeling
from dao.tweet_hash_dao import n_tweets_hash


def save_data(data):
    with open('data.csv', 'w', newline='') as new_file:
        fieldnames = ['Hashtag', 'Tweets', 'Positivo', 'Negativo', 'Neutro']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writerow({'Hashtag': 'Hashtag','Tweets': 'Tweets', 'Positivo': 'Positivo', 'Negativo': 'Negativo', 'Neutro': 'Neutro'})

        for x in data:
            csv_writer.writerow({'Hashtag': x[0],'Tweets': x[1], 'Positivo': x[2], 'Negativo': x[3], 'Neutro': x[4]})


def get_data():
    arq = open('hashtags.txt', 'r')
    lines = arq.readlines()
    output = []
        for hash in lines:
        hash = hash.replace("\n", "")
        id_hash = search_hashtag(id_hash).get_id()
        n_tweets = n_tweets_hash(id_hash)
        positive_tweets = n_tweets_feeling(1, id_hash)
        neg_tweets = n_tweets_feeling(2, id_hash)
        neutral_tweets = n_tweets_feeling(3, id_hash)

        line = [str(hash), int(n_tweets), int(positive_tweets), int(neg_tweets), int(neutral_tweets)]
        output.append(line)

    arq.close()
    return output


