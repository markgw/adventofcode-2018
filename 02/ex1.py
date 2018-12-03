#!/usr/bin/python3
from collections import Counter

with open("input.txt", "r") as f:
    # Read in the whole file and split up the lines to get all the IDs
    all_ids = f.read().splitlines()

# Count up the strings with chars that appear twice
double_chars = 0
# And three times
triple_chars = 0

for box_id in all_ids:
    # Count up the letters in the string
    # Note that a string is a sequence of characters, so when you put it into
    # a Counter, it counts up the number of times each character is used
    char_counts = Counter(box_id)

    # Check whether any character occurs twice
    if any(count == 2 for (char, count) in char_counts.items()):
        double_chars += 1

    # Check whether any character occurs three times
    if any(count == 3 for (char, count) in char_counts.items()):
        triple_chars += 1

print("{} IDs have double characters".format(double_chars))
print("{} IDs have triple characters".format(triple_chars))
print("Checksum: {}".format(double_chars * triple_chars))
