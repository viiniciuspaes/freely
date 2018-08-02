class TweetObj:
    def __init__(self, text):
        self.text = text
        self.id = None
        self.id_user = None
        self.id_hashtag = None
        self.id_location = None
        self.id_feeling = None
        self.id_font = None
        self.n_reply = None
        self.n_retweets = None
        self.n_likes = None
        self.date = None
        self.reliable = True

    def set_user(self, user):
        self.id_user = user

    def get_user(self):
        return self.id_user

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_location(self, locatino):
        self.id_location = locatino

    def get_location(self):
        return self.id_location

    def set_feeling(self, feeling):
        self.id_feeling = feeling

    def get_feeling(self):
        return self.id_feeling

    def set_font(self, font):
        self.id_font = font

    def get_font(self):
        return self.id_font

    def set_hasstag(self, hashtag):
        self.id_hashtag = hashtag

    def get_hashtag(self):
        return self.id_hashtag

    def set_number_likes(self, number):
        self.n_likes = number

    def number_likes(self):
        return self.n_likes

    def set_number_reply(self, number):
        self.n_reply = number

    def number_reply(self):
        return self.n_reply

    def set_number_retweet(self, number):
        self.n_retweets = number

    def number_retweet(self):
        return self.n_retweets

    def set_data(self, data):
        self.date = data

    def get_data(self):
        return self.date

    def set_reliability(self, bool):
        self.reliable = bool

    def is_reliable(self):
        return self.reliable