from database.db_helper import get_session, HashTag
from models.hashtag import HashTagObj


def insert_hashtag(hashtag_obj):
    session = get_session()
    session = session()
    new_hashtag = HashTag()
    new_hashtag.name = hashtag_obj.get_name()
    session.add(new_hashtag)
    session.commit()
    session.refresh(new_hashtag)
    hashtag_id = new_hashtag.id
    session.close()
    return hashtag_id


def search_hashtag(hashtag):
    session = get_session()
    session = session()
    tag_query = session.query(HashTag).filter(HashTag.name == hashtag).all()
    if tag_query:
        tag_query = tag_query[0]
        tag_obj = HashTagObj(tag_query.name)
        tag_obj.set_id(tag_query.id)
        session.close()
        return tag_obj
    else:
        session.close()
        return None
