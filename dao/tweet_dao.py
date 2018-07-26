from database.db_helper import get_session, Tweet


def insert_tweet(tweet_obj):
    session = get_session()
    session = session()
    new_tweet = Tweet()
    new_tweet.text = tweet_obj.get_text()
    new_tweet.id_user = tweet_obj.get_user()
    new_tweet.id_location = tweet_obj.get_location()
    new_tweet.id_feeling = tweet_obj.get_feeling()
    new_tweet.id_font = tweet_obj.get_font()
    new_tweet.id_hashtag = tweet_obj.get_hashtag()
    new_tweet.n_likes = tweet_obj.number_likes()
    new_tweet.n_reply = tweet_obj.number_reply()
    new_tweet.n_retweets = tweet_obj.number_retweet()
    new_tweet.data = tweet_obj.get_data()
    new_tweet.fake = tweet_obj.is_reliable()
    session.add(new_tweet)
    session.commit()
    session.refresh(new_tweet)
    tweet_id = new_tweet.id
    session.close()
    return tweet_id
