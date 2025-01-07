from collections import deque
# Define the state of the jugs (x, y) where:
# x is the amount of water in the 4-gallon jug
# y is the amount of water in the 3-gallon jug
def water_jug_problem(capacity1, capacity2, target):
    # Create a queue for BFS
    queue = deque()
    # Set to store visited states
    visited = set()
    # Initialize the queue with the initial state (0, 0)
    queue.append((0, 0, []))  # (amount in Jug1, amount in Jug2, steps taken)
    visited.add((0, 0))
    while queue:
        jug1, jug2, steps = queue.popleft()
        # If we reach the target, return the steps
        if jug1 == target:
            return steps
        # Generate all possible next steps:
        possible_states = [
            (capacity1, jug2, steps + ['Fill Jug1']),  # Fill Jug1
            (jug1, capacity2, steps + ['Fill Jug2']),  # Fill Jug2
            (0, jug2, steps + ['Empty Jug1']),  # Empty Jug1
            (jug1, 0, steps + ['Empty Jug2']),  # Empty Jug2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2), steps + ['Pour Jug1 into Jug2']),  # Pour Jug1 into Jug2
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1), steps + ['Pour Jug2 into Jug1'])  # Pour Jug2 into Jug1
        ]
        # Add valid states to the queue
        for new_jug1, new_jug2, new_steps in possible_states:
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                queue.append((new_jug1, new_jug2, new_steps))
    # If no solution is found
    return None
# Main function
if _name_ == "_main_":
    capacity1 = 4  # capacity of Jug1 (4-gallon jug)
    capacity2 = 3  # capacity of Jug2 (3-gallon jug)
    target = 2  # target amount to measure in Jug1
    # Solve the problem
    solution = water_jug_problem(capacity1, capacity2, target)
    # Print the solution steps
    if solution:
        print("Solution found:")
for step in solution:
            print(step)
    else:
        print("No solution exists.")
