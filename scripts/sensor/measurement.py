__author__ = 'Anniek'


class Measurement(object):
    def __init__(self, **kwargs):
        # Todo: initialise to default values if no inputs are given
        if kwargs:
            self.timeStamp = kwargs['timeStamp']
            self.value = kwargs['value']
            self.units = kwargs['units']

    def set_values(self, timeStamp, value, units):
        self.timeStamp = timeStamp
        self.value = value
        self.units = units

    def convert_to_dict(self):
        measurement_dict = {'timeStamp': self.timeStamp, 'value': self.value, 'units': self.units}
        return measurement_dict
