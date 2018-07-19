from database.db_helper import get_session, Feeling


def insert_feeling(name):
    session = get_session()
    session = session()
    new_feeling = Feeling()
    print("------------------------------------------", name)
    new_feeling.name = name
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
        n_feeling = feeling_query.name, feeling_query.id
        session.close()
        return n_feeling
    else:
        session.close()
        return None


def create_feelings():
    feelings = ['Positivo', 'Negativo', 'Neutro']
    for feel in feelings:
        if not search_feeling(feel):
            print("-----------------------------------------------------------------", feel)
            tag = insert_feeling(feel)
            if not tag:
                print("DB ERROR insert feeling: "+feel)
