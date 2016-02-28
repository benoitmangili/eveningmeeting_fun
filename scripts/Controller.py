
class Controller:
    """ Controller """
    def __init__(self, var_lower, var_upper):
        self.var_lower = var_lower
        self.var_upper = var_upper
        self._var_prev = []

    def get_command(self, var_current):
        # If the previous value has not been set yet, set to current
        if self._var_prev == []:
            self._var_prev = var_current

        # If the temperature is below temp_lower, give on command
        if var_current<self.var_lower:
            command = True
        elif var_current > self.var_upper:
            command = False
        elif var_current > self._var_prev:
            command = True
        else:
            command = False

        self._var_prev = var_current
        return command

    def update_temperature_range(self, var_lower, var_upper):
        self.var_lower = var_lower
        self.var_upper = var_upper
