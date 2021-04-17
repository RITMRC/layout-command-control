import serial
from .commands import commands

NCE_BAUD = 9600
NCE_BYTESIZE = serial.EIGHTBITS
NCE_PARITY = serial.PARITY_NONE
NCE_STOPBITS = serial.STOPBITS_ONE
TIMEOUT_SEC = 1


class NceSerialDriver:
    """NCE Command Station Serial Interface Driver"""

    def __init__(self):
        self.serial = serial.Serial(
            baudrate=NCE_BAUD,
            parity=NCE_PARITY,
            stopbits=NCE_STOPBITS,
            timeout=TIMEOUT_SEC,
        )

    def is_connected(self):
        return self.serial.is_open and self.noop()

    def connect(self, port):
        if self.is_connected():
            raise serial.SerialException("NCE Serial already connected")
        if port:
            self.serial.port = port
        self.serial.open()

    def disconnect(self):
        if not self.is_connected():
            raise serial.SerialException("NCE Serial not connected")
        self.serial.close()

    def write(self, data):
        self.serial.write(data)

    def read(self, bytecount):
        return self.serial.read(bytecount)

    def run_command(self, command_name):
        command = commands[command_name]
        self.write(command["cmd"])
        return self.read(command["res_size"])

    def noop(self):
        return self.run_command("NOOP")

    def dummy(self):
        return self.run_command("DUMMY")

    def read_clock(self):
        """Read command station clock setting"""
        return self.run_command("CLOCK_READ")

    def read_clock_formatted(self):
        hour, minute = self.read_clock()
        return f"{hour}:{minute}"

    def version(self):
        return self.run_command("VERSION")

    def version_formatted(self):
        VV, MM, mm = self.version()
        return f"v{VV}.{MM}.{mm}"
