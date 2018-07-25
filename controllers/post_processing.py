# coding: utf-8
import re

import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
from traceback import print_tb, extract_tb, format_list

from analise.analisys_test import analize
from controllers.db_controllers import get_location, get_user, add_hashtag
from dao.feeling_dao import search_feeling
from dao.hashtag_dao import insert_hashtag
from dao.tweet_dao import insert_tweet
from dao.tweet_hash_dao import insert_relation_tweet_tag
from models.hashtag import HashTagObj
from models.location import LocationObj
from models.tweet import TweetObj
from models.user import UserObj
from dao.user_dao import insert_user, search_user
from utils.location_utils import search_location_by_name
from utils.text_utils import remove_emoji, strip_all_entities


def printError():
    error = sys.exc_info()
    type = error[0]#tipo do erro
    print('\n'+'Type: \n'+str(type)+'\n')
    value = error[1] # valor do erro
    print('Value: \n'+str(error[1])+'\n')
    tb=error[2]
    print('Traceback:')
    e_tb=extract_tb(tb)
    f_l=format_list(e_tb)#traceback em forma de lista para futuro usos
    print_tb(tb)


def get_tweets(hashtag):
    arquivo = open('controllers/{}.txt'.format(hashtag),'r')
    lista=arquivo.read().split()
    lista1=[]
    for x in range (len(lista)):
        if x%2==0:
            lista1.append(lista[x])


    cwd = os.getcwd()
    auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
    auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
    api = tweepy.API(auth)

    for x in lista1:
        print(x)
        try:
            tweet = api.get_status(x , tweet_mode='extended')
            hashtags = tweet.entities["hashtags"]
            nomeUsuario = tweet.user.screen_name#nick fixo
            location = tweet.user.location
            followersUsuario = tweet.user.followers_count
            totalTweetsUsuario = tweet.user.statuses_count #SERÁ NECESSARIO?
            textoTweet = tweet.full_text
            tweetDate = tweet.created_at
            retweetCount = tweet.retweet_count
            likes = tweet.favorite_count

            location_name = search_location_by_name(location)
            if location_name:
                location_obj = LocationObj(location_name[0])
                location_obj.set_latitude(location_name[1])
                location_obj.set_longitude(location_name[2])
                location_obj = get_location(location_obj)
                location_id = location_obj.get_id()
            else:
                location_id = None

            user_obj = UserObj(nomeUsuario)
            user_id = get_user(user_obj).get_id()

            feeling = analize(textoTweet)
            id_feeling = search_feeling(list(feeling)[0])[1]
            # print(feeling)

            regex_link = "(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?\S"
            textoTweet = re.sub(regex_link, "", textoTweet)


            textoTweet = remove_emoji(textoTweet)

            textoTweet = strip_all_entities(textoTweet)

            tweet_obj = TweetObj(textoTweet)
            tweet_obj.set_number_likes(likes)
            tweet_obj.set_location(location_id)
            tweet_obj.set_user(user_id)
            tweet_obj.set_number_retweet(retweetCount)
            tweet_obj.set_feeling(id_feeling)

            id_tweet = insert_tweet(tweet_obj)

            for hash in hashtags:
                h = HashTagObj(hash["text"])
                hash_id = add_hashtag(h)
                insert_relation_tweet_tag(hash_id, id_tweet)




            print("------------------------------------------------------------")
            print(nomeUsuario)
            print("hash",hashtags)
            print("localizacao",location)
            print("followers",followersUsuario)
            print("totalTweets",totalTweetsUsuario)
            print("texto",textoTweet)
            print("retweet",retweetCount)
            print("likes",likes)
            print("feeling:",feeling)
            print("----------------------------------- NEW TWEET -------------------------")

        except:
            printError()
get_tweets("LulaLivre")