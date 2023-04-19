from simulation import simulation, random_scheduler
import sys
from typing import Union, List


# resources
dict_of_process = {}
dict_of_prioritized_process = {}

# Loads the number of processors and the list of
# process runtimes from the file with the given
# filename.
def load_data(filename: str) -> Union[int, List[int]]:

    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')
        processes = [ int(datum) for datum in data]
        no_processors = processes[0]
    return no_processors, processes[1:]

def get_keys_by_value(dict_of_elements, value_to_find):
    list_of_keys = list()
    list_of_items = dict_of_elements.items()
    for item in list_of_items:
        if item[1] == value_to_find:
            list_of_keys.append(item[0])
    return list_of_keys


# A scheduler that assigns the next process with the shortest processing time.
# The next-available processor is assigned.
def shortest_process_first_scheduler(processes, processors):
    # if empty, create a dictionary as large as the processors, w/ key(processors) and values(process) = 0
    if len(dict_of_prioritized_process) == 0:
        for i in range(len(processors)):
            dict_of_prioritized_process[i] = 0
    list_of_keys = get_keys_by_value(dict_of_prioritized_process, 0)  # get all keys with values(process) = 0
    if len(list_of_keys) > 0:  # if there are processor with process 0
        next_processor = list_of_keys.pop(0)  # get the first key with process zero and remove it from the list
        index_of_smallest_time = processes.index(min(processes))  # get index of the smallest element of the list
        dict_of_prioritized_process[next_processor] = min(processes)  # associate smallest process and 1st key value 0
        return index_of_smallest_time, next_processor  # next process index is the index of the smallest... next processor is the next key with value 0
    else:  # if all the processors are being used
        first_process_to_finish = min(dict_of_prioritized_process.values())  # find the first to finish
        index_of_smallest_element_in_process = processes.index(min(processes))
        for i in range(len(dict_of_prioritized_process)):  # refresh the remaining time of processes, and remember it
            dict_of_prioritized_process[i] = dict_of_prioritized_process[i] - first_process_to_finish
        key_of_process_to_finish = get_keys_by_value(dict_of_prioritized_process, 0)[0]  # verify the key of the process than get to 0 in that time
        dict_of_prioritized_process[key_of_process_to_finish] = processes[index_of_smallest_element_in_process]  # upload the processor that finished with the new starting process
        return index_of_smallest_element_in_process, key_of_process_to_finish


# A scheduler that assigns processes in the order they are
# presented, to the first available processor
def first_come_first_served_scheduler(processes, processors):
    if len(dict_of_process) == 0: #if empty, create a dictionary as large as the processors, w/ key(processors) and values(process) = 0
        for i in range(len(processors)):
            dict_of_process[i] = 0
    list_of_keys = get_keys_by_value(dict_of_process, 0) #get all keys with values(process) = 0
    if len(list_of_keys) > 0: #if there are processor with process 0
        next_processor = list_of_keys.pop(0) #get the first key with process zero and remove it from the list
        dict_of_process[next_processor] = processes[0] #associate first process with the first key with value 0
        return 0, next_processor #next process index is always 0, next processor is the next key with value 0
    else: #if all the processors are being used
        first_process_to_finish = min(dict_of_process.values()) #find the first to finish (considering time to pass, not total value)
        key_of_process_to_finish = get_keys_by_value(dict_of_process, first_process_to_finish) #verify the key of the first process to finish
        for i in range(len(dict_of_process)): #refresh the remaining time of processes, and remember it
            dict_of_process[i] -= first_process_to_finish
        dict_of_process[key_of_process_to_finish[0]] = processes[0] #upload the processor that finished with the new starting process
        return 0, key_of_process_to_finish[0]


# A program that runs the simulation using three different
# schedulers, and displays the wait time statistics for
# each one.
if __name__ == "__main__":

    num_processors, processes = load_data(filename=sys.argv[1])

    print("SIM 1: random scheduler")
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, random_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 2: first-come-first-served scheduler")
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, first_come_first_served_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 3: shortest-process-first scheduler")
    processes_copy = [ x for x in processes ]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, shortest_process_first_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))
