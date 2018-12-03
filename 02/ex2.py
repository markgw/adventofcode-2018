#!/usr/bin/python3

with open("input.txt", "r") as f:
    # Read in the whole file and split up the lines to get all the IDs
    all_ids = f.read().splitlines()


def find_matching():
    for box_num1, box_id1 in enumerate(all_ids):
        # Compare this box ID to all others (except itself)
        for box_num2, box_id2 in enumerate(all_ids):
            # Don't compare to yourself!
            if box_num1 != box_num2:
                # See how many characters are different between the two IDs
                compare_chars = [
                    # Put a 1 in the list if the characters differ
                    1 if x != y else 0
                    # zip puts together pairs of characters (x, y) from the same positions in the strings
                    for (x, y) in zip(box_id1, box_id2)
                ]
                # We're looking for a pair that differs by exactly one character
                if sum(compare_chars) == 1:
                    # Find which character was the different one
                    diff_char = compare_chars.index(1)
                    # Extract the common string
                    common = box_id1[:diff_char] + box_id1[diff_char+1:]
                    return box_id1, box_id2, common


matching_id1, matching_id2, common_id = find_matching()

print("Found matching ID pair: {} - {}".format(matching_id1, matching_id2))
print("Common part: {}".format(common_id))
