# Chapter 2

**Algorithms for data structures**

Data structures not only define how data is organized and stored, but also the operations performed on the data structure. While common operations include inserting, removing, and searching for data, the algorithms to implement those operations are typically specific to each data structure. Ex: Appending an item to a linked list requires a different algorithm than appending an item to an array.

**Algorithms using data structures**

Some algorithms utilize data structures to store and organize data during the algorithm execution. Ex: An algorithm that determines a list of the top five salespersons, may use an array to store salespersons sorted by their total sales.

# Chapter 2.2 Constant time operations

**Constant time operations**

In practice, designing an efficient algorithm aims to lower the amount of time that an algorithm runs. However, a single algorithm can always execute more quickly on a faster processor. Therefore, the theoretical analysis of an algorithm describes runtime in terms of number of constant time operations, not nanoseconds. A ***constant time operation*** is an operation that, for a given processor, always operates in the same amount of time, regardless of input values.

# **2.3 Algorithm efficiency**

**Algorithm efficiency**

An algorithm describes the method to solve a computational problem. Programmers and computer scientists should use or write efficient algorithms. ***Algorithm efficiency*** is typically measured by the algorithm's computational complexity. ***Computational complexity*** is the amount of resources used by the algorithm. The most common resources considered are the runtime and memory usage.


**Runtime complexity, best case, and worst case**

An algorithm's ***runtime complexity*** is a function, T(N), that represents the number of constant time operations performed by the algorithm on an input of size N. Runtime complexity is discussed in more detail elsewhere.

Because an algorithm's runtime may vary significantly based on the input data, a common approach is to identify best and worst case scenarios. An algorithm's ***best case*** is the scenario where the algorithm does the minimum possible number of operations. An algorithm's ***worst case*** is the scenario where the algorithm does the maximum possible number of operations.

**Space complexity**

An algorithm's ***space complexity*** is a function, S(N), that represents the number of fixed-size memory units used by the algorithm for an input of size N. Ex: The space complexity of an algorithm that duplicates a list of numbers is S(N) = N + k, where k is a constant representing memory used for things like the loop counter and list pointers.

Space complexity includes the input data and additional memory allocated by the algorithm. An algorithm's ***auxiliary space complexity*** is the space complexity not including the input data. Ex: An algorithm to find the maximum number in a list will have a space complexity of S(N) = N + k, but an auxiliary space complexity of S(N) = k, where k is a constant.

# **2.4 Growth of functions and complexity**

**Upper and lower bounds**

An algorithm with runtime complexity T(N) has a lower bound and an upper bound.

- ***Lower bound***: A function f(N) that is ≤ the best case T(N), for all values of N ≥ 1.
- ***Upper bound***: A function f(N) that is ≥ the worst case T(N), for all values of N ≥ 1.

**Growth rates and asymptotic notations**

An additional simplification can factor out the constant from a bounding function, leaving a function that categorizes the algorithm's growth rate. Ex: Instead of saying that an algorithm's runtime function has an upper bound of $30N^2$, the algorithm could be described as having a worst case growth rate of $N^2$. ***Asymptotic notation*** is the classification of runtime complexity that uses functions that indicate only the growth rate of a bounding function. Three asymptotic notations are commonly used in complexity analysis:

- ***O notation*** provides a growth rate for an algorithm's upper bound.
- ***Ω notation*** provides a growth rate for an algorithm's lower bound.
- ***Θ notation*** provides a growth rate that is both an upper and lower bound.

# **2.5 O notation**

**Big O notation**

***Big O notation*** is a mathematical way of describing how a function (running time of an algorithm) generally behaves in relation to the input size. In Big O notation, all functions that have the same growth rate (as determined by the highest order term of the function) are characterized using the same Big O notation. In essence, all functions that have the same growth rate are considered equivalent in Big O notation.

Given a function that describes the running time of an algorithm, the Big O notation for that function can be determined using the following rules:

1. If f(N) is a sum of several terms, the highest order term (the one with the fastest growth rate) is kept and others are discarded.
2. If f(N) has a term that is a product of several factors, all constants (those that are not in terms of N) are omitted.

**Runtime growth rate**

One consideration in evaluating algorithms is that the efficiency of the algorithm is most critical for large input sizes. Small inputs are likely to result in fast running times because N is small, so efficiency is less of a concern. The table below shows the runtime to perform f(N) instructions for different functions f and different values of N. For large N, the difference in computation time varies greatly with the rate of growth of the function f. The data assumes that a single instruction takes 1 μs to execute.


**Common Big O complexities**

Many commonly used algorithms have running time functions that belong to one of a handful of growth functions. These common Big O notations are summarized in the following table. The table shows the Big O notation, the common word used to describe algorithms that belong to that notation, and an example with source code. Clearly, the best algorithm is one that has constant time complexity. Unfortunately, not all problems can be solved using constant complexity algorithms. In fact, in many cases, computer scientists have proven that certain types of problems can only be solved using quadratic or exponential algorithms.


