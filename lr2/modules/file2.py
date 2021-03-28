from file1 import *


def funct(x):
    return x + z



if __name__ == '__main__':
    string_toml = return_string()
    toml_serializer = create_serializer('toml')
    fun = toml_serializer.loads(string_toml)

    print(fun(1,2, 3))