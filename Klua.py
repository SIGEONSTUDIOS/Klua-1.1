variables = {}


def get(name, text):
    variables[name] = input(text)
    return variables[name]

def make(name, value):
    try:
        if isinstance(value, bool):
            variables[name] = bool(value)
        elif isinstance(value, int):
            variables[name] = value
        elif isinstance(value, str):
            variables[name] = int(value)
        else:
            variables[name] = value
        return variables[name]
    except Exception as error:
        print("Klua Error:", error)


def kprint(text):
    try:
        if text in variables:
            print(variables[text])
        else:
            print(text)
    except Exception as error:
        print("Klua Error:", error)
        

def condition(condition):
    return eval(condition, {}, variables)

