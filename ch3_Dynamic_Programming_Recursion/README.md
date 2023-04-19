
# 3.1 Heuristics

In practice, solving a problem in the optimal or most accurate way may require more computational resources than are available or feasible. Algorithms implemented for such problems often use a ***heuristic.*** A technique that willingly accepts a non-optimal or less accurate solution in order to improve execution speed.

**Heuristic optimization**

A ***heuristic algorithm*** is an algorithm that quickly determines a near optimal or approximate solution. Such an algorithm can be designed to solve the ***0-1 knapsack problem***: The knapsack problem with the quantity of each item limited to 1.

A heuristic algorithm to solve the 0-1 knapsack problem can choose to always take the most valuable item that fits in the knapsack's remaining space. Such an algorithm uses the heuristic of choosing the highest value item, without considering the impact on the remaining choices. While the algorithm's simple choices are aimed at optimizing the total value, the final result may not be optimal.

```Python
Knapsack01(knapsack, itemList, itemListSize) {
   Sort itemList descending by value
   remaining = knapsack->maximumWeight
   for (i = 0; i < itemListSize; i++) {
      if (itemList[i]->weight <= remaining) {
         Put itemList[i] in knapsack
         remaining = remaining - itemList[i]->weight
      }
   }
}
```

**Self-adjusting heuristic**

A ***self-adjusting heuristic*** is an algorithm that modifies a data structure based on how that data structure is used. Ex: Many self-adjusting data structures, such as red-black trees and AVL trees, use a self-adjusting heuristic to keep the tree balanced. Tree balancing organizes data to allow for faster access.

Ex: A self-adjusting heuristic can be used to speed up searches for frequently-searched-for list items by moving a list item to the front of the list when that item is searched for. This heuristic is self-adjusting because the list items are adjusted when a search is performed.

# 3.2 Python: Heuristics

**0-1 Knapsack problem heuristic**

The general knapsack problem seeks to maximize the total value of items placed into a knapsack such that the total weight of items in the knapsack doesn't exceed a predetermined weight. The 0-1 knapsack problem imposes the restriction that each item can be added at most once. A heuristic algorithm to solve the knapsack problem first sorts items in descending order by value, and then iteratively places the most valuable items that fit within the remaining space into the knapsack until no more items can be added.

To construct a Python program to solve the knapsack problem using a heuristic, two classes are defined:

- An Item class to store each item's weight and value
- A Knapsack class to store the knapsack's maximum predetermined weight and the list of items the knapsack will hold

The heuristic is defined in the `knapsack_01()` function. To sort the original list of items by value, the operator module's `attrgetter()` function (attribute getter) is imported and used in list's `sort()` method to identify the 'value' attribute as the sorting key. The `reverse = True` argument passed to list's sort `method()` sorts the items in descending order. Then the first item of the sorted list is added to the knapsack, changing the knapsack's remaining weight. The algorithm continues until the knapsack is full or until the next item in the list weighs more than the remaining weight in the knapsack.


```python
from operator import attrgetter

class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value


class Knapsack:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items

def knapsack_01(knapsack, item_list):
    # Sort the items in descending order based on value
    item_list.sort(key = attrgetter('value'), reverse = True)

    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
            knapsack.item_list.append(item)
            remaining = remaining - item.weight

# Main program
item_1 = Item(6, 25)
item_2 = Item(8, 42)
item_3 = Item(12, 60)
item_4 = Item(18, 95)
item_list = [item_1, item_2, item_3, item_4]
initial_knapsack_list = []

max_weight = int(input('Enter maximum weight the knapsack can hold: '))

knapsack = Knapsack(max_weight, initial_knapsack_list)
knapsack_01(knapsack, item_list)

print ('Objects in knapsack')
i = 1
sum_weight = 0
sum_value = 0

for item in knapsack.item_list:
    sum_weight += item.weight
    sum_value += item.value
    print ('%d: weight %d, value %d' % (i, item.weight,item.value))
    i += 1
print()

print('Total weight of items in knapsack: %d' % sum_weight)
print('Total value of items in knapsack: %d' % sum_value)
```

# 3.3 Greed Algorithms

**Greedy algorithm**

