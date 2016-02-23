import pytest

import MockGPIO

class TestMockGPIO:

    def test_state_high(self):
        m = MockGPIO.MockGPIO()
        assert m.HIGH() == True


    def test_state_low(self):
        m = MockGPIO.MockGPIO()
        assert m.LOW() == False

    def test_default_state(self):
        m = MockGPIO.MockGPIO()
        assert m.input(29) == 'Undefined'

    def test_setting_state(self):
        m = MockGPIO.MockGPIO()
        # Set the state
        pin_number = 1
        m.output(pin_number, True)

        # Recover the state
        assert m.input(pin_number) == True
