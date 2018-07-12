from database.db_helper import get_session, Location
from models.location import LocationObj


def insert_location(location_obj):
    session = get_session()
    session = session()
    new_location = Location()
    new_location.name = location_obj.get_name()
    new_location.latitude = location_obj.get_latitude()
    new_location.longitude = location_obj.get_longitude()
    session.add(new_location)
    session.commit()
    session.refresh(new_location)
    location_id = new_location.id
    session.close()
    return location_id


def search_location(latitude, longitude):
    session = get_session()
    session = session()
    location_query = session.query(Location).filter(Location.latitude == latitude and
                                               Location.longitude == longitude).all()
    if location_query:
        location_query = location_query[0]
        location_obj = LocationObj(location_query.name)
        location_obj.set_id(location_query.id)
        location_obj.set_latitude(location_query.latitude)
        location_obj.set_longitude(location_query.longitude)
        session.close()
        return location_obj
    else:
        session.close()
        return None


def search_location_by_id(id):
    session = get_session()
    session = session()
    location_query = session.query(Location).filter(Location.id == id ).all()
    if location_query:
        location_query = location_query[0]
        location_obj = LocationObj(location_query.name)
        location_obj.set_id(location_query.id)
        location_obj.set_latitude(location_query.latitude)
        location_obj.set_longitude(location_query.longitude)
        session.close()
        return location_obj
    else:
        session.close()
        return None
