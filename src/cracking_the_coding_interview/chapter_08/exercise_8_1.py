"""
Triple Step:
 A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
"""

def run_stairs(n):
    if n == 0:
        return 1

    number_of_combinations = 0
    if n >= 3:
        number_of_combinations +=  run_stairs(n-3)
    if n >= 2:
        number_of_combinations += run_stairs(n-2)
    if n >= 1:
        number_of_combinations += run_stairs(n-1)
    return number_of_combinations


def main():
    number_of_combinations = run_stairs(10)
    print("Number of possible combinations: %s" %(number_of_combinations))


if __name__ == "__main__":
    main()