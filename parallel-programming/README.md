## Parallel Computing Architecture

Single Instruction and Single Data
Single Instruction and Multiple Data
Multiple Instruction and Single Data
Multiple Instruction and Multiple Data

Single Program, Multiple Data
Multiple Program, Multiple Data

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