| Notation | Name | Example pseudocode |
| --- | --- | --- |
| O(1) | Constant | FindMin(x, y) {
   if (x < y) {
      return x
   }
   else {
      return y
   }
} |
| O(log N) | Logarithmic | BinarySearch(numbers, N, key) {
   mid = 0
   low = 0
   high = N - 1

   while (high >= low) {
      mid = (high + low) / 2
      if (numbers[mid] < key) {
         low = mid + 1
      }
      else if (numbers[mid] > key) {
         high = mid - 1
      }
      else {
         return mid
      }
   }

   return -1   // not found
} |
| O(N) | Linear | LinearSearch(numbers, numbersSize, key) {
  for (i = 0; i < numbersSize; ++i) {
      if (numbers[i] == key) {
         return i
      }
   }

   return -1 // not found
} |
| O(N log N) | Linearithmic | MergeSort(numbers, i, k) {
   j = 0
   if (i < k) {
      j = (i + k) / 2              // Find midpoint

      MergeSort(numbers, i, j)     // Sort left part
      MergeSort(numbers, j + 1, k) // Sort right part
      Merge(numbers, i, j, k)      // Merge parts
   }
} |
| O(N2) | Quadratic | SelectionSort(numbers, numbersSize) {
   for (i = 0; i < numbersSize; ++i) {
      indexSmallest = i
      for (j = i + 1; j < numbersSize; ++j) {
         if (numbers[j] < numbers[indexSmallest]) {
            indexSmallest = j
         }
      }

      temp = numbers[i]
      numbers[i] = numbers[indexSmallest]
      numbers[indexSmallest] = temp
   }
} |
| O(cN) | Exponential | Fibonacci(N) {
  if ((1 == N) || (2 == N)) {
     return 1
  }
  return Fibonacci(N-1) + Fibonacci(N-2)
} |


# **2.6 Algorithm analysis**

**Worst-case algorithm analysis**

To analyze how runtime of an algorithm scales as the input size increases, we first determine how many operations the algorithm executes for a specific input size, N. Then, the big-O notation for that function is determined. Algorithm runtime analysis often focuses on the worst-case runtime complexity. The ***worst-case runtime*** of an algorithm is the runtime complexity for an input that results in the longest execution. Other runtime analyses include best-case runtime and average-case runtime. Determining the average-case runtime requires knowledge of the statistical properties of the expected data inputs.

**Counting constant time operations**

For algorithm analysis, the definition of a single operation does not need to be precise. An operation can be any statement (or constant number of statements) that has a constant runtime complexity, O(1). Since constants are omitted in big-O notation, any constant number of constant time operations is O(1). So, precisely counting the number of constant time operations in a finite sequence is not needed. Ex: An algorithm with a single loop that execute 5 operations before the loop, 3 operations each loop iteration, and 6 operations after the loop would have a runtime of f(N) = 5 + 3N + 6, which can be written as O(1) + O(N) + O(1) = O(N). If the number of operations before the loop was 100, the big-O notation for those operation is still O(1).

**Runtime analysis of nested loops**

Runtime analysis for nested loops requires summing the runtime of the inner loop over each outer loop iteration. The resulting summation can be simplified to determine the big-O notation.


# **2.7 Complexity classes**

**P and NP complexity classes**

A ***complexity class*** is the set of problems that can be solved using a specific amount of computational resources. By knowing the complexity class of a problem, a programmer can select an appropriate algorithm to solve a problem efficiently or know that the problem cannot be solved efficiently. Two common complexity classes are:

- The class ***P*** is the set of problems that can be solved using a *deterministic* machine in polynomial time. A Turing machine is deterministic machine, so a problem in P can be solved using a Turing machine with a polynomial runtime complexity.
- The class ***NP*** is the set of problems that can be solved using a *non-deterministic machine* in polynomial time. A non-deterministic Turing machine, while not discussed in this material, can be implemented as a deterministic Turing machine with at most an exponential increase in runtime complexity. So, problems in NP can be solved with at most exponential runtime complexity.

**NP-complete and NP-hard**

The class ***NP-complete*** is the set of problems in NP to which all other NP problems can be reduced in polynomial time. A problem $A$ is ***polynomial-time reducible*** to another problem $B$ if a polynomial-time algorithm exists that maps $A$ to $B$, such that the solution to $B$ provides the solution to $A$.

The class ***NP-hard*** is the set of problems that are at least as hard as NP-complete.

The figure below illustrates the P, NP, NP-complete, and NP-hard classes, assuming $P ≠ NP$


**Is P = NP?**

The problem of whether $P = NP$ or $P ≠ NP$ is one of the fundamental unsolved problems in computer science. Not knowing the answer to this question implies that the following answers to following questions are unknown.

1. Does an efficient algorithm exists for NP-complete problems?
2. Does a problem exist that is in NP but not in P?

