from database.db_helper import get_session, TagTweet


def insert_relation_tweet_tag(id_hashtag, id_tweet):
    session = get_session()
    session = session()
    new_relation = TagTweet()
    new_relation.id_hashtag = id_hashtag
    new_relation.id_tweet = id_tweet
    session.add(new_relation)
    session.commit()
    session.refresh(new_relation)
    relation_id = new_relation.id
    session.close()
    return relation_id
