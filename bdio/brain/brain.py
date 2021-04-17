from nceserial.driver import NceSerialDriver
from time import sleep

"""RITMRC Layout Control and Signaling: Brain"""

if __name__ == "__main__":  # is this required for an app entrypoint?
    print("All aboard!")  # Hello, world!
    cmd_station = NceSerialDriver()
    cmd_station.connect("/dev/ttyUSB0")
    if cmd_station.is_connected():
        print("Software version: " + cmd_station.version_formatted())
        print("Time: " + cmd_station.read_clock_formatted())
        while True:
            print("time is now " + cmd_station.read_clock_formatted())
            sleep(1)
    else:
        print("not connected")
