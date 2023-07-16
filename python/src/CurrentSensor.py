from VoltageSensor import VoltageSensor

NO_DECIMAL_ROUNDING = 0

class CurrentSensor:
    def __init__(self, channel, max_amperage, max_voltage, decimal=NO_DECIMAL_ROUNDING, samples=20):
        """
        Constructor
        :param channel: AO channel to be used.
        :param max_amperage: Max amperage rating of the shunt.
        :param max_voltage: Max voltage reading when at max amperage with the shunt.
        :param decimal: Accuracy of the reading by default.
        :param samples: Number of samples to average for a requested reading.
        """
        self.sensor = VoltageSensor(channel)
        self.resistance = max_amperage / max_voltage
        self.decimal = decimal
        self.samples = samples

    def get_reading(self, options=None):
        if options is None:
            options = {"round": self.decimal}

        value = self.sensor.get_reading(self.samples) / self.resistance
        if options["round"] == NO_DECIMAL_ROUNDING:
            return value
        else:
            return round(value * 10 ** options["round"]) / 10 ** options["round"]
