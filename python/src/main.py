from MonitoringSystem import MonitorSystem
import time

system = MonitorSystem()

while True:
    system.get_reading()
    time.sleep(1)