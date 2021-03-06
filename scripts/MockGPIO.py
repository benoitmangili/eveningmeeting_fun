

class MockGPIO(object):
    """Class for getting mocking the behaviour of the GPIO"""

    def __init__( self ):
        self.pin_state = dict()
        self._HIGH=True
        self._LOW=False

    @property
    def HIGH(self):
        return self._HIGH
    @property
    def LOW(self):
        return self._LOW

    def BOARD(self):
        return True

    def OUT(self):
        return True

    def setmode(self, GPIO_BOARD):
        pass

    def setup(self, pin, GPIO_OUT):
        pass

    def output(self, pin_number, status):
        self.pin_state[pin_number] = status

    def cleanup(self):
        pass

    def input(self, pin_number):
        try:
            status = self.pin_state[pin_number]
        except:
            status = 'Undefined'

        return status


