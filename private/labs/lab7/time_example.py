import time


def func():
    return 2 + 2
def func2():
    return 2 + 3
#time.time() <-- # of seconds since Jan 1 1970
#tstart = time.time()
#do stuff
#tstop = time.time()
#delta_t = tstop - tstart

N = 10000

tstart = time.time()
for i in range(N):
    func()
tstop = time.time()
print("Elapsed time for func(): ",(tstop-tstart) / N )


tstart = time.time()
for i in range(N):
    func2()
tstop = time.time()
print("Elapsed time for func2(): ",(tstop-tstart) / N )