A ***greedy algorithm*** is an algorithm that, when presented with a list of options, chooses the option that is optimal at that point in time. The choice of option does not consider additional subsequent options, and may or may not lead to an optimal solution.

```python

MakeChange(amount) {
   while (amount >= 25) {
      Add quarter
      amount = amount - 25
   }
   while (amount >= 10) {
      Add dime
      amount = amount - 10
   }
   while (amount >= 5) {
      Add nickel
      amount = amount - 5
   }
   while (amount >= 1) {
      Add penny
      amount = amount - 1
   }
}
```


The ***fractional knapsack problem*** is the knapsack problem with the potential to take each item a fractional number of times, provided the fraction is in the range [0.0, 1.0]. Ex: A 4 pound, $10 item could be taken 0.5 times to fill a knapsack with a 2 pound weight limit. The resulting knapsack would be worth $5.

While a greedy solution to the 0-1 knapsack problem is not necessarily optimal, a greedy solution to the fractional knapsack problem is optimal. First, items are sorted in descending order based on the value-to-weight ratio. Next, one of each item is taken from the item list, in order, until taking 1 of the next item would exceed the weight limit. Then a fraction of the next item in the list is taken to fill the remaining weight.

```Python
FractionalKnapsack(knapsack, itemList, itemListSize) {
   # Sort itemList descending by item's (value / weight) ratio
   remaining = knapsack->maximumWeight
   for each item in itemList {
      if (item->weight <= remaining) {
         Put item in knapsack
         remaining = remaining - item->weight
      }
      else {
         fraction = remaining / item->weight
         Put (fraction * item) in knapsack
         break
      }
   }
}
```

**Activity selection problem**

The ***activity selection problem*** is a problem where 1 or more activities are available, each with a start and finish time, and the goal is to build the largest possible set of activities without time conflicts. Ex: When on vacation, various activities such as museum tours or mountain hikes may be available. Since vacation time is limited, the desire is often to engage in the maximum possible number of activities per day.

A greedy algorithm provides the optimal solution to the activity selection problem. First, an empty set of chosen activities is allocated. Activities are then sorted in ascending order by finish time. The first activity in the sorted list is marked as the current activity and added to the set of chosen activities. The algorithm then iterates through all activities after the first, looking for a next activity that starts after the current activity ends. When such a next activity is found, the next activity is added to the set of chosen activities, and the next activity is reassigned as the current. After iterating through all activities, the chosen set of activities contains the maximum possible number of non-conflicting activities from the activities list.


# **3.4 Python: Greedy algorithm**

**Greedy algorithm**

A greedy algorithm solves a problem by assuming that the optimal choice *at a given moment* during the algorithm will also be the optimal choice overall. Greedy algorithms tend to be efficient, but certain types of problems exist where greedy algorithms don't find the *best* or *optimal* solution. However, greedy algorithms produce both efficient and optimal solutions for many problems, including the fractional knapsack problem and the activity selection problem.

**Fractional knapsack problem**

The fractional knapsack problem is similar to the regular knapsack problem, except that fractional pieces of any given item are allowed to be selected. The optimal solution can be achieved by first sorting the items by their value-to-weight ratio, in descending order. The items are then added to the knapsack in that order, taking whole units of items until only a fraction of the next item is possible. The highest fraction of that item that will fit in the knapsack is taken, and the algorithm ends.

The list's sort() method is used with a custom key function, value_to_weight_ratio(). The key function tells the sort() method what value to use to sort each item. For solving fractional knapsack problem, sort() will use the item's value divided by the item's weight. The items are sorted in descending order, so the call to sort() passes the `reverse = True` parameter.

Item objects have a `fraction` data member that is assigned with the fraction of the item (in the range [0.0, 1.0]) in the Knapsack. Items are assumed to be added fully, so fraction is assigned with 1.0 when the Item object is constructed; the value of the fraction data member is modified in the fractional_knapsack() function when only a part of the item fits in the knapsack.

3.4.1 Fractional knapsack greedy algorithm

