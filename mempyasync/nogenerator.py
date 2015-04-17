from resourcehelper import ResourceHelper

def no_generator(top):
    result = []
    i = 0
    while i < top:
        result.append(i)
        i += 1
    return result


if __name__ == '__main__':
    rh = ResourceHelper(__file__)
    
    for i in no_generator(10000):
        pass
    
    rh.usage()