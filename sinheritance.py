class Apple:
    maunfacturer = "Apple Inc"
    contactwebsite = "www.apple.com"

    def contactDetails(self):
        print("To contact use, go to", self.contactwebsite)


class Macbook(Apple):
    def __init__(self):
        self.yearofman = "2017"

    def mandetails(self):
        print("this was manufactured in the year {} by {} ".format(self.yearofman, self.maunfacturer))

        # Python checks if attribute is instance and then checks if it is a class attribute and then checks base class (apple)
# create object for MAcbook not Apple


macbook = Macbook()
macbook.mandetails()
macbook.contactDetails()
