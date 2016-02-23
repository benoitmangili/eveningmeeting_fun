import pytest

import MockGPIO

class TestMockGPIO:

    def test_state_high(self):
        m = MockGPIO.MockGPIO()
        assert m.HIGH() == True


    def test_state_low(self):
        m = MockGPIO.MockGPIO()
        assert m.LOW() == False

    def test_input(self):
        m = MockGPIO.MockGPIO()
        assert m.input(29) == True
