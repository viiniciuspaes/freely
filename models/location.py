class LocationObj:
    def __init__(self, name):
        self.name =  name
        self.latitude = None
        self.longitude = None
        self.id = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
