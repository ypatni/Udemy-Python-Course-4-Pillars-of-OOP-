class musicalInstruments:
    majorkeys = "12"


class stringInstruments (musicalInstruments):
    typeofwood = "Tone Wood"


class Guitar(stringInstruments):
    def __init__(self):
        self.numofstrings = "6"
        print("the guitar consists of {} strings, is made of {}, and plays {} keys".format(self.numofstrings, self.typeofwood, self.majorkeys))


guitar = Guitar()
