from geopy.geocoders import Nominatim


def search_location_by_name(name):
    geolocator = Nominatim(user_agent="geopy=1.15.0")
    geo_location = geolocator.geocode(name)
    return [geo_location.address, geo_location.latitude, geo_location.longitude] if geo_location else None


def search_location_by_coordinate(lat,long):
    geolocator = Nominatim()
    geo_location = geolocator.reverse("{}, {}".format(lat, long))
    return [geo_location.address, geo_location.latitude, geo_location.longitude] if geo_location else None