While the prevailing thought is that $P ≠ NP$, no proof exists.


# **2.8 Turing machines introduction**

**Turing machines introduction**

A ***Turing machine*** is model of computer developed by Alan Turing to reason about general purpose computers.

- A Turing machine has a one-dimensional ***tape*** divided into cells, where each cell can hold one symbol from a finite ***tape alphabet*** denoted by Γ. The tape alphabet must contain a blank symbol (represented by * ) and at least one other symbol.
- The Turing machine has a head that always points to a cell of the tape. The symbol in the cell to which the head is currently pointing is called the current symbol.
- A Turing machine has a finite set of states, denoted by $Q.Q$  include three special states:  $q_0$ is the start state,  $q_{acc}$ is the accept state, and $q_{rej}$ is the reject state.
- A Turing machine's actions are defined by a transition function $\delta$. The input to the transition function is the current state and current symbol. The output of the transition function is the next state, the symbol to be written to the current cell, and the direction to move the head (L denotes move left, and R denotes move right).

A ***configuration*** of a Turing machine consists of the tape contents, current state, and tape cell currently pointed to by the head.

The Turing machine proceeds in a series of steps dictated by the transition function. Ex: The transition function $\delta(q,b) = (r, a, L)$ denotes that when the Turing machines is in state $q$ and the current symbol is 'b', the Turing machine will write 'a' to the current cell, transition to state $r$, and moves the head one cell to the left. If the head is supposed to move left and is already in the leftmost tape cell, then the head stays in the same location after the step.


# 2.10 Python: Turing machine example

**TuringMachine class**

The TuringMachine class has data members to contain the various components of a Turing Machine:

- alphabet - The finite set of symbols that can be used by the input string. Includes the blank symbol.
- tape - A list storing each character of the input string in an individual cell. The last cell contains the blank symbol.
- blank_symbol - The character used to specify a blank in the tape.
- current_state - The current state of the machine. Starts at the initial state.
- final_states - A list of states (accept and reject) that cause the machine to stop running when reached.
- transition_function - A dictionary storing the conditions of transitions as the keys and the rules of transitions as the values. Ex: `transition_function = {('q_0','a'):('q_0', 'a', 'R'), ('q_0','*'):('q_rej', '*', 'L')}`
- head_position - The position in the tape where each step through the machine begins. head_position moves forward (R) or backwards (L) each step according to the transition rules.

TuringMachine's step() method uses the rules of the defined transition function to step through and modify the tape. If the current rule requires the head position to move to the right, head_position is increased by 1. If the rule requires the head move to the left, head_position is decreased by 1. If the head_position is 0 and is supposed to move left, head_position remains 0. The step() method is continually called by the main program until a final state (accept or reject) is reached. The method final_state() returns True if a final state has been reached and False otherwise.


```python
# TuringMachine.py

class TuringMachine(object):

    def __init__(self, alphabet, tape_string, blank_symbol, initial_state,
                 final_states, transition_function):
        self.alphabet = alphabet
        self.tape = list(tape_string)
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

        self.head_position = 0
        self.tape.append(blank_symbol)


    def step(self):
        current_char = self.tape[self.head_position]
        trans_key = (self.current_state, current_char)

        # Retrieve transition rule for current configuration
        if trans_key in self.transition_function:
            trans_rule = self.transition_function[trans_key]
            self.tape[self.head_position] = trans_rule[1]
            # Move head position right or left
            if trans_rule[2] == 'R':
                self.head_position += 1
            elif trans_rule[2] == 'L' and self.head_position != 0:
                self.head_position -= 1
            self.current_state = trans_rule[0]

    def final_state(self):
        if self.current_state in self.final_states:
            return True
        else:
            return False

# main.py

from TuringMachine import TuringMachine

alphabet =['a','b', '*']

print('Enter a string using the following symbols:', end=' ')
for i in alphabet:
    print(i, end=' ')
print()
input_string = input()

# Make sure input characters are valid (in the alphabet)
for char in input_string:
    if char not in alphabet:
        print('Invalid input string.')
        exit()

initial_state = 'q_0'
final_states = ['q_acc', 'q_rej']

# Transition function
transition_function = {('q_0','a'):('q_0', 'a', 'R'),
                       ('q_0','b'):('q_1', 'b', 'R'),
                       ('q_0','*'):('q_rej', '*', 'L'),
                       ('q_1','a'):('q_1', 'a', 'R'),
                       ('q_1','b'):('q_acc', 'b', 'R'),
                       ('q_1','*'):('q_rej', '*', 'L')}

turing = TuringMachine(alphabet, input_string, '*', initial_state, final_states,
                  transition_function)

# Step through Turing machine until a final state is reached
while not turing.final_state():
    turing.step()

if turing.current_state == 'q_acc':
    print('String %s is accepted.' % input_string)
else:
    print('String %s is rejected.' % input_string)
```
