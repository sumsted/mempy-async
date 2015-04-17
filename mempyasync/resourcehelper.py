__author__ = 'scottumsted'
import gc
import resource
import time

class ResourceHelper():
    def __init__(self, module=None):
        self.module = '' if module is None else '\nmodule:\t'+module+'\n'
        gc.disable()
        self.reset()
        
    def reset(self):
        self.start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        self.start_utime = resource.getrusage(resource.RUSAGE_SELF).ru_utime
        self.start_stime = resource.getrusage(resource.RUSAGE_SELF).ru_stime
        self.start_time = time.time()
        
    def usage(self):
        stop_utime = resource.getrusage(resource.RUSAGE_SELF).ru_utime
        stop_stime = resource.getrusage(resource.RUSAGE_SELF).ru_stime
        diff_utime = stop_utime - self.start_utime
        diff_stime = stop_stime - self.start_stime
        diff_cpu = (stop_utime + stop_stime) - (self.start_utime + self.start_stime)
        diff_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - self.start_mem
        diff_time = time.time() - self.start_time;
        print('{}mem:\t{:,}\nutime:\t{:f}\nstime:\t{:f}\ncpu:\t{:f}\ntime:\t{:f}\n'.format(self.module, diff_mem, diff_utime, diff_stime, diff_cpu, diff_time))