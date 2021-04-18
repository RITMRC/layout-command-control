from nceserial.driver import NceSerialDriver
from nceserial.commander import NceCommander
from time import sleep

"""RITMRC Layout Control and Signaling: Brain"""

if __name__ == "__main__":  # is this required for an app entrypoint?
    print("All aboard!")  # Hello, world!
    driver = NceSerialDriver()
    driver.connect("/dev/ttyUSB0")
    cmd_station = NceCommander(driver)
    if cmd_station.is_online():
        print("NCE Software version: " + cmd_station.version_formatted())
        print("Time: " + cmd_station.clock_formatted())
        while True:
            print(cmd_station.aiu_status(4))
            sleep(1)
    else:
        print("not connected")
 