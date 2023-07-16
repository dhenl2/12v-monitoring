from gpiozero import MCP3008

class AOSensor:
    def __init__(self, channel, scale_func=None):
        self.sensor = MCP3008(channel)
        self.scale_func = scale_func

    def get_reading(self, raw=False):
        if raw:
            return self.sensor.value
        else:
            return self.scale_func(self.sensor.value)

    def get_avg_reading(self, samples=20):
        total = 0
        for i in range(samples):
            total += self.get_reading()

        return total / samples