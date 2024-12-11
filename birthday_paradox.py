import random

def has_duplicate_birthdays(num_people, trials=10000):
    """
    Estimate the probability of having at least one shared birthday
    among num_people people.
    """
    count_duplicates = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(set(birthdays)) < len(birthdays):
            # If there's a duplicate, increment
            count_duplicates += 1
    return count_duplicates / trials

# Test for group sizes from, say, 5 to 50
for group_size in range(5, 51, 5):
    probability = has_duplicate_birthdays(group_size)
    print(f"For {group_size} people, probability of a shared birthday ~ {probability:.2f}")
