# coding: utf-8
import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
from traceback import print_tb, extract_tb, format_list
from models.user import UserObj
from dao.user_dao import insert_user, search_user


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

arquivo = open('pratodagalera.txt','r')
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
        hashtags=tweet.entities["hashtags"]
        nomeUsuario = tweet.user.screen_name#nick fixo
        location = tweet.user.location
        followersUsuario = tweet.user.followers_count
        totalTweetsUsuario = tweet.user.statuses_count #SERÁ NECESSARIO?
        textoTweet = tweet.full_text
        tweetDate = tweet.created_at
        retweetCount = tweet.retweet_count
        likes = tweet.favorite_count
        print(nomeUsuario)
        print("hash",hashtags)
        print("localizacao",location)
        print("followers",followersUsuario)
        print("totalTweets",totalTweetsUsuario)
        print("texto",textoTweet)
        print("retweet",retweetCount)
        print("likes",likes)

    except:
        printError()
