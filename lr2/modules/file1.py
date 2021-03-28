from entrypoint import *
from serializers import *
from customSerializer import *

z = 10
s = 5
k = 2


def func(x, y, z):
    return x + y + z


def return_string():
    toml_serializer = create_serializer('toml') 
    string_toml = toml_serializer.dumps(func, 'function')
    return string_toml
    




