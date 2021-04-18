import pytest
from serial import Serial, SerialException
from .driver import NceSerialDriver


def test_construction():
    nce = NceSerialDriver()
    assert isinstance(nce.serial, Serial)


def test_connect(mocker):
    nce = NceSerialDriver()
    mocker.patch("serial.Serial.open")
    nce.connect("/dev/notexist")
    assert nce.serial.port == "/dev/notexist"


def test_connect_fail(mocker):
    nce = NceSerialDriver()
    mocker.patch.object(nce, "is_connected", return_value=True)
    with pytest.raises(SerialException) as excinfo:
        nce.connect("port")
    assert "already connected" in str(excinfo.value)


def test_is_connected(mocker):
    nce = NceSerialDriver()
    nce.serial.is_open = True
    mocker.patch.object(nce, "noop", return_value=True)
    assert nce.is_connected()