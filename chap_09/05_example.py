# Initialze the constructor
class Country():
    def __init__(self):
        print("Intializing country....")
class State(Country):
    def __init__(self):
        super().__init__()
        print("Initializing State...")
class Distict(State):
    def __init__(self):
        super().__init__()
        print("Tere nazarone dilko ")
obj = Distict()