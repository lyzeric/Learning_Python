def normalize(name):
    return name.capitalize()

L1 = ['asd', 'Aasdf', 'ff']
L2 = list(map(normalize , L1))
print(L2)