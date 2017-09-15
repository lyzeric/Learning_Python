x =50

def func():
    global x

    print('x is', x)
    x = 2
    print('Change local x to', x)

func()
print('x is still', x)