# Source: https://leetcode.com/discuss/interview-question/1595274/Microsoft-or-Online-Assessment-or-Questions
import queue

def find_minimum_number_of_filters_to_reduce_emissions(array: list[int]) -> int:

    # calculate half of emissions (target value)
    current_emission = sum(array)
    emission_target = sum(array) / 2

    priority_queue = queue.PriorityQueue()

    for element in array:
        priority_queue.put(- element) # invert the index, as priority queue goes from lowest to highest

    number_of_filters_installed = 0

    while current_emission > emission_target:
        number_of_filters_installed += 1
        max_emission = abs(priority_queue.get())
        reduced_emission = max_emission / 2

        current_emission = current_emission - max_emission + reduced_emission
        priority_queue.put(- reduced_emission) # invert the index, as priority queue goes from lowest to highest

    return number_of_filters_installed

array = [5, 19, 8, 1]
print(find_minimum_number_of_filters_to_reduce_emissions(array))