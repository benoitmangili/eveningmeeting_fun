
class Controller:
    """ Controller """
    def __init__(self, set_point_lower, set_point_upper):
        self.set_point_lower = set_point_lower
        self.set_point_upper = set_point_upper
        self._var_prev = []

    def get_command(self, var_current):
        # If the previous value has not been set yet, set to current
        if self._var_prev == []:
            self._var_prev = var_current

        # If the temperature is below temp_lower, give on command
        if var_current<self.set_point_lower:
            command = True
        elif var_current > self.set_point_upper:
            command = False
        elif var_current > self._var_prev:
            command = True
        else:
            command = False

        self._var_prev = var_current
        return command

    def update_temperature_range(self, set_point_lower, set_point_upper):
        self.set_point_lower = set_point_lower
        self.set_point_upper = set_point_upper
