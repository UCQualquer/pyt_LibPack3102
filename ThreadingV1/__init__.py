import threading as _threading
from typing import Callable, Dict, Tuple, Union
from My_Pack.Essentials import ensureType as _ensureType
import sys as _sys, inspect as _inspect

class NotStartedException(Exception):
    pass

class Thread():
    def __init__(self, target: Callable, args: Tuple = None, custom_data: dict = None, **kwargs):
        if args is None: args = tuple()
        if custom_data is None: custom_data = dict()
        _ensureType(args, tuple, 'args')
        _ensureType(custom_data, dict, 'custom_data')

        def x():
            self._state = 1
            target(*args)
            self._state = 2
        
        self.__thread: _threading.Thread = _threading.Thread(target = x, **kwargs)
        self._state: int = 0 # 0: Non iniciation 1: Running 2: Complete

        # Custom data that will be provided on thread creation, and acessed after.
        # Read only. Not modified in any situation.
        # Use example:
        ## >>> th = Thread(target = ..., args = (...), custom_data = {'test': 123})
        ## >>> th.CustomData
        ## {'test': 123}
        self.__custom_data: dict = custom_data
    

    # See [Thread.running_]
    @property
    def IsRunning(self) -> bool:
        return self._state == 1
    
    # See [Thread.complete_]
    @property
    def IsComplete(self) -> bool:
        return self._state == 2
    
    # See [Thread.__custom_data]
    @property
    def CustomData(self):
        return self.__custom_data

    def start(self):
        try:
            self.__thread.start()
        except (KeyboardInterrupt, SystemExit):
            _sys.exit()
        except Exception as ex:
            raise ex
    
    def join(self, timeout: float | None = None):
        super().join(timeout = timeout)
    
    def startAndJoin(self, timeout: Union[float, None] = None):
        try:
           self.__thread.start()
           self.__thread.join(timeout)

        except (KeyboardInterrupt, SystemExit):
            _sys.exit()
        except Exception as ex:
            raise ex

class Threading(object):
    # Dict containing thread's id and it's object: {0: Thread(...), 1: Thread(...)}
    # Not intended to be modified outside.
    # Can be used to iterate over threads
    threads: Dict[int, Thread] # {thread_id: thread_obj}

    # Last id on [Threading.threads]. Defaults to [-1]
    # Not intended to be modified outside.
    lastId: int = -1

    # If thread target supports key-arguments, it will pass this [Threading] [self] object as kwargs['threading_obj']
    # and it own id as kwargs['thread_id']

    def __init__(self):
        self.threads = {}
        self.lastId = -1

    @property
    def ThreadCount(self) -> int:
        return len(self.threads)
    
    @property
    def RunningCount(self) -> int:
        return len([None for v in self.threads.values() if v.IsRunning])
    
    @property
    def CompleteCount(self) -> int:
        return len([None for v in self.threads.values() if v.IsComplete])
    
    @property
    def AllComplete(self) -> bool:
        return self.ThreadCount == self.CompleteCount

    def AddThread(self, target: Callable, args: Tuple = (), run: bool = False, custom_data: dict = {}, **kwargs) -> Tuple[int, Thread]:
        _ensureType(args, tuple, 'args')
        _ensureType(run, bool, 'run')

        self.lastId += 1
        thread_id = self.lastId

        kwargs['daemon'] = True
        if bool(_inspect.getfullargspec(target)[2]):
            kwargs['kwargs'] = {'threading_obj': self, 'thread_id': thread_id, 'custom_data': custom_data}

        t = Thread(target, args, custom_data, **kwargs)
        self.threads[thread_id] = t
        if run:
            self.StartThread(thread_id)

        return (thread_id, t)
    
    def StartThread(self, thread_id: int):
        _ensureType(thread_id, int, 'thread_id')

        thr = self.threads[thread_id]
        if not thr.IsComplete and not thr.IsRunning:
            thr.start()
        else:
            raise NotStartedException

    def JoinThread(self, thread_id: int):
        _ensureType(thread_id, int, 'thread_id')

        thr = self.threads[thread_id]
        if thr.IsRunning:
            thr.join()
        
        else:
            raise NotStartedException

    def StartAll(self):
        for thread_id in self.threads:
            self.StartThread(thread_id)