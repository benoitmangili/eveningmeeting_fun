import pytest
from Controller import Controller


class TestController:
    def test_get_on_when_too_cold(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        assert c.get_command(13) == True

    def test_get_off_when_too_hot(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        assert c.get_command(22) == False

    def test_hysteresis_from_below(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        c.get_command(14)
        assert c.get_command(15) == True

    def test_hysteresis_from_above(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        c.get_command(19)
        assert c.get_command(16) == False

    def test_first_measurement_in_range(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        assert c.get_command(16) == False

    def test_update_temperature_range(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_lower, t_upper)
        c.update_temperature_range(16,17)
        assert c.set_point_lower == 16
        assert c.set_point_upper == 17

    def test_swapped_temperature_range(self):
        t_lower = 15
        t_upper = 18
        c = Controller(t_upper, t_lower)
        assert c.set_point_lower == 15
        assert c.set_point_upper == 18