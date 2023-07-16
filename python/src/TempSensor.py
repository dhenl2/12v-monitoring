from Sensor import AOSensor
class TempSensor:
    def __init__(self, channel, m, c, samples):
        """
        Constructor
        :param channel: AO channel to be used.
        :param m: Linear scale to be applied to the read raw value.
        :param c: Offset to be applied to the read raw value.
        :param samples: Number of samples to be averaged.
        """
        self.m = m
        self.c = c
        self.sensor = AOSensor(channel)
        self.samples = samples

    def linear_func(self, value):
        return (self.m * value) + self.c

    def get_reading(self):
        return self.sensor.get_avg_reading(self.samples)