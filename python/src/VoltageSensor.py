from Sensor import AOSensor

R1 = 30000
R2 = 7500
REF_VOLTAGE = 5
SCALE_CORRECTION = 0.98066914498

class VoltageSensor:
    def __init__(self, channel, decimal):
        self.sensor = AOSensor(channel, self.scale_func)
        self.decimal = decimal      # Number of decimal places

    def scale_func(self, value):
        adc_voltage = value * REF_VOLTAGE
        return adc_voltage * ((R1 + R2) / R2) * SCALE_CORRECTION

    def get_reading(self, samples=1000, options=None):
        if options is None:
            options = {"round": self.decimal}

        return round(self.sensor.get_avg_reading(samples) * 10 ** options["round"]) / 10 ** options["round"]