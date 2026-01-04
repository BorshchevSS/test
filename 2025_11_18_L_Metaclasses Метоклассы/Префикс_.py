class LoggerMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                if not attr_name.startswith('log_'):
                    new_name = f'log_{attr_name}'
                    new_attrs[new_name] = attr_value
                else:
                    new_attrs[attr_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)

class Service(metaclass=LoggerMeta):
    def __init__(self, value):
        self.value = value

    def calc(self, x, y):
        return x+y+self.value

    def log_status(self):
        print('ok')

    TEST = 5

service = Service(value=10)
res = service.log_calc(1, 2)
print(res)
service.log_status()
print(Service.TEST)