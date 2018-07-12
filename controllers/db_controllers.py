from dao.hashtag_dao import search_hashtag, insert_hashtag
from dao.location_dao import search_location, insert_location, search_location_by_id
from dao.user_dao import search_user, insert_user, search_user_by_id


def get_user(user):
    validation = search_user(user.get_username())
    if validation:
        return validation
    else:
        id = insert_user(user)
        return search_user_by_id(id)


def get_location(location):
    validation = search_location(location.get_latitude(), location.get_longitude())
    if validation:
        return validation
    else:
        id = insert_location(location)
        return search_location_by_id(id)


def add_hashtag(hash):
    h = search_hashtag(hash.get_name())
    if h:
        return h.get_id()
    else:
        return insert_hashtag(hash)
