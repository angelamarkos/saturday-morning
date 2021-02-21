from abc import ABC, abstractmethod

class Protype(ABC):
        def __init__(self):
            pass

        @abstractmethod
        def clone(self):
            pass

class Config(Protype):
    def __init__(self, log_path, microsevice_1_ip, microsevice_2_ip, database_config={}):
        self.log_path = log_path
        self.microsevice_1_ip = microsevice_1_ip
        self.microsevice_2_ip = microsevice_2_ip
        self.database_config = database_config

    def __str__(self):
        return f'{self.log_path} \n' \
               f'{self.microsevice_1_ip} \n' \
               f'{self.microsevice_2_ip} \n' \
               f'{self.database_config}'

    def clone(self):
        pass


class Protype:
    """ objects_data = {obj1: [{attr1: value, attr2: value, ...}]}"""
    def __init__(self, objects_data, class_name):
        self.objects_data = objects_data
        self.class_name = class_name

    def clone(self):
        for object, kwargs_list in self.objects_data.items():
            for kwargs in kwargs_list:
                yield self.class_name(**{**object.__dict__, **kwargs})


config_1 = Config('.\logs\dev', microsevice_1_ip='123.3.65.6', microsevice_2_ip='12.0.0.3',
                  database_config={
                      'username': 'user',
                      'password': 'password',
                      'database': 'employee',
                      'host': '12.0.0.4',
                      'port': '1234'
                  })

prototype = Protype({config_1: [{'microsevice_1_ip': '134.0.0.34'}, {'microsevice_2_ip': '98.97.4.3'}]}, Config)

print(type(config_1).__name__)

# for config in prototype.clone():
#     print(config)
