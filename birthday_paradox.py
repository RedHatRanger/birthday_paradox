import random

def has_duplicate_birthdays(num_people, trials=10000):
    """
    Estimate the probability that among 'num_people' people,
    there is at least one pair who share the same birthday.
    
    We do this by running 'trials' simulations. In each simulation:
    - Assign random birthdays (1 through 365) to all 'num_people'.
    - Check if there's a duplicate birthday.
    - Count how many trials have at least one duplicate.

    Returns:
        A float representing the estimated probability (0 to 1).
    """
    count_duplicates = 0
    for _ in range(trials):
        # Generate a list of random birthdays for the group
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        
        # Check if there's a duplicate by comparing set and list lengths
        if len(set(birthdays)) < len(birthdays):
            count_duplicates += 1
    
    # Probability is number_of_duplicate_trials / total_trials
    return count_duplicates / trials

# Test group sizes from 1 to 75 people
for group_size in range(1, 76):
    probability = has_duplicate_birthdays(group_size)
    # Convert probability to a percentage for easier interpretation
    print(f"For {group_size} people, probability of a shared birthday: {probability * 100:.2f}%")
