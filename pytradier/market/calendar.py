class Calendar:
    def __init__(self, month=None, year=None):
        self.__payload = {}


        if month is not None:
            self.__payload['month'] = month

        if year is not None:
            self.__payload['year'] = year


        print(self.__payload)


    def month(self):
        pass

    def year(self):
        pass

    def date(self):
        pass

    def status(self):
        pass

    def desc(self):
        pass

    def premarket(self):
        pass

    def open(self):
        pass

    def postmarket(self):
        pass

    def start(self):
        pass

    def end(self):
        pass