from loguru import logger
from datetime import timedelta
import configparser
from VoltageSensor import VoltageSensor
from CurrentSensor import CurrentSensor
from TempSensor import TempSensor
import sys

CONFIG_VOLTAGE_SENSOR = "Voltage Sensor"
CONFIG_CURRENT_SENSOR= "Current Sensor"
CONFIG_TEMP_SENSOR = "Temperature Sensor"
CONFIG_LOGGER = "Logger"

class MonitorSystem:

    def __init__(self, config_file="./config.ini"):
        self.logger = logger
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.voltage = None
        self.current = None
        self.temp = None
        self.initialise()

    def initialise(self):
        # logger
        logger.remove()
        logger.add(
            sink=self.config[CONFIG_LOGGER]["file"],
            rotation=timedelta(days=1),
            level=self.config[CONFIG_LOGGER]["level"].upper(),
            colorize=True
        )
        if bool(self.config[CONFIG_LOGGER]["stdout"]):
            logger.add(
                sink=sys.stdout,
                level=self.config[CONFIG_LOGGER]["level"].upper()
            )
        self.logger.info("Initialising Monitoring System...")

        self.voltage = VoltageSensor(
            channel=int(self.config[CONFIG_VOLTAGE_SENSOR]["AO_channel"]),
            decimal=int(self.config[CONFIG_VOLTAGE_SENSOR]["round"]),
            samples=int(self.config[CONFIG_VOLTAGE_SENSOR]["samples"])
        )
        self.current = CurrentSensor(
            channel=int(self.config[CONFIG_CURRENT_SENSOR]["AO_channel"]),
            max_amperage=float(self.config[CONFIG_CURRENT_SENSOR]["max_amperage"]),
            max_voltage=float(self.config[CONFIG_CURRENT_SENSOR]["max_voltage"]),
            samples=int(self.config[CONFIG_CURRENT_SENSOR]["samples"])
        )
        self.temp = TempSensor(
            channel=int(self.config[CONFIG_TEMP_SENSOR]["AO_channel"]),
            m=float(self.config[CONFIG_TEMP_SENSOR]["m"]),
            c=float(self.config[CONFIG_TEMP_SENSOR]["c"]),
            samples=int(self.config[CONFIG_TEMP_SENSOR]["samples"])
        )

    def get_reading(self, log=False):
        if log:
            self.logger.info(
                f"Voltage: {self.voltage.get_reading()}V\n" +
                f"Amperage: {self.current.get_reading()}A"
            )

        return {
            "voltage": self.voltage.get_reading(),
            "amperage": self.current.get_reading()
        }
