class Button:
    def __init__(self, name):
        self.__ispressed = False
        self._name = name

    def press(self, Snek):
        if Snek.interact():
            self.__ispressed = True

    def timeout(self):
        # If the button is pressed, it will be unpressed after 3 seconds
        if self.__ispressed:
            # there needs to be code here that keeps track of when 3 seconds pass, but I don't know how to do that
            self.__ispressed = False
