import os
import json


class Config:
    _instance = None

    def __new__(cls, conf=None, default=None):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        elif conf:
            raise Exception("Dynamic configuration file is not implemented")

        return cls._instance

    def __init__(self, conf=None, default=None):
        if not hasattr(self, "initialized"):
            if conf:
                if os.path.isfile(conf):
                    with open(conf, "r") as f:
                        self.config = json.load(f)
                else:
                    self.config = default
            else:
                self.config = default

            self.initialized = True
