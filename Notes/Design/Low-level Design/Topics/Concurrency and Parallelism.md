# Concurrency and Parallelism

Concurrency and parallelism are key concepts in low-level design and programming. They refer to techniques that help manage multiple tasks or threads that overlap in execution time.

**Concurrency** refers to the concept of making progress together where multiple tasks start, run, and complete in overlapping time periods, in no specific order. Concurrency does not always mean that these multiple tasks will be executing at the exact same time. For example, single-core CPUs use context switching to provide concurrent execution of threads or processes. 

**Parallelism**, on the other hand, is the concept where multiple tasks or even parts of a unique task literally run at the same time, e.g., on a multi-core processor.

Let's delve a bit deeper into these concepts:

1. **Multithreading**: Multithreading is a widespread programming and execution model that allows multiple threads to exist within the context of one process. These threads share the process's resources but are able to execute independently. In Python, the `threading` module built on top of `_thread` module provides a higher level, more pythonic approach to work with threads.

Example:
```python
import threading
  
def print_cube(num):
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")
```

2. **Multiprocessing**: Python’s Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecodes at a time even in a multi-threaded architecture. To bypass this, Python has a multiprocessing module. This module bypasses the GIL by creating processes. Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem.

Example:
```python
import multiprocessing
  
def print_cube(num):
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
  
    # both processes finished
    print("Done!")
```

3. **Asynchronous programming (async/await)**: Python 3.5 introduced the async and await keywords (functions and syntax) to define coroutines. Python’s asyncio module provides a framework that revolves around the event loop. An event loop basically waits for something to happen and then acts on the event. An example of this is handling I/O-bound tasks more efficiently.

Example:
```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

# Python 3.7+
asyncio.run(main())
```
In this example, `asyncio.sleep()` is also a coroutine, and await can be used to wait for its completion.

These techniques allow you to manage the execution of multiple tasks in your program, potentially improving performance, responsiveness, and giving you better control over resource utilization. However, they also add complexity to your program and can lead to issues like race conditions or deadlocks if not managed properly. Therefore, understanding the principles of concurrency and parallelism is essential for designing and implementing efficient and effective programs.

Deciding which technique to use—multithreading, multiprocessing, or asynchronous programming—depends on the type of problem you are trying to solve.

- **I/O-bound problems**: If your program spends most of its time talking to a slow device (like a network connection, a hard drive, or a printer), you're probably dealing with an I/O-bound problem. I/O-bound programs often benefit from using threads or asynchronous I/O to achieve concurrent execution. This is because while one thread is waiting for the I/O to complete, other threads can continue their work, or in asynchronous I/O, the I/O operations are non-blocking, so you can do other work while waiting for I/O operations to complete.

- **CPU-bound problems**: If your program spends most of its time doing computations, you're probably dealing with a CPU-bound problem. These programs often benefit from multiprocessing, which allows for parallel execution across multiple CPUs or cores and can result in a significant speedup.

Now let's discuss how to handle issues like race conditions or deadlocks:

- **Race Conditions**: A race condition occurs when two or more threads can access shared data and they try to change it at the same time. As a result, the values of variables may be unpredictable and vary depending on the timings of context switches of the processes.

  A common way to prevent race conditions is to use locks (or Mutex). A lock allows only one thread to enter the part that's handling the shared data. Python's threading module provides a Lock class to deal with the race conditions. Python's `queue` module also provides a thread-safe FIFO implementation.

- **Deadlocks**: A deadlock occurs when two or more processes are unable to proceed because each is waiting for the other to release a resource. For example, if you have two locks and two threads, and each thread acquires one lock and then tries to acquire the other, a deadlock occurs.

  Avoiding deadlocks can be tricky, but the following principles (the Coffman conditions) can help:

   1. Mutual Exclusion: Only one process can use a resource at a given instant of time.
   2. Hold and Wait: A process can request for a resource while holding other resources.
   3. No Preemption: No process can forcefully remove another process's resource.
   4. Circular Wait: Two or more processes form a circular chain where each process waits for a resource that the next process in the chain holds.

  If these four conditions hold simultaneously, then a deadlock can occur. By negating any one of the conditions, we can prevent deadlocks.

  For instance, we can impose an order on the acquisition of locks (negating the circular wait condition). If all threads always acquire their locks in the same order, deadlocks cannot occur. Python's standard library provides a `RLock` ("reentrant lock") object for more complex locking situations.

Remember, concurrency and parallelism are powerful tools, but they should be used judiciously. In many cases, simpler, single-threaded or single-process solutions are more appropriate and can avoid many of these complexities.

## QnAs

Sure, here are some interview questions and answers about concurrency and parallelism in low-level system design:

1. **What's the difference between parallelism and concurrency?**

   Parallelism and concurrency are two terms often used interchangeably, but they denote subtly different concepts. Parallelism is about doing lots of things at once, leveraging multiple processors to perform multiple tasks simultaneously. Concurrency, on the other hand, deals with managing access to shared state from multiple threads in a way that these threads can run independently without interfering with each other.

2. **What are threads and how are they different from processes?**

   Threads are the smallest unit of execution that can be scheduled by an operating system. A process is an instance of a program that is being executed and may consist of multiple threads. The main difference between them is that all threads within a process share the same memory space, while separate processes do not.

3. **What is a race condition and how can you avoid it?**

   A race condition occurs when two or more threads can access shared data and they try to change it at the same time. It leads to unpredictable and undesirable outcomes. To avoid race conditions, you can use synchronization techniques such as locks, semaphores, or mutexes to ensure that only one thread can access the shared data at a time.

