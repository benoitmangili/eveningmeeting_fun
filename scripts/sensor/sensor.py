import os
import glob
import time
from measurement import Measurement


class DS18B20:
    """ Measures Temperature using a Thermistor """
    # Class variable: Sensor type
    sensorType = "Thermometer"
    sensorID = "DS18B20"
    sensorUnits = "degC"

    def __init__(self):
        self.temperature = 0
        # Set up wire1 communicat
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def __del__(self):
        pass


    def getMeasurement(self):

        # Read raw data
        rawData = self.__readSensor()

        newMeasurement = Measurement()

        if rawData[0].strip()[-3:] == 'YES':
            time_meas = time.time()
            time.sleep(0.2)
            # Extract temperature from raw data
            self.temperature = self.__formatSensorData(rawData[1])

            newMeasurement.timeStamp = time_meas
            newMeasurement.value = self.temperature
            newMeasurement.units = self.sensorUnits

        return newMeasurement

    def __readSensor(self):
        f = open(self.device_file, 'r')
        rawData = f.readlines()
        f.close()
        return rawData

    def __formatSensorData(self, stringInput):

        equals_pos = stringInput.find('t=')
        if equals_pos != -1:
            temp_string = stringInput[equals_pos+2:]
            temp_c = float(temp_string) / 1000.0 # Sensor returns 1/1000 degC
            return temp_c

