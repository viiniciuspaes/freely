class UserObj:
    def __init__(self, username):
        self.username = username
        self.id = None
        self.location = None

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location
