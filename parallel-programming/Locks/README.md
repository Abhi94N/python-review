# Locks 

### Deadlock

- if thread tries to lock a mutex that is already locked, all process and threads are unable to continue executing

- Reentrant Mutex - Can be locked multiple times by the same process or thread
  - must be unlocked as many times as it was locked
  - recursive function call is an example of renetrant mutex
  - Reentrant mutex
  - Reentrant lock
  - Recursive mutex
  - Recursive lock

### Locks vs RLock

- Lock can be released by a diffrent thread than was used to acquire it
- RLock must be released by the same thread that acquired it
  - Must be released the same number of times it was acquired
- spliting lock operations with multiple threads is usually a bad idea


### Try Lock
- Non-blocking lock/acquire method for mutex
- if mutex is available, locak it and return true
- if mutlex is not available, immediately return False


### Reader-Writer Lock - Shared Mutex

- `SHARED READ` - multiple threads read at once and cannot read until exclusive write lock is released
- `EXCLUSTIVE WRITE` - only one thread can write at a time to shared resource and must wait until read locks are released
- usefule when you have a lot more threads reading the shared data than writing the shared data
- `pip install readerwriterlock`
- RWLock variations
  - `RWLockFair` - fiar priority for readers/writers
  - `RWLockRead` - readers get priority
  - `RWLockWrite` - writers get priority
- RWLock methods
  - `gen_rlock()` - generates a reader lock object
  - `gen_wlock()` - generates a writer lock object

### Deadlock

- each member is waiting for another member to take action
- Liveness - prperties that require system to amke progress
  - Members may have to `take turns` in critical sections
- `Prioritize Locks` - acquire highest priority chopstick first
  - `Lock ordering` - ensure locks are always taken in the same order any thread
  - `Lock timeout` - put a time out on lcok attempts
    - if thread cannot acquire locks within alloted time, thread will release all locks, wait a random amount of time and try again
  - use context manager instead of try catch

### Starvation
- a process or thread is prepetually denied the resource it needs

### LiveLock

- Multiple threads or processes are actively responding to each other to resolve conflict, but it prevents them from making progress

    



