from resourcehelper import ResourceHelper


def generator(top):
    i = 0
    while i < top:
        yield i
        i += 1


if __name__ == '__main__':
    rh = ResourceHelper(__file__)
    
    for i in generator(10000):
        pass
    
    rh.usage()