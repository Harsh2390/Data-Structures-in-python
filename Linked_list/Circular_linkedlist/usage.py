"""
Example usage of the CircularLinkedList class.
"""

from Clinkedlist import CircularLinkedList


def basic_usage():
    """
    Demonstrate basic usage of the CircularLinkedList class.
    """
    print("=== Basic Usage ===")
    
    # Create a new circular linked list
    cll = CircularLinkedList()
    print(f"Empty list: {cll}")
    
    # Add elements
    cll.append(1)
    cll.append(2)
    cll.append(3)
    print(f"After appending 1, 2, 3: {cll}")
    
    # Prepend an element
    cll.prepend(0)
    print(f"After prepending 0: {cll}")
    
    # Insert at a specific position
    cll.insert_at(2, 1.5)
    print(f"After inserting 1.5 at index 2: {cll}")
    
    # Remove an element
    cll.remove(1.5)
    print(f"After removing 1.5: {cll}")
    
    # Remove at a specific position
    cll.remove_at(1)
    print(f"After removing element at index 1: {cll}")
    
    # Get element at a specific position
    value = cll.get_at(1)
    print(f"Element at index 1: {value}")
    
    # Find an element
    index = cll.find(2)
    print(f"Index of element 2: {index}")
    
    # Check if an element exists
    print(f"Contains 2: {2 in cll}")
    print(f"Contains 5: {5 in cll}")
    
    # Get the size of the list
    print(f"Size: {len(cll)}")
    
    # Iterate through the list
    print("Iterating through the list:")
    for item in cll:
        print(f"  {item}")
    
    # Convert to a Python list
    python_list = cll.to_list()
    print(f"As Python list: {python_list}")
    
    # Create from a Python list
    new_cll = CircularLinkedList.from_list([5, 6, 7, 8])
    print(f"New list from [5, 6, 7, 8]: {new_cll}")
    
    # Rotate the list
    new_cll.rotate(2)
    print(f"After rotating by 2 positions: {new_cll}")
    
    # Clear the list
    cll.clear()
    print(f"After clearing: {cll}")


def round_robin_scheduler():
    """
    Demonstrate a round-robin scheduler using a circular linked list.
    """
    print("\n=== Round-Robin Scheduler ===")
    
    tasks = ["Task A", "Task B", "Task C", "Task D"]
    time_quantum = 2
    
    # Initialize tasks with their remaining time
    task_list = CircularLinkedList()
    for task in tasks:
        task_list.append({"name": task, "remaining_time": 10})  # Each task needs 10 time units
    
    current_time = 0
    executed_tasks = []
    
    print(f"Tasks: {tasks}")
    print(f"Time quantum: {time_quantum}")
    print("Execution sequence:")
    
    # Process until all tasks are completed
    while not task_list.is_empty():
        current_task = next(iter(task_list))
        
        # Execute the task for the time quantum or until completion
        execution_time = min(time_quantum, current_task["remaining_time"])
        current_task["remaining_time"] -= execution_time
        current_time += execution_time
        
        print(f"  Time {current_time}: Executed task '{current_task['name']}' for {execution_time} units")
        executed_tasks.append(current_task["name"])
        
        # If the task is completed, remove it from the list
        if current_task["remaining_time"] <= 0:
            task_list.remove(current_task)
            print(f"  Task '{current_task['name']}' completed")
        else:
            # Rotate to the next task
            task_list.rotate(1)
    
    print(f"Total execution time: {current_time}")
    print(f"Task execution sequence: {executed_tasks}")


def josephus_problem():
    """
    Solve the Josephus problem using a circular linked list.
    
    In the Josephus problem, n people are standing in a circle. Counting begins at a specified point
    and proceeds around the circle in a specified direction. After a specified number of people are
    skipped, the next person is eliminated. The procedure is repeated with the remaining people,
    starting with the next person, going in the same direction and skipping the same number of people,
    until only one person remains.
    """
    print("\n=== Josephus Problem ===")
    
    n = 7  # Number of people
    k = 3  # Count every kth person
    
    # Create a circular linked list with n people
    people = CircularLinkedList.from_list(list(range(1, n + 1)))
    print(f"Initial circle: {people}")
    
    print(f"Eliminating every {k}th person:")
    
    # Eliminate people until only one remains
    while len(people) > 1:
        # Move to the k-th person (k-1 steps)
        people.rotate(k - 1)
        
        # Eliminate the current person
        eliminated = people.remove_at(0)
        print(f"  Eliminated person {eliminated}")
    
    survivor = people.get_at(0)
    print(f"Survivor: Person {survivor}")


def media_playlist():
    """
    Simulate a media playlist using a circular linked list.
    """
    print("\n=== Media Playlist ===")
    
    # Create a playlist
    playlist = CircularLinkedList.from_list([
        "Song A",
        "Song B",
        "Song C",
        "Song D",
        "Song E"
    ])
    
    print(f"Playlist: {playlist}")
    
    # Simulate playing 10 songs in a loop
    print("Playing songs:")
    
    current_song_index = 0
    for i in range(10):
        song = playlist.get_at(current_song_index)
        print(f"  {i+1}. Now playing: {song}")
        
        # Move to the next song (circular)
        current_song_index = (current_song_index + 1) % len(playlist)


if __name__ == "__main__":
    basic_usage()
    round_robin_scheduler()
    josephus_problem()
    media_playlist()