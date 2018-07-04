from database.db_helper import get_session, Feeling


def insert_feeling(feeling):
    session = get_session()
    session = session()
    new_feeling = Feeling()
    new_feeling.username = feeling
    session.add(new_feeling)
    session.commit()
    session.refresh(new_feeling)
    feeling_id = new_feeling.id
    session.close()
    return feeling_id


def search_feeling(feeling):
    session = get_session()
    session = session()
    feeling_query = session.query(Feeling).filter(Feeling.name == feeling).all()
    if feeling_query:
        feeling_query = feeling_query[0]
        feeling = bool(feeling_query.name)
        session.close()
        return feeling
    else:
        session.close()
        return None


def create_feelings():
    feelings = ["positive", "neutral", "negative"]
    for feel in feelings:
        if not search_feeling(feel):
            tag = insert_feeling(feel)
            if not tag:
                print("DB ERROR insert feeling: "+feel)
                break
