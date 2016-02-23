import time
from measurement import Measurement


class DummySensor:
    """ Dummy Sensor """
    # Class variable: Sensor type
    def __init__(self):
        pass

    sensorType = "DummySensor"
    sensorID = "Dummy"
    sensorUnits = "-"

    def getMeasurement(self):

        newMeasurement = Measurement()
        newMeasurement.timeStamp = time.time()
        newMeasurement.value = 1
        newMeasurement.units = self.sensorUnits
        return newMeasurement