import os
import json

defaultDirectory = None


with open(os.getenv("HOME") + "/.config/user-dirs.dirs") as f:
    for line in f:
        if "XDG_VIDEOS_DIR" in line:
            defaultDirectory = line.split("=")[1].strip().replace("$HOME", os.getenv("HOME")).replace('"', '')


config_directory = os.getenv("HOME") + "/.config/groaac"
config_path = config_directory + "/config.json"

if not os.path.exists(config_directory):
    os.mkdir(config_directory)


if defaultDirectory is None:
    defaultDirectory = os.getenv("HOME")


def save_config(config: dict):
    with open(config_path, "w") as f:
        json.dump(config, f)


if not os.path.exists(config_path):
    save_config({"directory": defaultDirectory})


def load_config():
    with open(config_path, "r") as f:
        return json.load(f)