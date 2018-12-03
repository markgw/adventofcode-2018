#!/usr/bin/python3

# Start the frequency on 0
freq = 0

# Keep track of all frequencies we've seen
all_freqs = set()

# Loop over the list as many times as it takes to reach a repeated frequency
found_repeat = False
# Just for output
repeats = 0

while not found_repeat:
    repeats += 1
    print("Looping over list {}. time".format(repeats))

    # Read in the file line by line
    with open("input.txt", "r") as f:
        for line in f:
            # Get the frequency change and apply it
            freq += int(line.strip("\n"))
            if freq in all_freqs:
                # Found a repeat
                found_repeat = True
                break
            # Keep the frequency to see if it gets repeated
            all_freqs.add(freq)

# The final frequency we're left with after stopping is the one we're looking for
print("Found repeated frequency: {}".format(freq))
