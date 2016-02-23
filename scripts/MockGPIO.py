

class MockGPIO(object):
    """Class for getting mocking the behaviour of the GPIO"""

    def HIGH(self):
        return True

    def LOW(self):
        return False

    def BOARD(self):
        return True

    def OUT(self):
        return True

    def setmode(self, GPIO_BOARD):
        pass

    def setup(self, pin, GPIO_OUT):
        pass

    def output(self, pin, status):
        return status

    def cleanup(self):
        pass

    def input(self, pin):
        return True


