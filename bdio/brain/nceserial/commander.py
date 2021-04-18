import struct
from .commands import COMMANDS, RESPONSE_VALUES
from .util import int2addr

class NceCommander:
    def __init__(self, driver):
        self.driver = driver

    def is_online(self):
        return self.driver.is_connected() and self.noop()

    def run_command(self, name):
        try:
            cmd, _, res_size, res_opts = COMMANDS[name]
        except KeyError:
            raise Exception(f"'{name}' is not a valid NCE command")
        
        result = self.driver.read_write(cmd, res_size)
        if len(res_opts):
            if result not in res_opts:
                # TODO: map this better from error response code to
                # an error class
                raise Exception(f"response not in possible result set")
        return result

    def clock(self):
        """Read command station clock setting"""
        return self.run_command("CLOCK_READ")

    def clock_formatted(self):
        hour, minute = self.clock()
        return f"{hour}:{minute}"

    def version(self):
        return self.run_command("VERSION")

    def version_formatted(self):
        VV, MM, mm = self.version()
        return f"v{VV}.{MM}.{mm}"

    def noop(self):
        return self.run_command("NOOP")

    def dummy(self):
        return self.run_command("DUMMY")

    def aiu_status(self, address):
        cmd = struct.pack(">BB", 0x8A, address)
        result = self.driver.read_write(cmd, 4)
        #return [byte >> i & 1 for i in range(8) for byte in result]
        return (
            [int.from_bytes(result[0:2], byteorder='big') >> i & 1 for i in range(16)],
            [int.from_bytes(result[2:4], byteorder='big') >> i & 1 for i in range(16)]
        )