```python
# An individual item with a weight and value
class Item:
    def __init__(self, item_weight, item_value):
        self.weight = item_weight
        self.value = item_value
        self.fraction = 1.0

# The knapsack that contains a list of items and a maximum
# total weight
class Knapsack:
    def __init__(self, weight, items):
        self.max_weight = weight
        self.item_list = items

# A key function to be used to sort the items
def value_to_weight_ratio(item):
    return item.value / item.weight

# The Fractional Knapsack algorithm.    
def fractional_knapsack(knapsack, item_list):
    # Sort the items in descending order based on value/weight
    item_list.sort(key = value_to_weight_ratio, reverse = True)

    remaining = knapsack.max_weight
    for item in item_list:
        # Check if the full item can fit into the knapsack or
        # only a fraction
        if item.weight <= remaining:
            # The full item will fit. Add the item to item_list with
            # a fraction of 1.0
            item.fraction = 1.0
            knapsack.item_list.append(item)
            remaining = remaining - item.weight

        else:
            # Only a fractional part of the item will fit. Add that
            # fraction of the item, and then exit.
            item.fraction = remaining / item.weight
            knapsack.item_list.append(item)
            break


# Main program to test the fractional knapsack algorithm.
item_1 = Item(6, 25)
item_2 = Item(8, 42)
item_3 = Item(12, 60)
item_4 = Item(18, 95)
item_list = [item_1, item_2, item_3, item_4]
initial_knapsack_list = []

# Ask the user for the knapsack's maximum capacity.
max_weight = int(input('Enter maximum weight the knapsack can hold: '))
print()

# Construct the knapsack object, then run the fractional_knapsack
# algorithm on it.
knapsack = Knapsack(max_weight, initial_knapsack_list)
fractional_knapsack(knapsack, item_list)

# Output the information about the knapsack. Show the contents
# of the knapsack, and the fraction of each item.
print ('Objects in knapsack')
i = 1
sum_weight = 0
sum_value = 0
for item in knapsack.item_list:
    sum_weight += item.weight * item.fraction
    sum_value += item.value * item.fraction
    print ('%d: %0.1f of weight %0.1f, value %0.1f' %
          (i, item.fraction, item.weight, item.value * item.fraction))
    i += 1
print()

# Display the total weight of the items as well as the total value.
print('Total weight of items in knapsack: %d' % sum_weight)
print('Total value of items in knapsack: %d' % sum_value)
```

**Activity selection problem**

The activity selection problem defines a set of "activities" (Ex: Tourist activities on a vacation), as well as when these activities start and finish (Ex: Time of day). The optimal solution will schedule the *most* activities possible without having any time conflicts.

The greedy algorithm starts by sorting the activities, using the activity finish times as the sorting key, from earliest to latest. The first activity in the list is selected and added to the set of chosen activities. The second activity in the sorted list is selected only if the activity does not conflict with the first activity. If the second activity *does* conflict with the first, then the activity is not selected. The third activity in the sorted list is selected only if the activity does not conflict with the second activity. The process continues until the entire sorted list of activities is processed.

An activity is represented with a Python class called Activity. Three data members are defined: `name`, `start_time`, and `finish_time`. A `conflicts_with()` method is also defined to determine whether or not a time conflict exists between two Activity objects.

3.4.3 Activity class for the activity selection problem

```python
class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time

    def conflicts_with(self, other_activity):
        # No conflict exists if this activity's finish_time comes
        # at or before the other activity's start_time
        if self.finish_time <= other_activity.start_time:
            return False

        # No conflict exists if the other activity's finish_time
        # comes at or before this activity's start_time
        elif other_activity.finish_time <= self.start_time:
            return False

        # In all other cases the two activity's conflict with each
        # other
        else:
            return True

# Main program to test Activity objects
activity_1 = Activity('History museum tour', 9, 10)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('Boat tour', 11, 14)

print('History museum tour conflicts with Morning mountain hike:',    
       activity_1.conflicts_with(activity_2))
print('History museum tour conflicts with Boat tour:',
       activity_1.conflicts_with(activity_3))
print('Morning mountain hike conflicts with Boat tour:',
       activity_2.conflicts_with(activity_3))
```

The `activity_selection()` function takes a list of Activity objects as a parameter and finds an optimal selection of activities using the greedy algorithm.

