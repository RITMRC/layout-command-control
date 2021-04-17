import csv
import os

commands = {}

this_dir, this_filename = os.path.split(__file__)
commands_file = os.path.join(this_dir, "commands.csv")

with open(commands_file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "#":
            continue
        cmd, name, arg_size, res_size, res_options = row
        if name == "name":
            continue
        name_upper = str.upper(str.rstrip(name))
        commands[name_upper] = {
            "cmd": bytes.fromhex(cmd),
            "arg_size": int(arg_size),
            "res_size": int(res_size),
            "responses": None,
        }
        if res_options:
            commands[name_upper]["responses"] = res_options.split("|")
