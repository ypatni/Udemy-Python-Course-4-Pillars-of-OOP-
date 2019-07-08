class OperatingSystem:
    multitasking = True


class Apple:
    website = "www.apple.com"


class Macbook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.website))


macbook = Macbook()

#if two derived classes have the same attribute name, the new class will take the attribute from the first mentioned class
#in this case it is OperatingSystem

