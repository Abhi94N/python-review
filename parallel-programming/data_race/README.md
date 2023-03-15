### Data Race

- problem two or more concurrent threads access the same memory location
- at least one thread is modifying it
- Read-Modify-Write
- pay attention whenever two or more threads access the same resource

### Mutual exclusion

- `Critical Section` - Code segment that access a shared resource
- should not be executed by more than one thread or process at a time
-  `Mutex` - lock mechenism to omplement mutual exclusion
  - only one thread or process can possess at a time
  - Limits access to critical section
  - `Atomic Operation`
    - execute as a single action, relative to other threads
    - cannot be interrupted by other concurrent threds
    - Acquire a lock
      - if lock is taken, block/wait for it to be available
      - code protected by mutex should be kept short as possible to operations that require mutual exclusion
    
  
