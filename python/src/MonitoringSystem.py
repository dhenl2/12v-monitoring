from loguru import logger
from datetime import timedelta
import configparser
from VoltageSensor import VoltageSensor
from CurrentSensor import CurrentSensor
import sys

CONFIG_VOLTAGE_SENSOR = "Voltage Sensor"
CONFIG_CURRENT_SENSOR= "Current Sensor"
CONFIG_LOGGER = "Logger"

class MonitorSystem:

    def __init__(self, config_file="./config.ini"):
        self.logger = logger
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.voltage = None
        self.current = None
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
            int(self.config[CONFIG_VOLTAGE_SENSOR]["AO_channel"]),
            int(self.config[CONFIG_VOLTAGE_SENSOR]["round"])
        )
        self.current = CurrentSensor(
            int(self.current[CONFIG_CURRENT_SENSOR]["AO_channel"]),
            float(self.current[CONFIG_CURRENT_SENSOR]["max_amperage"]),
            float(self.current[CONFIG_CURRENT_SENSOR]["max_voltage"])
        )

    def get_reading(self):
        self.logger.info(
            f"Voltage: {self.voltage.get_reading()}V\n" +
            f"Amperage: {self.current.get_reading()}A"
        )
