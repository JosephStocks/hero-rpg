import random

# choice = random.choices(["regular", "double"], [80, 20])
choices = []
for _ in range(1000):
    choices.append(random.choices(["regular", "double"], [80, 20])[0])
regular_count = 0
double_count = 0
for choice in choices:
    if choice == "regular":
        regular_count += 1
    else:
        double_count += 1

print(f"regulars={regular_count} {regular_count / (regular_count + double_count)}%")
print(f"doubles={double_count} {double_count / (regular_count + double_count)}%")