## Parallel Computing Architecture

- Single Instruction and Single Data
- Single Instruction and Multiple Data
- Multiple Instruction and Single Data
- Multiple Instruction and Multiple Data

- Single Program, Multiple Data
- Multiple Program, Multiple Data

Memory Speed is slower than Processor Speed

#### Shared Memory Architecture - All processors access the same memory with global address space
  1. Uniform Memory access - all process have equal access to memory
      -  Symmetric Multiprocessing - two or more identical processors connected to the same system bus that connects it to the shared memmory
        - cache memory - local storage for a processor
  2. Non-Uniform Memory access - made by physically connecting SMP together
    - some process will have faster access to others regarding certain parts of memory
    - requires programmer to sync cache data and memory

#### Distributed Memory Architecture
  1. Each processor has its own memory and its own address space
  2. scalable but need to sync when to share data form memory across processor


### Threads anad process

1. Process
  - includes code, data, and state information
  - independent instance of a running program
  - seperate address space and memory

2. Threads - tiny processes
  - independent path of exection
  - subset of a process
  - operationg system schedules threads for execution
  - shared address space for process
  - require less overhead to create and terminate
  OS can switch faster between threads than processes

3. Sharing data between processses(Inter-process Communication)
  - Sockets and pipes
  - shared memory
  - Remote Procedure Call

4. Concurrent vs parallel execution
  - ability of an algorithm or program to be broekn into parts that can run independently of each other
  - Concurrent Execution - our two parallel processes overlap in time
  - Parallel hardware
    - Multi-Core Processors
    -  GPU
    - Computer Cluster
  - Concurrency
    - program structure
    - dealing with multiple things at once
  - Parallelism
    - simultaneous Execution
    - Doing multiple things at once
  - I/O - concurrently with single 
  - GPU - I/O dependent tasks
  - Parallelism processing - computationally intensive tasks


### Python
- concurrent python threads are allowed but python does not allow for parallel python threads due to `global interpreter lock`
  - mechanism that limits python to only execute one thread at a time
- CPython - default python interpreter written in C and python
- GIS allows for thread safe for execution
- Other python interpretors not with GIL - Jython, ironPython, PyPy-STM, CPython
- I/O bound tasks
  - GIL is not a bottleneck
  - Use the python trheading module
- CPU-bound Application
  - GIL can negatively impact performance
  - Implement parallel algorithms as external library functions
  - use the python multiprocessing package
    - each process will be its own instance of python interpretor with its own gil
    - communication between process will be challenge

` ps aux` - how to view processes running

  - ps: is the process status command.
  - a: displays information about other users' processes as well as your own.
  - u: displays the processes belonging to the specified usernames.
  - x: includes processes that do not have a controlling terminal.

- Scheduler
  - operating system function that assigns processes and threads to run on available CPUs
  - processes get loaded into memory and added to the read queue(FIFO)
  - Multiple process will dequeue if there are available resources(processes)
  - process may get blocked and have to an I/O event so scheduler will move process to I/O queue
  - Context Switch - store the state of a process or thread to resume later
      - has to load the new state of the process or thread
  - Scheduling Algoirthms for context switch
      - NonPreemptive - lets schedule run the entire process
          - First come, first served
          - Round Robin
          - Multiple-level queues
      - Premptive 
          - shortest job  
          - priority
          - shortest remaining time
      - Goals:
        - maximize throughput
        - maximize fairness
        - maiximze wait time
        - minimize latency
- Thread life cycle
  - main thread
      - can spawn child thread which is part of same process but execute independently to do other tasks
      - child thread can also spawn child threads who notify their parent once process is complete and terminate
  - you must eplicitly start the thread in order for it to move to runnable state which means the operating system can schedule  
    - context switching allows for operating system to run thread in one of the available processes
  a thread is in a blocked state and not using resources when it is waiting for an event to occur
    - wating->Blocked->Resume->Runnable
  - `join()` - wait until another thread completes its execution
  - a thread enters the terminated state when it has finished execution or aborted and notifies its parent if it is a child thread
  - lifecycle thread phases
    - new, runnable, blocked, terminated
  - `is_alive()` - thread to check if thread is alive
- Garbage Collector
  - automatic memory management that reclaims memory no longer in use by program
- Daemon (Background) Thread
  - Does not prevent the process from terminating when main thread is finsihed
  - by default, threads are created as non-daemon
  - detached from the main program
  - daemon threads terminates when there are no more threads are running
  - new threads will inherit daemon status from their parent
  - set the daemon property to change status before starting thread
  when program ends, remaining daemon threads are abandoned
  - A daemon thread will be abruptly terminated when the main thread finishes. If that occurs during a write operation, the file could be corrupted.

### Facts

- I/O-bound tasks spend most of their time waiting on external actions, like network operations or user input. They do not need to possess the GIL while waiting on I/O, so the GIL usually has a minimal impact on I/O-intensive applications.
- The Global Interpreter Lock prevents multiple Python threads from executing at the same time.
- Concurrent tasks can take turns to execute on the same processor.
- Mathematical operations on matrices are computationally intensive and therefore well suited to benefit from parallel execution.
- Concurrency describes the structure that enables a program to execute in parallel (given the necessary hardware), but a concurrent program is not inherently parallel.
- Threads that belong to the same process share that process's address space.







      