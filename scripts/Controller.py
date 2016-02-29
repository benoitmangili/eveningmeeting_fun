
class Controller:
    """ Controller """
    def __init__(self, set_point_lower, set_point_upper):
        self.update_temperature_range(set_point_lower, set_point_upper)
        self._state_prev = False

    def get_command(self, var_current):

        # If the temperature is below temp_lower, give on command
        if var_current <= self.set_point_lower:
            state = True
        elif var_current > self.set_point_upper:
            state = False
        else:
            state = self._state_prev

        self._state_prev = state
        command = state
        return command

    def update_temperature_range(self, set_point_lower, set_point_upper):

        if set_point_lower <= set_point_upper:
            self.set_point_lower = set_point_lower
            self.set_point_upper = set_point_upper
        else:
            # Swap if the lower set point is larger than the upper
            self.set_point_lower = set_point_upper
            self.set_point_upper = set_point_lower
