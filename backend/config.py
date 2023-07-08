import json


class Config(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)

            with open('./config.json', mode='r') as f:
                cls.configs = json.load(f)

        return cls.instance
