# multiprocessing

All testing is under `python/3.7.8`.

## Process

```
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

```
from multiprocessing import Process
import os,time


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    print('hello first', name)
    info('function f')
    time.sleep(5)
    print('hello second', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    print("daemon is", p.daemon)
    p.start()
    p.join()
    print('name is', p.name)
    print('is_alive is', p.is_alive())
    print('exitcode is', p.exitcode)
```
For `join()`, the default argument timeout is None, which means that the method blocks until the process whose `join()` method is called terminates. 

```
main line
module name: __main__
parent process: 34723
process id: 87817
daemon is False
hello first bob
function f
module name: __main__
parent process: 87817
process id: 87823
hello second bob
name is Process-1
is_alive is False
exitcode is 0
```
If timeout is a positive number e.g. `p.join(1)`:
```
if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    print("daemon is", p.daemon)
    p.start()
    p.join(1)
    print('name is', p.name)
    print('is_alive is', p.is_alive())
    print('exitcode is', p.exitcode)
```

```
main line
module name: __main__
parent process: 34723
process id: 88868
daemon is False
hello first bob
function f
module name: __main__
parent process: 88868
process id: 88875
name is Process-1
is_alive is True
exitcode is None
hello second bob
```
```
if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    print("daemon is", p.daemon)
    p.start()
    p.join(1)
    print('name is', p.name)
    print('is_alive is', p.is_alive())
    print('exitcode is', p.exitcode)
    time.sleep(10)
    print('-----------------\nafter 10s')
    print('name is', p.name)
    print('is_alive is', p.is_alive())
    print('exitcode is', p.exitcode)
```
```
main line
module name: __main__
parent process: 34723
process id: 89567
daemon is False
hello first bob
function f
module name: __main__
parent process: 89567
process id: 89568
name is Process-1
is_alive is True
exitcode is None
hello second bob
-----------------
after 10s
name is Process-1
is_alive is False
exitcode is 0
```
multiprocessing supports two types of communication channel between processes: `Queue` and `Pipe`.

## Queue
```
class multiprocessing.Queue([maxsize])
```


## Pipe
```
multiprocessing.Pipe([duplex])
```

## Pool
```
class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
```

Reference:
- https://docs.python.org/3/library/multiprocessing.html
- https://blog.csdn.net/brucewong0516/article/details/85776194
- https://blog.csdn.net/LCY133/article/details/107173364
