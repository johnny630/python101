import multiprocessing
import os
import time

def whoami(what):
    time.sleep(20)
    print('Process %s says: %s' % (os.getpid(), what))
    
if __name__ == '__main__':
    # whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,))
        p.start()