The algorithm uses the list's sort() method, using the key function `attrgetter` imported from the operator module. This key function allows the sort() method to sort the list based on the indicated item attribute, namely the finish_time attribute.

3.4.4 activity_selection() function

```python
from operator import attrgetter

def activity_selection(activities):

    # Start with an empty list of selected activities
    chosen_activities = []

    # Sort the list of activities in increasing order of finish_time
    activities.sort(key = attrgetter("finish_time"))

    # Select the first activity, and add it to the chosen_activities list
    current = activities[0]
    chosen_activities.append(current)

    # Process all the remaining activities, in order
    for i in range(1, len(activities)):

        # If the next activity does not conflict with
        # the most recently selected activity, select the
        # next activity
        if not activities[i].conflicts_with(current):
            chosen_activities.append(activities[i])
            current = activities[i]

    # The chosen_activities list is an optimal list of
    # activities with no conflicts
    return chosen_activities

# Program to test Activity Selection greedy algorithm. The
# start_time and finish_time are represented with integers
# (ex. "20" is 20:00, or 8:00 PM).
activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

# Use the activity_selection() method to get a list of optimal
# activities with no conflicts.               
itinerary = activity_selection(activities)
for activity in itinerary:
    # Output the activity's information.
    print('%s - start time: %d, finish time: %d' %
         (activity.name, activity.start_time, activity.finish_time))
```

```python

from operator import attrgetter

class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time

    def conflicts_with(self, other_activity):
        # No conflict exists if this activity's finish_time comes
        # at or before the other activity's start_time.
        if self.finish_time <= other_activity.start_time:
            return False

        # No conflict exists if the other activity's finish_time
        # comes at or before this activity's start_time.
        elif other_activity.finish_time <= self.start_time:
            return False

        # In all other cases the two activity's conflict with each
        # other.
        else:
            return True

def activity_selection(activities):

    # Start with an empty list of selected activities.
    chosen_activities = []

    # Sort the list of activities in increasing order of finish_time.
    activities.sort(key = attrgetter("finish_time"))

    # Select the first activity, and add it to the chosen_activities list.
    current = activities[0]
    chosen_activities.append(current)

    # Process all the remaining activities, in order.
    for i in range(1, len(activities)):

        # If the next activity does not conflict with
        # the most recently selected activity, select the
        # next activity.
        if not activities[i].conflicts_with(current):
            chosen_activities.append(activities[i])
            current = activities[i]

    # The chosen_activities list is an optimal list of
    # activities with no conflicts.
    return chosen_activities


# Program to test Activity Selection greedy algorithm. The
# start_time and finish_time are represented with integers
# (ex. "20" is 20:00, or 8:00 PM).
activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

# Use the activity_selection() method to get a list of optimal
# activities with no conflicts.               
itinerary = activity_selection(activities)
for activity in itinerary:
    # Output the activity's information.
    print('%s - start time: %d, finish time: %d' %
         (activity.name, activity.start_time, activity.finish_time))
```

```python

from operator import attrgetter

class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time

    def conflicts_with(self, other_activity):
        # No conflict exists if this activity's finish_time comes
        # at or before the other activity's start_time.
        if self.finish_time <= other_activity.start_time:
            return False

        # No conflict exists if the other activity's finish_time
        # comes at or before this activity's start_time.
        elif other_activity.finish_time <= self.start_time:
            return False

        # In all other cases the two activity's conflict with each
        # other.
        else:
            return True

def activity_selection(activities):

    # Start with an empty list of selected activities.
    chosen_activities = []

    # Sort the list of activities in increasing order of finish_time.
    activities.sort(key = attrgetter("finish_time"))

    # Select the first activity, and add it to the chosen_activities list.
    current = activities[0]
    chosen_activities.append(current)

    # Process all the remaining activities, in order.
    for i in range(1, len(activities)):

        # If the next activity does not conflict with
        # the most recently selected activity, select the
        # next activity.
        if not activities[i].conflicts_with(current):
            chosen_activities.append(activities[i])
            current = activities[i]

    # The chosen_activities list is an optimal list of
    # activities with no conflicts.
    return chosen_activities


# Program to test Activity Selection greedy algorithm. The
# start_time and finish_time are represented with integers
# (ex. "20" is 20:00, or 8:00 PM).
activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

# Use the activity_selection() method to get a list of optimal
# activities with no conflicts.               
itinerary = activity_selection(activities)
for activity in itinerary:
    # Output the activity's information.
    print('%s - start time: %d, finish time: %d' %
         (activity.name, activity.start_time, activity.finish_time))
```

