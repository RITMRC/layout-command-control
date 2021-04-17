from serial import Serial
from driver import NceSerialDriver


def test_NceSerial_construction():
    nce = NceSerialDriver()
    assert isinstance(nce.serial, Serial)
