# **3.9 Improving An Application**

One of the jobs of an operating system is to schedule processes to run on one or more processors available to the system. The operating system can decide which process to run next, and on which processor, in a number of different ways. This lab explores some different scheduling algorithms and measures their effectiveness.

You are given a program that schedules processes randomly. Your task is to implement two different scheduling algorithms that can process the same inputs in a shorter total time, and with lower overall process wait time.

## Requirements

You are to write three functions:

- `load_data()` - Takes a filename as an argument, reads the file specified by the filename, and returns:
    - the number of processors to be used
    - a list of runtimes for all the processes

    The format of the data file is described below.

- Two "scheduler" functions:
    - `first_come_first_served_scheduler()`
    - `shortest_process_first_scheduler()`

The scheduler functions each take two arguments: the list of remaining process runtimes, and a list of times the processors are next available.

The purpose of a scheduler is to decide which process to start next, and which processor is to execute the process. More details on the schedulers are given below.

## The simulation and test program

The simulator is given as the function `simulation()` in the `simulation.py` file. The simulation() function has three parameters: the total number of processors, a list of integers representing the runtimes of each process, and a reference to the scheduler function. The simulation() function returns statistics that measure the efficiency of the scheduling algorithm when executing the input processes:

- total time to run all processes
- total time all processes spent waiting to be executed
- the maximum wait time amongst all the processes

The following code fragment shows how the simulation is executed.

```
from simulation import simulation, random_scheduler

# load the number of processors and the list of process run times from a file
# given on the command line
num_processors, process_run_times = load_data(sys.argv[1])

# run the simulation
statistics = simulation(num_processors, process_run_list, random_scheduler)

```

The above code fragment loads the processor, processes information from a file, and then runs the simulator using a random scheduler.

A program is provided in `main.py` that will run the simulation with each of the three schedulers. The expected statistics for the three schedulers are shown below. Do not modify the program's output in any way, as the automatic grading requires the output to be formatted exactly as shown.

## The data file format

Data files are simple text files with one integer per line. The first line is the number of processors that should be used, and each following line is the running time of a single process. Ex: A data file looks like this:

```
2
10
4
8
2
1
15

```

The above file describes a test case with 2 processors (the first line), and 6 processes with running times of 10, 4, 8, 2, 1 and 15. The running times have no units because units are not required for this lab. The time units could be seconds or milliseconds or nanoseconds, but the scale doesn't matter. The important measure is how the particular schedulers perform compared to each other.

Process runtimes are stored in a list, so calling `load_data()` with the above data file returns `(2, [10, 4, 8, 2, 1, 15])`.

Three sample data files have been added to the lab for testing. You are encouraged to make your own data files and test your code on your own computer outside of the zyLab development environment. The main program uses the data file from the filename given as a command line argument.

| Filename | Filename | Filename |
| --- | --- | --- |
| processes_input1.txt | processes_input2.txt | processes_input3.txt |
| 4 10 3 2 15 4 8 10 7 3 1 6 9 | 2 10 4 8 1 7 16 22 9 18 43 19 12 | 8 12 18 40 7 15 2 27 16 35 25 10 5 18 37 21 30 19 42 17 |
## Schedulers

A scheduler is a function that is used by the simulation to decide, when appropriate, which process is to be assigned to which processor. The first argument is the list of processes that remain and are waiting to be run. The second parameter is a list with one integer per processor; the value is the next time step that the processor is available. Ex: If two processors exist, the second argument could be `[27, 41]`, meaning the Processor 0 will be available at time step 27, and Processor 1 will be available at time step 41.

The scheduler function returns a 2-tuple containing the index of the selected process, followed by the index of the selected processor.

### Random Scheduler

The random scheduler is provided for you in the `simulation` module. The scheduler simply picks a random process and assigns the process to a random processor. The random number generator is given a seed of 123 so that the results, although random, are consistent each time the program is run. The table below shows the expected statistics on each of the data files when using the random scheduler.

|  | Data File |  |  |
| --- | --- | --- | --- |
| Statistic | processes_input1.txt | processes_input2.txt | processes_input3.txt |
| Total Time | 72 | 216 | 376 |
| Total Wait Time | 177 | 790 | 1507 |
| Max Wait Time | 33 | 99 | 179 |
| Average Wait Time | 44.25 | 395.00 | 188.38 |

### First-Come-First-Served Scheduler

A reasonable scheduler is one that always assigns the first processor that comes available, and always chooses the next process in the list. This scheduler returns the first index in the process list (zero), and the index of the first processor that will be available.

|  | Data File |  |  |
| --- | --- | --- | --- |
| Statistic | processes_input1.txt | processes_input2.txt | processes_input3.txt |
| Total Time | 39 | 180 | 118 |
| Total Wait Time | 76 | 372 | 37 |
| Max Wait Time | 15 | 83 | 242 |
| Average Wait Time | 19.00 | 186.00 | 30.25 |

### Shortest-Process-First Scheduler

Like the First-Come-First-Served scheduler, the Shortest-First scheduler picks the processor that first comes available. However, instead of just selecting the next process in the list, the scheduler always selects the process that has the *shortest* running time of all the remaining processes.
