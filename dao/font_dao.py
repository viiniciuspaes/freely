from database.db_helper import get_session, Font, get_engine
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


def create_fonts():
    con = get_engine()
    rs = con.execute("""insert into font(id_user, url, trust) VALUE
  (1, null, FALSE),
  (2, null, FALSE),
  (3, "https://jornalivre.com", FALSE),
  (4, "https://pensabrasil.com", FALSE),
  (5, "https://www.diariodobrasil.org", FALSE),
  (6, "https://epoca.globo.com/", TRUE),
  (7, "https://catracalivre.com.br/", TRUE),
  (8, "https://diplomatique.org.br/", TRUE),
  (9, "https://piaui.folha.uol.com.br/", TRUE),
  (10, "https://super.abril.com.br/", TRUE ),
  (11, "https://www.uol.com.br/", TRUE ),
  (12, "https://ne10.uol.com.br/", TRUE),
  (13, "https://www.r7.com/", TRUE),
  (14, "https://www.bbc.com/portuguese/brasil", TRUE),
  (15, "https://www.cartacapital.com.br/", TRUE),
  (16, "https://www.diariodepernambuco.com.br", TRUE),
  (17, "https://www.estadao.com.br/", TRUE),
  (18, "https://www.folha.uol.com.br/", TRUE),
  (19, "https://www.jornaldocomercio.com/", TRUE),
  (20, "https://brasil.elpais.com/", FALSE ),
  (21, "https://exame.abril.com.br", TRUE),
  (22, "https://veja.abril.com.br/", TRUE),
  (23, "https://g1.globo.com/", TRUE),
  (24, "https://istoe.com.br/",TRUE),
  (25, "https://oglobo.globo.com/", TRUE),
  (26, "https://www.terra.com.br/", TRUE),
  (27, null, TRUE),
  (28, null, TRUE),
  (29, null, TRUE),
  (30,"https://www.sensacionalista.com.br", FALSE ),
  (31, "http://mbl.org.br", FALSE ); """)
