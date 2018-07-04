from database.db_helper import get_session, Font
from models.font import FontObj


def insert_font(font_obj):
    session = get_session()
    session = session()
    new_font = Font()
    new_font.id_user = font_obj.get_user()
    new_font.url = font_obj.get_url()
    new_font.trust = font_obj.is_reliable()
    session.add(new_font)
    session.commit()
    session.refresh(new_font)
    font_id = new_font.id
    session.close()
    return font_id


def search_font(font_obj):
    session = get_session()
    session = session()
    font_query = session.query(Font).filter(Font.url == font_obj.get_url() or
                                            Font.id_user == font_obj.get_user()).all()
    if font_query:
        font_query = font_query[0]
        font_obj = FontObj()
        font_obj.set_id(font_query.id)
        font_obj.set_reliability(font_query.trust)
        font_obj.set_user(font_query.id_user)
        font_obj.set_url(font_query.url)
        session.close()
        return font_obj
    else:
        session.close()
        return None
