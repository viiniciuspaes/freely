class FontObj:
    def __init__(self):
        self.id = None
        self.user = None
        self.url = None
        self.trust = False

    def is_reliable(self):
        return self.trust

    def set_reliability(self, confiability):
        self.trust = confiability

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url
