import serial

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
        return self.serial.is_open

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
        #print(f"driver: writing - {data}")
        return self.serial.write(data)

    def read(self, size):
        result = self.serial.read(size)

        #print(f"driver: read {size} bytes - {result.hex()}")
        return result

    def read_write(self, data, size):
        self.write(data)
        return self.read(size)