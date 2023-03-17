### Synchronization

- `Conditional Variable` - queue of threads waiting for a certain condition
- Associated with a mutex
- `Monitor` - protect section of code with mutual exclusion and provide ability for threads to wait until a condition occurs
- `wait` - automatically release lock on the mutex
  - Go to sleep and enter waiting queue
  - reacquire lock when woken up
`signal` - wake up one thread from condion variable queue
  - also known as `notify` or `wake`
- `broadcast`
  - wake up all threads from condition variable queue
- Shared Queue or Buffer
  - needs mutex - only one thread to add or remove from it
  - condition variables(add items to a quueue)
    - BuffernotFull - wait on condition(signal)
    - BufferNotEmpty - wait on condition(signal)

- Using a conditional variable
  - acquire lock
  - conditional variable waits for a condition
  - does something and then releases a lock
  - The condition - is the conditional logic
  - condition_variable is a place for the threads to wait until they are signal by another thread to check the condition
  - confirm that you have a lock on mutex before you do something that changes the state of the conditional variable

### Producer-Consumer pattern

- Producer
    - Add elements to shared data structure
- Consumer
    - Remove elements from shared data structure
- Queue(FIFO) - tiems are removed in the same order that they are put in the queue
- Enforce mutual exclusion of producers and consumers
- Prevent producers from trying toa dd data to a full queue
- Prevent consumers from trying to remove data from an empty queue
- Unbounded Queue - A queue with an unlimited capacity implmented with LinkedList only limited by computer memory
- Average rate of production < average rate of consumption
- Pipeline - chain of processing elements
  - Producer queue -> Consumer, Producer -> queue Consumer

### Global Interpreter Lock(GIL)
- Mechansim that limits python to only execute one thread at a time
- use the multprocessing package as a workaround

### Semaphore

- Synchronization mechanism
- can be used by multiple threads at the same time
- includes a counter to track visibility
-  `acquire()`
  - if counter is positive, decrement counter
  - if counter is zero, wait until available
- `release()`
  - increment counter
  - signal waiting thread
- Types
  - Counting Sempaphore
    - value >= 0
    - used to track limted resources
  - Binary Semaphore
    - Value = 1 or 0
      - 0 represents locked state
      - 1 represents unlocked
    - similar to mutex
  - Producer-Consumer Semaphore
    - one semaphore tracks item in buffer
      - acqure empty count
      - put item in buffer
      - release to fill count
    - one semaphore tracks free spaces in buffer
      - acqures fillcount
      - remove item
      - release emptycount
    - producer and consumer aquire a different semaphore as the first operation as their respective sequence
- semaphore can be acquire and released by different threads which a mutuex cannot


