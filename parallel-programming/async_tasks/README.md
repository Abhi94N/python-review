# Async

- `Cirtical Path` - how long the longest path lasts which creates work
- `Ideal Parallelism` = work/span
- `Thread pool`- creates a maintains a collection of wroker thread.
  - reuses existing threads to execute tasks
  - ThreadPoolExecuter class in python
    - higher level interface for asycnrnously running tasks
    - when max workers is set to none it creates five times as many threads as CPUs
  - ProcessPoolExecuter - for multiple process
- `Process pool`
  - samething but with processes
- `Future` - placeholder for a result that will be available later
  - mechanism ot access the result of an asynchronous operation

- Divide and Conquer algos
  - divide problem int subproblems
  - solve subproblems recursively
  - combine the soltuons to the subproblems
  - The base case uses a sequential algorithm executing as a separate process to find the solution to the subproblem.

# Evaluating Speedup, latency, and throughput

- `Weak Scaling` - variable number of processors with fixed problem size per processor
  - accomplish more work in the same time
- `Strong scaling` - variable number of processors with fixed total problem size
- `Throughput` - tasks/time
- `latency` - time/task
- `speedup` - sequential time/parallel time for execution
- `Efficiency` - how well addion resources are utilized
  - `speedup / number of processors`

- `Amdahl's law` - 
  - `overall speedup = 1/(1-P) + P/S`
  - P = portion of program that is parallizable
  - S = speedup of the parallelized portion
  - calculates the upper limit of overall speedup

# Designing Parallel Program

- `Partitioning` - break down problem to discrete chunks of work
  - `domain(data) decomposition` - divides data into atomic data
    - block decompisition
    - cyclic decompsition(round robin)
  - `functional decomposition` - consider the computation to be performed and associate them with the data involved
- `Communication` - coordinate task execution and share information
  - Point-to-Point Communication - sender and reciever to share information
  - Collective Communication - broadcast data to all tasks or scatters and gathers up data for specific tasks
  - Synchronous Blocking Communication - tasks wait until entire communication is complete
  - Asynchronous nonblocking communication - tasks do not need to wait for communication to be complete
  - Overhead - compute time/resources spent on communciation
  - Latency - time tos end message from A to B
  - Bandwidth - Amount of data communicated per second
- `Agglomeration` - Combine tasks and replicate data/computation to increase efficiency
  - Granularity = computation/communication
    - Fine-Grained - large number of small tasks good for distribution of worklaod
      - low computation-to-communication ratio
    - Coarse Graned Parallelism - small number of large tasks
      - high computation to communication ratio
      - longer processing time per task
- `Mapping`