from Sensor import AOSensor

R1 = 30000
R2 = 7500
REF_VOLTAGE = 5
SCALE_CORRECTION = 0.98066914498
NO_DECIMAL_ROUNDING = 0
class VoltageSensor:
    def __init__(self, channel, decimal=NO_DECIMAL_ROUNDING):
        """
        Constructor
        :param channel: AO channel to be used.
        :param decimal: Accuracy of the reading by default.
        """
        self.sensor = AOSensor(channel, self.scale_func)
        self.decimal = decimal      # Number of decimal places

    def scale_func(self, value):
        """
        Scaling function to correct the read voltage from the voltage sensor.
        :param value: Read value from the sensor.
        :return: Scaled value.
        """
        adc_voltage = value * REF_VOLTAGE
        return adc_voltage * ((R1 + R2) / R2) * SCALE_CORRECTION

    def get_reading(self, samples=1000, options=None):
        if options is None:
            options = {"round": self.decimal}

        if options["round"] == NO_DECIMAL_ROUNDING:
            # raw value
            return self.sensor.get_avg_reading(samples)
        else:
            # rounded value
            return round(self.sensor.get_avg_reading(samples) * 10 ** options["round"]) / 10 ** options["round"]