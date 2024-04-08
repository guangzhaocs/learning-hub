# multiprocessing

All testing is under `python/3.7.8`.

## Process

```
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

```
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```

```
main line
module name: __main__
parent process: 34723
process id: 80504
function f
module name: __main__
parent process: 80504
process id: 80505
hello bob
```
