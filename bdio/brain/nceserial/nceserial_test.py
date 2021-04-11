from serial import Serial
from nceserial import NceSerial


def test_NceSerial_construction():
    nce = NceSerial()
    assert isinstance(nce.serial, Serial)
