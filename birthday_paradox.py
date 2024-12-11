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
            count_duplicates += 1
    return count_duplicates / trials

# Test group sizes from 1 to 75
for group_size in range(1, 76):
    probability = has_duplicate_birthdays(group_size)
    print(f"For {group_size} people, probability of a shared birthday: {probability * 100:.2f}%")
