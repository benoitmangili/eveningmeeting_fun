import pyttsx

class Speaker():

    def __init__(self):
        self.engine = pyttsx.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 130)
        self.engine.setProperty('voice', 'english')

    def say(self, text_to_speak):
        self.engine.say(text_to_speak)
        self.engine.runAndWait()


