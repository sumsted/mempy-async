from resourcehelper import ResourceHelper

class generator(object):
    
    def __init__(self, top):
        self.top = top
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        c = self.i
        if self.i < self.top:
            self.i += 1
            return c
        else:
            raise StopIteration()
    
if __name__ == '__main__':
    rh = ResourceHelper(__file__)
    
    for i in generator(10000):
        pass
    
    rh.usage()