4. **What is a deadlock and how can you prevent it?**

   A deadlock is a situation where two or more threads are blocked forever, each waiting for the other to release a lock. Deadlocks can be prevented by avoiding the four Coffman conditions for deadlocks which are mutual exclusion, hold and wait, no preemption, and circular wait.

5. **What is the Global Interpreter Lock (GIL) in Python and how does it affect concurrency?**

   The Global Interpreter Lock (GIL) is a mechanism used in the CPython interpreter to synchronize access to Python objects, preventing multiple native threads from executing Python bytecodes at once. It can be a limiting factor for concurrency because it allows only one thread to execute Python bytecodes at a time even in a multi-threaded architecture.

6. **What's the difference between blocking I/O and non-blocking I/O?**

   In a blocking I/O operation, the execution thread is blocked and doesn't regain control until the operation completes. In contrast, a non-blocking I/O operation returns immediately, allowing the thread to continue its operation while the I/O operation is performed in the background.

Remember to provide answers based on your own experiences and understanding of these topics.

Sure, here are a few more interview questions and potential answers on Concurrency and Parallelism:

1. **What is a semaphore and how is it used in concurrency?**

   A semaphore is a synchronization mechanism used to control access to a common resource by multiple processes or threads in a concurrent system such as a multitasking operating system. A semaphore has a counter which is incremented or decremented as threads acquire or release access to the resource. If the counter is 0, threads trying to acquire the resource will block until the counter is greater than 0.

2. **What is the difference between a mutex and a semaphore?**

   A mutex (short for mutual exclusion) is a synchronization primitive that ensures that only one thread is able to execute a specific section of code at a time (critical section). A semaphore is a more generalized form of a mutex that can be used to control access to multiple instances of a resource.

3. **What is livelock and how does it differ from a deadlock?**

   A livelock is a situation where two or more threads continually repeat the same operation without making progress, because they are all blocked by each other. It differs from deadlock in that threads in a livelock are not blocked from executing—they are simply unable to make progress.

4. **What is asynchronous programming and how does it relate to concurrency?**

   Asynchronous programming is a programming paradigm where operations are executed out of sync with the main program flow, allowing the program to continue executing without waiting for those operations to complete. Asynchronous programming is one way to achieve concurrency, particularly in I/O-bound applications.

5. **What is the "Dining Philosophers" problem and what does it illustrate about concurrent systems?**

   The "Dining Philosophers" problem is a classic computer science problem that deals with synchronization issues in concurrent programming. It involves a group of philosophers sitting at a circular table with one chopstick between each pair. Each philosopher needs both chopsticks to eat but can only pick up one at a time. This problem illustrates the challenges of deadlock and resource contention in concurrent systems.

6. **What is the purpose of Python's `threading` and `multiprocessing` libraries?**

   Python's `threading` library is used for running multiple threads (lightweight processes) in the same process space. However, because of Python's Global Interpreter Lock (GIL), true parallelism is not achieved with `threading`. 

   On the other hand, Python's `multiprocessing` library spawns multiple processes and leverages multiple processors for parallel computation, bypassing the GIL. It introduces a little more overhead than threading because new processes need to be spawned and inter-process communication is more complex than inter-thread communication.

Remember, the answers to these questions can depend on the specific technology stack you're using, and it's good to give examples from your own experience where possible.

Sure, here are a few more interview questions and potential answers on Concurrency and Parallelism:

1. **What is the Global Interpreter Lock (GIL) in Python and how does it impact concurrency and parallelism?**

   The Global Interpreter Lock, or GIL, is a part of CPython's (Python's standard interpreter) memory-management system. It ensures that only one thread executes Python bytecodes at a time in a single process. This means that even on a multi-threaded Python program, only one thread is executed at a time. This limits the efficiency of CPU-bound programs. However, for I/O-bound programs, it is not a bottleneck as the lock can be released while waiting for I/O.

2. **Explain the difference between parallel and concurrent programming.**

   Parallel programming is a type of computation where many calculations or processes are carried out simultaneously, typically to be run on multi-core processors. It is about doing lots of things at once.

   Concurrent programming, on the other hand, deals with lots of things at once but not necessarily does it mean they're executing simultaneously. In concurrent programming, the execution of processes is non-deterministic and the order of execution may be different each time the program is run.

3. **What are some strategies to avoid race conditions in a multithreaded application?**

   There are several strategies to avoid race conditions in a multithreaded application: 

   - Mutexes: Mutexes (or locks) can be used to ensure that only one thread accesses a piece of code or data at a time.
   - Semaphores: Like mutexes, semaphores also restrict access to shared resources but can allow more than one thread to access a resource at a time.
   - Condition variables: These are used to synchronize the execution flow of threads based on certain conditions.
   - Atomic operations: These are operations that complete in a single operation without the possibility of interruption.

4. **Explain the concept of a thread-safe function.**

   A thread-safe function is a function that can be called from multiple threads simultaneously and it operates correctly in a multithreaded environment. This typically means that the function either does not use shared data (and hence doesn't need to worry about data races), or it uses synchronization mechanisms such as locks to protect shared data.

5. **Explain Python's `asyncio` module and its use in concurrent programming.**

   Python's `asyncio` is a library that provides support for handling asynchronous I/O through coroutines and multiplexing I/O access over sockets and other resources. It is built on top of Python's async and await language features. `asyncio` allows for high-performance networking and other I/O-bound tasks with relatively simple syntax, allowing you to write single-threaded concurrent programs.

Remember, these are complex topics and the depth of your answer would depend on the position you're applying for. Always tailor your responses to the job requirements and your personal experience.