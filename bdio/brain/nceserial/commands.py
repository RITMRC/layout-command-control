import csv
import os
from pprint import pprint

COMMANDS = {}
RESPONSES = {
    "SUCCESS": b"!",
    "UNSUPPORTED_COMMAND": b"0",
    "ADDRESS_RANGE_ERROR": b"1",
    "CAB_OP_RANGE_ERROR": b"2",
    "DATA_RANGE_ERROR": b"3",
    "BYTE_COUNT_RANGE_ERROR": b"4",
    "SPEED_MODE_1": b"14",
    "SPEED_MODE_2": b"28",
    "SPEED_MODE_3": b"128",
}
RESPONSE_VALUES = {v: k for k, v in RESPONSES.items()}

this_dir, this_filename = os.path.split(__file__)
commands_file = os.path.join(this_dir, "commands.csv")


def unpack_opts(field):
    if not field:
        return []
    options = field.split("|")
    return list(map(lambda o: bytes(o, "ascii"), options))


with open(commands_file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "#":
            continue
        if row[1] == "name":
            continue
        cmd = bytes.fromhex(row[0])
        name = str.upper(str.rstrip(row[1]))
        arg_size = int(row[2])
        res_size = int(row[3])
        res_opts = unpack_opts(row[4])

        COMMANDS[name] = (cmd, arg_size, res_size, res_opts)