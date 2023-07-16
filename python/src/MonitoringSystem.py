from loguru import logger
from datetime import timedelta
import configparser
from VoltageSensor import VoltageSensor
import sys

CONFIG_VOLTAGE_SENSOR = "Voltage Sensor"
CONFIG_LOGGER = "Logger"

class MonitorSystem:

    def __init__(self, config_file="./config.ini"):
        self.logger = logger
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.voltage = None
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

    def get_reading(self):
        self.logger.info(
            f"Voltage: {self.voltage.get_reading()}V"
        )
