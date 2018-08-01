from database.db_helper import get_session, User, get_engine
from models.user import UserObj


def insert_user(user_obj):
    session = get_session()
    session = session()
    new_user = User()
    new_user.username = user_obj.get_username()
    new_user.id_location = user_obj.get_location()
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    user_id = new_user.id
    session.close()
    return user_id


def search_user(username):
    session = get_session()
    session = session()
    user_query = session.query(User).filter(User.username == username).all()
    if user_query:
        user_query = user_query[0]
        user_obj = UserObj(user_query.username)
        user_obj.set_id(user_query.id)
        session.close()
        return user_obj
    else:
        session.close()
        return None

def search_user_by_id(id):
    session = get_session()
    session = session()
    user_query = session.query(User).filter(User.id == id).all()
    if user_query:
        user_query = user_query[0]
        user_obj = UserObj(user_query.username)
        user_obj.set_id(user_query.id)
        session.close()
        return user_obj
    else:
        session.close()
        return None


def create_users():
    con = get_engine()
    rs = con.execute("""insert into user(username) values
  ("roxmo"),
  ("DaniloGentili"),
  ("Jornalivre_BR"),
  ("brasilpensa"),
  ("diariodobrasil"),
  ("epoca"),
  ("catracalivre"),
  ("diplomatique"),
  ("piaui"),
  ("superinteressante"),
  ("uol"),
  ("ne10"),
  ("r7"),
  ("bbc"),
  ("cartacapital"),
  ("diariodepernambuco"),
  ("estadao"),
  ("folha"),
  ("jornaldocomercio"),
  ("elpais"),
  ("exame"),
  ("veja"),
  ("g1"),
  ("istoe"),
  ("oglobo"),
  ("terra"),
  ("JornalistasLivres"),
  ("VejaSP"),
  ("VejaRJ"),
  ("sensacionalista"),
  ("mblivre");""")
