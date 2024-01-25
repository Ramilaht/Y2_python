# Simple class to describe a trick
class Trick:
    def __init__(self, name):
        self.trick_name = name

    def get_name(self):
        return self.trick_name

    def __str__(self):
        return "The dog can " + self.trick_name