# **3.5 Dynamic programming**

**Dynamic programming overview**

***Dynamic programming*** is a problem solving technique that splits a problem into smaller subproblems, computes and stores solutions to subproblems in memory, and then uses the stored solutions to solve the larger problem. Ex: Fibonacci numbers can be computed with an iterative approach that stores the 2 previous terms, instead of making recursive calls that recompute the same term many times over.


# **3.6 Python: Dynamic programming**

**Dynamic programming for the longest common substring problem**

```python
def longest_common_substring(str1, str2):

    # Create the matrix as a list of lists.
    matrix = []
    for i in range(len(str1)):
        # Each row is started as a list of zeros.
        matrix.append([0] * len(str2))

    # Variables to remember the largest value, and the position it
    # occurred at.
    max_value = 0
    max_value_row = 0
    max_value_col = 0
    for row in range(len(str1)):
        for col in range(len(str2)):

            # Check if the characters match
            if str1[row] == str2[col]:
                # Get the value in the cell that's up and to the
                # left, or 0 if no such cell
                up_left = 0
                if row > 0 and col > 0:
                    up_left = matrix[row - 1][col - 1]

                # Set the value for this cell
                matrix[row][col] = 1 + up_left
                if matrix[row][col] > max_value:
                    max_value = matrix[row][col]
                    max_value_row = row
                    max_value_col = col
            else:
                matrix[row][col] = 0

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1,
    # up to and including max_value_col.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_col + 1]
```

3.6.2: A space-saving optimized version of the longest common substring algorithm

```python
def longest_common_substring_optimized(str1, str2):
    # Create one row of the matrix.
    matrix_row = [0] * len(str2)

    # Variables to remember the largest value, and the row it
    # occurred at.
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        # Variable to hold the upper-left value from the
        # current matrix position.
        up_left = 0
        for col in range(len(str2)):
            # Save the current cell's value; this will be up_left
            # for the next iteration.
            saved_current = matrix_row[col]

            # Check if the characters match
            if str1[row] == str2[col]:
                matrix_row[col] = 1 + up_left

                # Update the saved maximum value and row,
                # if appropriate.
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0

            # Update the up_left variable
            up_left = saved_current

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1,
    # up to and including max_value_row.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]
```

# **3.8 Greedy Algorithm: Creating A Meal Plan**

Heuristic used

- For each food item in the list:
    - add the food if:
        - it is not "empty" (too few calories or too few of the target nutrient), and
        - an entire serving can be added, or
        - an entire serving can't be added, but there is a fraction of a serving that doesn't violate either constraint (total calories or percent nutrient)
    - if the food item was added, check if the meal plan meets both the target calorie content and the percent nutrient content (within acceptable thresholds, as described below)
        - if the meal plan meets the requirements, exit the loop; otherwise continue to the next food item
- display the final meal plan

## Details

- A meal plan matches the calorie limit if total calories fall in the range [1999.9, 2000.1].
- A meal plan matches the nutrient goal if the total percent calories of the target nutrient comes within 0.1%. Ex. If the goal is 30% protein, a protein calorie content in the range [29.9%, 30.1%] is successful.
- Only allow fractional servings greater than or equal to 0.05.
- Only include `Food` objects with a calorie content greater than or equal to 0.1.
- Only include `Food` objects that are greater than or equal to 0.1% calories by the selected nutrient. Ex. If the selected nutrient is protein, ignore `Food` items where `protein_calories / calories < 0.001`.

# **3.9 Improving An Application**

One of the jobs of an operating system is to schedule processes to run on one or more processors available to the system. The operating system can decide which process to run next, and on which processor, in a number of different ways. This lab explores some different scheduling algorithms and measures their effectiveness.

You are given a program that schedules processes randomly. Your task is to implement two different scheduling algorithms that can process the same inputs in a shorter total time, and with lower overall process wait time.
